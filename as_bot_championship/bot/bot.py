from aiogram import Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from as_bot_championship.db.manager import db_manager
from as_bot_championship.db.tables import Hall, Request, User
from as_bot_championship.keyboards.keyboards import *

dp = Dispatcher()
router = Router()
dp.include_router(router)


@router.message(CommandStart())
async def welcome_message(message: Message, state: FSMContext):
    if not message.from_user.username:
        await message.answer("Для пользования ботом необходимо установить имя пользователя (username), это можно сделать в настроках тг.")
        return
    await add_and_get_user(message)
    if state:
        await state.clear()
    await message.answer(START_TEXT, reply_markup=get_back_to_main_keyboard())


async def add_and_get_user(message: Message):
    user_id = message.from_user.id
    user = await db_manager.get_record(User, user_id)
    if not user:
        new_user = User(id=user_id, username=message.from_user.username)
        user = await db_manager.add_record(new_user)
    return user


@router.callback_query(F.data == BACK_TO_MAIN_MENU_CALLBACK)
async def handle_main_menu_callback(call: CallbackQuery):
    options = await db_manager.get_records(Hall)
    await call.message.edit_text(
        HALL_CHOICE_TEXT, reply_markup=get_hall_choice_keyboard(options)
    )


@router.callback_query(HallChoiceFactory.filter())
async def handle_hall_choice_callback(
    call: CallbackQuery, callback_data: HallChoiceFactory
):
    hall_id = callback_data.hall_id
    options = await db_manager.get_records(Location, hall_id=hall_id)
    await call.message.edit_text(
        LOCATION_CHOICE_TEXT,
        reply_markup=get_location_choice_keyboard(options, hall_id, 1),
    )


@router.callback_query(LocationPageFactory.filter())
async def handle_location_turn_page_callback(
    call: CallbackQuery, callback_data: LocationPageFactory
):
    hall_id = callback_data.hall_id
    options = await db_manager.get_records(Location, hall_id=hall_id)
    await call.message.edit_text(
        LOCATION_CHOICE_TEXT,
        reply_markup=get_location_choice_keyboard(
            options, hall_id, callback_data.page_num
        ),
    )


@router.callback_query(LocationChoiceFactory.filter())
async def handle_location_choice_callback(
    call: CallbackQuery, callback_data: LocationChoiceFactory
):
    hall_id = callback_data.hall_id
    options = await db_manager.get_records(Service)
    await call.message.edit_text(
        SERVICE_CHOICE_TEXT,
        reply_markup=get_service_choice_keyboard(
            options, hall_id, callback_data.location_id, 1
        ),
    )


@router.callback_query(ServicePageFactory.filter())
async def handle_service_turn_page_callback(
    call: CallbackQuery, callback_data: ServicePageFactory
):
    options = await db_manager.get_records(Service)
    await call.message.edit_text(
        SERVICE_CHOICE_TEXT,
        reply_markup=get_service_choice_keyboard(
            options,
            callback_data.hall_id,
            callback_data.location_id,
            callback_data.page_num,
        ),
    )


@router.callback_query(ServiceChoiceFactory.filter())
async def handle_service_choice_callback(
    call: CallbackQuery, callback_data: ServiceChoiceFactory
):
    service_id = callback_data.service_id
    options = await db_manager.get_records(Option, service_id=service_id)
    await call.message.edit_text(
        OPTION_CHOICE_TEXT,
        reply_markup=get_option_choice_keyboard(
            options, callback_data.hall_id, callback_data.location_id, service_id
        ),
    )


@router.callback_query(OptionChoiceFactory.filter())
async def handle_option_choice_callback(
    call: CallbackQuery, callback_data: OptionChoiceFactory, state: FSMContext
):
    await state.set_state(COMMENT_AWAITING_STATE)
    await state.set_data(
        {
            "msg_id": call.message.message_id,
            "location_id": callback_data.location_id,
            "option_id": callback_data.option_id,
        }
    )

    await call.message.edit_text(
        COMMENT_CHOICE_TEXT,
        reply_markup=get_skip_keyboard(
            callback_data.location_id, callback_data.option_id
        ),
    )


@router.callback_query(SkipFactory.filter())
async def handle_skip_callback(
    call: CallbackQuery, callback_data: SkipFactory, state: FSMContext
):
    await state.clear()

    location: Location = await db_manager.get_record(
        Location, callback_data.location_id
    )
    option: Option = await db_manager.get_record(Option, callback_data.option_id)
    service: Service = await db_manager.get_record(Service, option.service_id)

    msg_text = construct_confirmation_message(service.name, location.name, option.name)

    await call.message.edit_text(
        text=msg_text,
        reply_markup=get_confirmation_keyboard(service, location, option),
        parse_mode="HTML",
    )


