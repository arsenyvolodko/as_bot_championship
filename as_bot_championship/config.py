import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BUSINESS_PROGRAM_BOT_TOKEN")
DATABASE_URL = os.environ.get("BUSINESS_PROGRAM_DATABASE_URL")
