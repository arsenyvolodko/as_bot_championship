from aiogram import types

from atomskills_org_bot.db.manager import db_manager
from atomskills_org_bot.db.tables import User


async def add_and_get_user(message: types.Message):
    user_id = message.from_user.id
    user = await db_manager.get_record(User, user_id)
    if not user:
        new_user = User(id=user_id, username=message.from_user.username)
        user = await db_manager.add_record(new_user)
    return user
