from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repositoryDB.UserRepository import UserRepository
from domain.notify.NotificationAdmin import NotificationAdmin


class UserRegistrationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user = event.from_user

        if not UserRepository().get_user(user.id):
            if not UserRepository().add_user(user.id, user.username, user.first_name, user.last_name, user.language_code):
                await event.bot.send_message(chat_id=user.id, text=data['i18n'].REGISTER_FAIL())
                return None

            await NotificationAdmin().new_user_db(data['bot'], data['i18n'], UserRepository().get_user(user.id))

            await event.bot.send_message(chat_id=user.id, text=data['i18n'].REGISTER_SUCCESS())

        return await handler(event, data)

