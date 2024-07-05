from aiogram import Bot
from aiogram_i18n import I18nContext

from data.repository.users import UserRepository


class NotificationAdmin:

    @staticmethod
    async def user_activate_bot(user_id: int, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)

        try:
            for admin in admins:
                with i18n.use_locale(user['lang']):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.NEW_USER(
                            username=user['username'],
                            user_id=user['user_id'],
                            join_at=user['join_at']
                        )
                    )
                counter += 1
            pass

        except Exception as e:
            print(f"user_activate_bot: {e}")

        print(f"messaging {counter}/{len(admins)}")
