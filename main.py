import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_i18n import I18nMiddleware, I18nContext
from aiogram_i18n.cores import FluentRuntimeCore

import private_cfg as config
from data.repository.users import UserRepository
from domain.handlers.admin import main_admin
from domain.handlers.client import main_client
from domain.middlewares.UserRegistrationMiddleware import UserRegistrationMiddleware
from domain.middlewares.LocaleManager import LocaleManager


storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(
    main_client.router,
    main_admin.router,
)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.BOT_TOKEN, default=default_properties)

    try:
        i18n_middleware = I18nMiddleware(
            core=FluentRuntimeCore(path='presentation/locales'),
            default_locale='en',
            manager=LocaleManager()
        )

        i18n_middleware.setup(dp)

        dp.message.outer_middleware(UserRegistrationMiddleware())  # register if client not registered
        dp.callback_query.outer_middleware(UserRegistrationMiddleware())  # register if client not registered
        # dp.business_message.outer_middleware(UserRegistrationMiddleware())  # register if client not registered

        # start bot
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(f"start bot: {e}")
        return


if __name__ == '__main__':
    asyncio.run(main())
