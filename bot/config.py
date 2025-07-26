import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_NAME = os.getenv('BOT_NAME')
WEBHOOK_BASE_URL = os.getenv('WEBHOOK_BASE_URL')
WEBHOOK_PATH = f"/mt-shop-bot/{BOT_TOKEN}"

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PASSWORD')

CHANNEL_ID = os.getenv('CHANNEL_ID')
CHANNEL_URL = os.getenv('CHANNEL_URL')

SUPPORT_CONTACT = os.getenv('SUPPORT_CONTACT')

WHITE_PAY_TOKEN = os.getenv('WHITE_PAY_TOKEN')
WHITE_PAY_WEBHOOK_TOKEN = os.getenv('WHITE_PAY_WEBHOOK_TOKEN')
WHITE_PAY_AUTHTOKEN = f"Bearer {os.getenv('WHITE_PAY_AUTHTOKEN')}"
WHITE_PAY_SLUG = os.getenv('WHITE_PAY_SLUG')

BOT_LINK = os.getenv('BOT_LINK')
LOG_PATH = os.getenv('LOG_PATH')

SECRET_SERVER_BOT_ALIVE = os.getenv("SECRET_SERVER_BOT_ALIVE")
MIXPANEL_TOKEN = os.getenv("MIXPANEL_TOKEN")
