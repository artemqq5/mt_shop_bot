from aiogram import Bot
from aiogram_i18n import I18nContext

from data.repository.orders import OrderRepository
from data.repository.users import UserRepository


class NotificationAdmin:

    @staticmethod
    async def user_activate_bot(user_id: int, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)

        for admin in admins:
            with i18n.use_locale(admin['lang']):
                try:
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.NEW_USER(
                            username=user['username'],
                            user_id=user['user_id'],
                            join_at=user['join_at']
                        )
                    )
                    counter += 1
                except Exception as e:
                    print(f"user_activate_bot: {e}")

        print(f"messaging user_activate_bot {counter}/{len(admins)}")

    @staticmethod
    async def new_order(identify, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        order = OrderRepository().order_by_identify(identify)
        user = UserRepository().user(order['user_id'])

        username = f"@{user['username']}" if user['username'] else i18n.ADMIN.USERNAME_HAVNT()

        try:
            for admin in admins:
                with i18n.use_locale(user['lang']):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.NEW_ORDER(
                            id=order['id'],
                            date=order['date'],
                            category=order['category'],
                            count=order['count'],
                            price=order['total_cost'],
                            desc=order['desc'],
                            user_id=user['user_id'],
                            username=username
                        )
                    )
                    counter += 1

        except Exception as e:
            print(f"new_order: {e}")

        print(f"messaging new_order {counter}/{len(admins)}")
