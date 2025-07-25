import io
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore
from fastapi import FastAPI

from bot.config import BOT_TOKEN, LOG_PATH
from bot.domain.middlewares.LocaleManager import LocaleManager

utf8_stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_PATH, encoding="utf-8"), logging.StreamHandler()],
)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=BOT_TOKEN, default=default_properties, timeout=60)

app = FastAPI()

i18n_middleware = I18nMiddleware(
    core=FluentRuntimeCore(path="locales"),
    default_locale="en",
    manager=LocaleManager(),
)
