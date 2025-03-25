import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
DATABASE_URL = os.environ.get("DATABASE_URL")
COMMON_CHAT_ID = int(os.environ.get("COMMON_CHAT_ID"))