@router.message(COMMENT_AWAITING_STATE)
async def handle_comment_message(message: Message, state: FSMContext):
    state_data = await state.get_data()
    await state.set_state(CONFIRMATION_AWAITING_STATE)
    await state.set_data({"comment": message.text})

    await message.bot.edit_message_reply_markup(
        chat_id=message.from_user.id, message_id=state_data["msg_id"], reply_markup=None
    )

    location: Location = await db_manager.get_record(
        Location, state_data["location_id"]
    )
    option: Option = await db_manager.get_record(Option, state_data["option_id"])
    service: Service = await db_manager.get_record(Service, option.service_id)

    msg_text = construct_confirmation_message(
        service.name, location.name, option.name, message.text
    )

    await message.answer(
        text=msg_text,
        reply_markup=get_confirmation_keyboard(service, location, option),
        parse_mode="HTML",
    )


def construct_confirmation_message(
    service: str, location: str, option: str, comment: str | None = None
) -> str:
    msg_text = (
        "Подтвердите отправку обращения.\n"
        f"<b>Тематика обращения</b>: {service}\n"
        f"<b>Компетенция</b>: {location}\n"
        f"<b>Цель обращения</b>: {option}\n"
    )

    if comment:
        msg_text += f"<b>Ваш комментарий</b>: {comment}"

    return msg_text


@router.callback_query(ConfirmationFactory.filter())
async def handle_confirmation_callback(
    call: CallbackQuery, callback_data: ConfirmationFactory
):
    options = await db_manager.get_records(Hall)
    if not callback_data.confirmed:
        await call.message.edit_text(text="Ваше обращение было отменено.")
        await call.message.answer(
            text=HALL_CHOICE_TEXT, reply_markup=get_hall_choice_keyboard(options)
        )
        return

    await call.message.delete_reply_markup()

    service: Service = await db_manager.get_record(Service, callback_data.service_id)
    location: Location = await db_manager.get_record(
        Location, callback_data.location_id
    )
    option: Option = await db_manager.get_record(Option, callback_data.option_id)
    comment = get_comment_from_message_text(call.message.text)

    new_request = Request(
        user_id=call.from_user.id,
        text=comment,
        service_id=service.id,
        location_id=location.id,
        option_id=option.id,
    )

    request: Request = await db_manager.add_record(new_request)
    await send_request(call.bot, request)

    text_to_source = (
        "Ваше обращение было успешно отправлено.\n"
        f"Уникальный номер вашего обращения: {request.id}.\n"
        f"Мы сообщим, ориентировочное время выполнения после ответа представителя выбранной тематики.\n"
    )

    msg_to_source = await call.message.answer(
        text=text_to_source + f"{STATUS_INFO.format(AnswerStatusEnum.IGNORED.value)}",
    )
    await call.message.answer(
        text=HALL_CHOICE_TEXT, reply_markup=get_hall_choice_keyboard(options)
    )

    text_to_common = (
        f"<b>Обращение №{request.id}:</b>\n"
        f"<b>Тематика обращения</b>: {service.name}.\n"
        f"<b>Компетенция</b>: {location.name}.\n"
        f"<b>Цель обращения</b>: {option.name}.\n"
        f"<b>Направлено от</b>: @{call.from_user.username}.\n"
    )
    if comment:
        text_to_common += f'<b>Текст обращения</b>: "{request.text}"\n'

    msg_to_common = await call.bot.send_message(
        chat_id=COMMON_CHAT_ID,
        text=text_to_common + f"{STATUS_INFO.format(AnswerStatusEnum.IGNORED.value)}",
        parse_mode="HTML",
    )

    await db_manager.update_record(
        Request,
        request.id,
        source_chat_msg_id=msg_to_source.message_id,
        common_chat_msg_id=msg_to_common.message_id,
        source_chat_msg_text=text_to_source,
        common_chat_msg_text=text_to_common,
    )


def get_comment_from_message_text(text: str):
    pattern = "Ваш комментарий: "
    return text[text.rfind(pattern) + len(pattern):] if pattern in text else None


