import asyncio
import logging
import sys

from aiogram import Bot

from atomskills_org_bot.bot.bot import dp
from atomskills_org_bot.config import BOT_TOKEN

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
