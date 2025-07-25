from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from bot.data.repository.users import UserRepository


class IsRoleMiddleware(BaseMiddleware):

    def __init__(self, *roles: str):
        self.roles = list(roles)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user_id = event.from_user.id

        user = UserRepository().user(user_id)

        if user and user["role"] in self.roles:
            data["current_user"] = user
            return await handler(event, data)

        return
