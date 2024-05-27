from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from atomskills_org_bot.consts import *
from atomskills_org_bot.enums.answer_status_enum import AnswerStatusEnum
from atomskills_org_bot.utils.services import SERVICE_MODELS
from atomskills_org_bot.utils.fabrics import ServiceAnswerCallback


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=i)] for i in SERVICE_MODELS],
        one_time_keyboard=True,
    )
    return keyboard


def get_cancel_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(text="Отмена", callback_data=CANCEL_CALLBACK)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_service_ans_keyboard(request_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    options: list[AnswerStatusEnum] = AnswerStatusEnum.get_answer_options()
    for option in options:
        builder.button(
            text=option.value,
            callback_data=ServiceAnswerCallback(
                callback=option.value, request_id=request_id
            ),
        )
    builder.adjust(1)
    return builder.as_markup()
