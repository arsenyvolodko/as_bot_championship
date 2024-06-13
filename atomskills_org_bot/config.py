import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("CHAMPIONSHIP_BOT_TOKEN")
DATABASE_URL = os.environ.get("CHAMPIONSHIP_DATABASE_URL")
