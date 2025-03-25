import paginate
from aiogram.utils.keyboard import InlineKeyboardBuilder

from as_bot_championship.consts import *
from as_bot_championship.db.tables import Location, Service, Option
from as_bot_championship.enums import PageButtonEnum, AnswerStatusEnum
from as_bot_championship.keyboards.button_factories import *


def get_back_to_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=GO_TO_MAIN_MENU, callback_data=BACK_TO_MAIN_MENU_CALLBACK)
    return builder.as_markup()


def get_hall_choice_keyboard(options: list[Option]):
    builder = InlineKeyboardBuilder()
    for item in options:
        builder.button(
            text=item.name,
            callback_data=HallChoiceFactory(
                hall_id=item.id,
            ),
        )

    builder.adjust(2)
    return builder.as_markup()


def get_location_choice_keyboard(options: list[Location], hall_id: int, page_num: int):
    builder = InlineKeyboardBuilder()
    page = paginate.Page(options, items_per_page=8, page=page_num)
    items: list[Location] = page.items
    for item in items:
        builder.button(
            text=item.name,
            callback_data=LocationChoiceFactory(hall_id=hall_id, location_id=item.id),
        )

    if page_num > 1:
        builder.button(
            text=PageButtonEnum.PREVIOUS_PAGE.value,
            callback_data=LocationPageFactory(
                page_num=page_num - 1,
                hall_id=hall_id,
            ),
        )
        builder.adjust(1)

    builder.button(text=BACK_TO_MENU, callback_data=BACK_TO_MAIN_MENU_CALLBACK)

    if page_num == 1:
        builder.adjust(1)

    if page_num < page.page_count:
        builder.button(
            text=PageButtonEnum.NEXT_PAGE.value,
            callback_data=LocationPageFactory(
                page_num=page_num + 1,
                hall_id=hall_id,
            ),
        )
    return builder.as_markup()


def get_service_choice_keyboard(
    options: list[Service], hall_id: int, location_id: int, page_num: int
):
    builder = InlineKeyboardBuilder()
    page = paginate.Page(options, items_per_page=5, page=page_num)
    items: list[Service] = page.items
    items.sort(key=lambda x: x.id)
    for item in items:
        builder.button(
            text=item.name,
            callback_data=ServiceChoiceFactory(
                hall_id=hall_id, location_id=location_id, service_id=item.id
            ),
        )

    if page_num > 1:
        builder.button(
            text=PageButtonEnum.PREVIOUS_PAGE.value,
            callback_data=ServicePageFactory(
                hall_id=hall_id,
                location_id=location_id,
                page_num=page_num - 1,
            ),
        )
        builder.adjust(1)

    builder.button(text=BACK_TO_MENU, callback_data=BACK_TO_MAIN_MENU_CALLBACK)

    if page_num == 1:
        builder.adjust(1)

    if page_num < page.page_count:
        builder.button(
            text=PageButtonEnum.NEXT_PAGE.value,
            callback_data=ServicePageFactory(
                hall_id=hall_id,
                location_id=location_id,
                page_num=page_num + 1,
            ),
        )
    return builder.as_markup()


def get_option_choice_keyboard(
    options: list[Option], hall_id: int, location_id: int, service_id
):
    builder = InlineKeyboardBuilder()
    options.sort(key=lambda x: x.id)
    for item in options:
        builder.button(
            text=item.name,
            callback_data=OptionChoiceFactory(
                hall_id=hall_id,
                location_id=location_id,
                service_id=service_id,
                option_id=item.id,
            ),
        )

    builder.button(text=BACK_TO_MENU, callback_data=BACK_TO_MAIN_MENU_CALLBACK)
    builder.adjust(1)
    return builder.as_markup()


def get_skip_keyboard(location_id: int, option_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=SKIP_COMMENT_TEXT,
        callback_data=SkipFactory(location_id=location_id, option_id=option_id),
    )
    return builder.as_markup()


def get_confirmation_keyboard(
    service: Service, location: Location, option: Option
):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=CANCEL_TEXT,
        callback_data=ConfirmationFactory(
            service_id=service.id,
            location_id=location.id,
            option_id=option.id,
            confirmed=False
        )
    )
    builder.button(
        text=CONFIRM_TEXT,
        callback_data=ConfirmationFactory(
            service_id=service.id,
            location_id=location.id,
            option_id=option.id,
            confirmed=True
        ),
    )
    builder.adjust(2)
    return builder.as_markup()


def get_service_ans_keyboard(request_id: int):
    builder = InlineKeyboardBuilder()
    options: list[AnswerStatusEnum] = AnswerStatusEnum.get_answer_options()
    for option in options:
        builder.button(
            text=option.value,
            callback_data=ServiceAnswerFactory(
                callback=option.value,
                request_id=request_id
            ),
        )
    builder.adjust(1)
    return builder.as_markup()


def get_mark_as_closed_keyboard(request_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=MARK_AS_CLOSE_TEXT,
        callback_data=CloseRequestFactory(
            request_id=request_id
        )
    )
    return builder.as_markup()
