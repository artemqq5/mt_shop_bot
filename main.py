import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

import private_cfg as config
from domain.middlewares.IsUserBanned import UserBannedMiddleware
from domain.middlewares.IsUserRegistration import UserRegistrationMiddleware
from domain.middlewares.LocaleManager import LocaleManager
from domain.routers.admin import admin_handler
from domain.routers.common_route_ import localization_
from domain.routers.user import user_handler
from domain.routers.user_no_team import user_no_team_handler

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(
    admin_handler.router,
    user_handler.router,
    user_no_team_handler.router,
    localization_.route
)


async def main():
    logging.basicConfig(level=logging.INFO)
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.BOT_TOKEN, default=default_properties)

    try:
        i18n_middleware = I18nMiddleware(
            core=FluentRuntimeCore(path='locales'),
            default_locale='en',
            manager=LocaleManager()
        )

        i18n_middleware.setup(dp)

        dp.message.outer_middleware(UserRegistrationMiddleware())  # register if user not registered
        dp.callback_query.outer_middleware(UserRegistrationMiddleware())  # register if user not registered

        dp.message.outer_middleware(UserBannedMiddleware())  # check if user banned
        dp.callback_query.outer_middleware(UserBannedMiddleware())  # check if user banned

        # start bot
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(f"start bot: {e}")
        return


if __name__ == '__main__':
    asyncio.run(main())