async def send_request(bot, request: Request):
    service: Service = await db_manager.get_record(Service, request.service_id)
    location: Location = await db_manager.get_record(Location, request.location_id)
    option: Option = await db_manager.get_record(Option, request.option_id)
    user: User = await db_manager.get_record(User, request.user_id)

    text = (
        "Вам поступило обращение:\n"
        f"<b>Павильон №{location.hall_id}</b>.\n"
        f"<b>Компетенция</b>: {location.name}.\n"
        f"<b>Цель обращения</b>: {option.name}.\n"
        f"<b>Направлено от</b>: @{user.username}.\n"
    )

    if request.text:
        text += f'<b>Текст обращения</b>: "{request.text}"\n\n'
    text += "Укажите ориентировочное время, необходимое для его выполнения - мы сообщим его отправителю."

    await bot.send_message(
        chat_id=service.chat_id,
        text=text,
        reply_markup=get_service_ans_keyboard(request.id),
        parse_mode="HTML",
    )


@router.callback_query(ServiceAnswerFactory.filter())
async def handle_query(call: CallbackQuery, callback_data: ServiceAnswerFactory):
    request: Request = await db_manager.get_record(Request, callback_data.request_id)
    username = call.from_user.username
    if callback_data.callback == AnswerStatusEnum.DENY.value:
        additional_common_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.DENIED.value)}\n"
        )
        if username:
            additional_common_chat_text += f"Представитель выбранной тематике, отклонивший обращение - @{call.from_user.username}."
        additional_source_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.DENIED.value)}"
        )
        text_to_source = (
            f"Ваше обращение №{request.id} было отклонено.\n"
            # f"Убедитесь, что Вы направили обращение в тот чат - используйте команду /help.\n"
            f"Убедитесь, что Вы направили обращение в тот чат.\n"
        )
        if username:
            text_to_source += f"Также вы можете связаться с представителем выбранной тематики напрямую - @{call.from_user.username}."
    else:
        additional_common_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.RESOLVED.value)}\n"
            f"Ориентировочное время выполнения: {callback_data.callback}.\n"
        )
        if username:
            additional_common_chat_text += f"Исполнитель: @{call.from_user.username}."
        additional_source_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.RESOLVED.value)}\n"
        )
        if username:
            additional_source_chat_text += f"Представитель: @{call.from_user.username}."
        text_to_source = (
            f"Ваше обращение №{request.id} было принято в работу.\n"
            f"Ориентировочное время выполения: {callback_data.callback}.\n"
        )
        if username:
            text_to_source += f"При необходимости, вы можете связаться с представителем тематики напрямую: @{call.from_user.username}."

    options = await db_manager.get_records(Hall)

    new_common_chat_text = request.common_chat_msg_text + additional_common_chat_text
    new_source_chat_text = request.source_chat_msg_text + additional_source_chat_text

    await db_manager.update_record(Request, request.id, common_chat_msg_text=new_common_chat_text)
    await db_manager.update_record(Request, request.id, source_chat_msg_text=new_source_chat_text)

    await call.bot.edit_message_text(
        chat_id=COMMON_CHAT_ID,
        message_id=request.common_chat_msg_id,
        text=new_common_chat_text,
        parse_mode="HTML",
    )
    if callback_data.callback == AnswerStatusEnum.DENY.value:
        await call.bot.edit_message_text(
            chat_id=request.user_id,
            message_id=request.source_chat_msg_id,
            text=new_source_chat_text,
            parse_mode="HTML"
        )
    else:
        await call.bot.edit_message_text(
            chat_id=request.user_id,
            message_id=request.source_chat_msg_id,
            text=new_source_chat_text,
            parse_mode="HTML",
            reply_markup=get_mark_as_closed_keyboard(request.id)
        )
    await call.bot.send_message(
        chat_id=request.user_id,
        text=text_to_source,
        reply_to_message_id=request.source_chat_msg_id,
    )
    await call.bot.send_message(
        chat_id=request.user_id,
        text=HALL_CHOICE_TEXT,
        reply_markup=get_hall_choice_keyboard(options),
    )

    await call.message.delete_reply_markup()
    await call.message.answer("Ваш ответ был направлен отправителю.")


@router.callback_query(CloseRequestFactory.filter())
async def handle_close_request(call: CallbackQuery, callback_data: CloseRequestFactory):
    request: Request = await db_manager.get_record(Request, callback_data.request_id)
    new_source_text = request.source_chat_msg_text.replace(AnswerStatusEnum.RESOLVED.value, AnswerStatusEnum.CLOSED.value)
    new_common_text = request.common_chat_msg_text.replace(AnswerStatusEnum.RESOLVED.value, AnswerStatusEnum.CLOSED.value)
    await call.message.edit_text(
        text=new_source_text,
        parse_mode="HTML"
    )
    await call.bot.edit_message_text(
        text=new_common_text,
        chat_id=COMMON_CHAT_ID,
        message_id=request.common_chat_msg_id,
        parse_mode="HTML"
    )
