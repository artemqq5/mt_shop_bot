from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repository.users import UserRepository


class IsUserAdmin(BaseMiddleware):

    def __init__(self, role):
        self.role = role

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user_id = event.from_user.id

        if not UserRepository().user(user_id)['role'] == self.role:
            return

        return await handler(event, data)
