from aiogram.types import User
from aiogram_i18n.managers import BaseManager

from data.repositoryDB.UserRepository import UserRepository


class LocaleManager(BaseManager):

    async def set_locale(self, locale: str) -> str:
        pass

    async def get_locale(self, event_from_user: User) -> str:
        user_database = UserRepository().get_user(event_from_user.id)
        if not user_database or not user_database['lang']:
            return event_from_user.language_code

        return user_database['lang']
