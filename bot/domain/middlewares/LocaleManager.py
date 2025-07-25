from aiogram.types import User
from aiogram_i18n.managers import BaseManager

from bot.data.repository.users import UserRepository


class LocaleManager(BaseManager):

    async def set_locale(self, locale: str) -> str:
        pass

    async def get_locale(self, event_from_user: User) -> str:
        current_user = UserRepository().user(event_from_user.id)
        return current_user["lang"] if current_user else event_from_user.language_code
