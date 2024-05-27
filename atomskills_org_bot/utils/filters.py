from aiogram import types

from atomskills_org_bot.utils.services import SERVICE_MODELS


async def text_in_service_models(message: types.Message) -> bool:
    return message.text in SERVICE_MODELS
