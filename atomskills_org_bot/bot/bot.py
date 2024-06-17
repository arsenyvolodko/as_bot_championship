from aiogram import Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from atomskills_org_bot.consts import (
    CANCEL_CALLBACK,
    START_TEXT,
    HELP_TEXT,
    STATUS_INFO,
)
from atomskills_org_bot.db.manager import db_manager
from atomskills_org_bot.db.tables import Request, User
from atomskills_org_bot.enums import ServiceNameEnum, ServiceChatIdEnum
from atomskills_org_bot.enums.answer_status_enum import AnswerStatusEnum
from atomskills_org_bot.models import ServiceModel
from atomskills_org_bot.utils import (
    text_in_service_models,
    ServiceAnswerCallback,
    add_and_get_user,
)
from atomskills_org_bot.utils.keyboards import (
    get_main_keyboard,
    get_cancel_keyboard,
    get_service_ans_keyboard,
)

from aiogram.fsm.context import FSMContext

from atomskills_org_bot.utils.services import SERVICE_MODELS

dp = Dispatcher()
router = Router()
dp.include_router(router)


@dp.message(CommandStart())
async def welcome_message(message: types.Message, state: FSMContext) -> None:
    if not message.from_user.username:
        await message.answer(
            "Для использования бота необходимо установить имя пользователя (username) - это можно сделать в настройках телеграм."
        )
        return
    await add_and_get_user(message)
    if state:
        await state.clear()
    await message.answer(START_TEXT, reply_markup=get_main_keyboard())


@router.message(Command("help"))
async def handle_main_menu_callback(message: Message):
    await message.answer(
        text=HELP_TEXT,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )


@router.message(text_in_service_models)
async def process_callback_button1(message: Message, state: FSMContext = None):
    service: ServiceModel = SERVICE_MODELS[message.text]

    current_state = await state.get_state()
    if current_state:
        data = await state.get_data()
        old_msg = data["message"]
        await old_msg.delete()

    await state.set_state(service.state.value)
    message = await message.answer(
        f'Ваше обращение будет направлено в сервис "{service.service_name.value}".\n'
        'Отправьте сообщение с текстом обращения, Не забудьте указать всю необходимую информацию для представителей сервиса.\n'
        "После отправки сообщения обращение будет автоматически направлено в выбранный сервис.",
        reply_markup=get_cancel_keyboard(),
    )
    await state.set_data({"message": message, "service": service})


@router.message()
async def handle_request_message(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if not current_state:
        await message.answer(
            "Сервис не выбран. Для отправки обращения, необходимо сначала выбрать сервис, воспользовавшись клавиатурой",
            reply_markup=get_main_keyboard(),
        )
        return

    state_data = await state.get_data()
    old_msg: Message = state_data["message"]
    service: ServiceModel = state_data["service"]
    await old_msg.delete()
    await state.clear()

    new_request = Request(
        user_id=message.from_user.id, text=message.text, service=service.service_name
    )

    request: Request = await db_manager.add_record(new_request)
    await send_request(message.bot, request)

    text_to_source = (
        "Ваше обращение было отправлено.\n"
        f"Сервис-получатель: {service.service_name.value}.\n"
        f"Уникальный номер вашего обращения: {request.id}.\n"
        f"Мы сообщим, ориентировочное время выполнения после ответа представителя сервиса.\n"
    )

    msg_to_source = await message.answer(
        text=text_to_source + f"{STATUS_INFO.format(AnswerStatusEnum.IGNORED.value)}",
    )

    text_to_common = (
        f"Обращение №{request.id}:\n"
        f'Текст обращения: "{request.text}"\n'
        f"Сервис-получатель: {service.service_name.value}.\n"
        f"Направлено от: @{message.from_user.username}.\n"
    )

    msg_to_common = await message.bot.send_message(
        chat_id=ServiceChatIdEnum.COMMON_CHAT_ID.value,
        text=text_to_common + f"{STATUS_INFO.format(AnswerStatusEnum.IGNORED.value)}",
    )

    try:
        await db_manager.update_record(
            Request,
            request.id,
            source_chat_msg_id=msg_to_source.message_id,
            common_chat_msg_id=msg_to_common.message_id,
            source_chat_msg_text=text_to_source,
            common_chat_msg_text=text_to_common,
        )
    except Exception as e:
        await msg_to_source.delete()
        await msg_to_common.delete()
        await message.answer(
            text="Что-то пошло не так, обращение не было отправлено. Пожалуйста, повторите попытку еще раз.",
            reply_markup=get_main_keyboard(),
        )
        await message.bot.send_message(
            chat_id=ServiceChatIdEnum.MY_CHAT_ID.value,
            text=f"error sending request from @{message.from_user.username} to"
                 f"{service.service_name.value}.\nerror: {e}",
        )


async def send_request(bot, request: Request):
    service: ServiceNameEnum = request.service
    user = await db_manager.get_record(User, request.user_id)
    text = (
        "Вам поступило обращение:\n"
        f"Направлено от: @{user.username}.\n"
        f'Текст обращения: "{request.text}"\n\n'
        "Укажите ориентировочное время, необходимое для его выполнения - мы сообщим его отправителю."
    )
    chat_id = SERVICE_MODELS[service.value].chat_id
    await bot.send_message(
        chat_id=chat_id, text=text, reply_markup=get_service_ans_keyboard(request.id)
    )


@dp.callback_query(F.data == CANCEL_CALLBACK)
async def handle_query(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_reply_markup(None)
    await call.message.answer("Обращение отменено.", reply_markup=get_main_keyboard())


@router.callback_query(ServiceAnswerCallback.filter())
async def handle_query(call: types.CallbackQuery, callback_data: ServiceAnswerCallback):
    request: Request = await db_manager.get_record(Request, callback_data.request_id)
    if callback_data.callback == AnswerStatusEnum.DENY.value:
        additional_common_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.DENIED.value)}\n"
            f"Представитель сервиса, отклонивший обращение - @{call.from_user.username}."
        )
        additional_source_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.DENIED.value)}"
        )
        text_to_source = (
            f"Ваше обращение №{request.id} было отклонено.\n"
            f"Убедитесь, что Вы направили обращение в тот чат - используйте команду /help.\n"
            f"Также вы можете связаться с представителем сервиса напрямую - @{call.from_user.username}."
        )
    else:
        additional_common_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.RESOLVED.value)}\n"
            f"Ориентировочное время выполнения: {callback_data.callback}.\n"
            f"Исполнитель: @{call.from_user.username}."
        )
        additional_source_chat_text = (
            f"{STATUS_INFO.format(AnswerStatusEnum.RESOLVED.value)}\n"
            f"Представитель сервиса: @{call.from_user.username}."
        )
        text_to_source = (
            f"Ваше обращение №{request.id} было принято в работу.\n"
            f"Ориентировочное время выполения: {callback_data.callback}.\n"
            f"При необходимости, вы можете связаться с представителем сервиса напрямую: @{call.from_user.username}."
        )

    await call.bot.edit_message_text(
        chat_id=ServiceChatIdEnum.COMMON_CHAT_ID.value,
        message_id=request.common_chat_msg_id,
        text=request.common_chat_msg_text + additional_common_chat_text,
    )
    await call.bot.edit_message_text(
        chat_id=request.user_id,
        message_id=request.source_chat_msg_id,
        text=request.source_chat_msg_text + additional_source_chat_text,
    )
    await call.bot.send_message(
        chat_id=request.user_id,
        text=text_to_source,
        reply_to_message_id=request.source_chat_msg_id,
        reply_markup=get_main_keyboard(),
    )

    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Ваш ответ был направлен отправителю.")
