from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject, ReplyKeyboardRemove

from data.repository.users import UserRepository


class UserBannedMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user_id = event.from_user.id

        if UserRepository().get_user(user_id)['banned']:
            await event.bot.send_message(chat_id=user_id, text=data['i18n'].YOU_ARE_BLOKED(), reply_markup=ReplyKeyboardRemove())
            return

        return await handler(event, data)

