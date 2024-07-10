from dev.constants.base_constants import ADMIN
from data.repository.users import UsersRepository


async def user_activate_bot(telegram_id, bot):
    try:
        admins = UsersRepository().get_users(position=ADMIN)
        user = UsersRepository().get_user(telegram_id)

        message = f"👤 <b>Новий користувач доєднався до боту!</b>\n\nІм'я: <b>@{user['name']}</b>\nТелеграм ID: <b>{user['id']}</b>\nЧас: <b>{user['time']}</b>"

        for admin in admins:
            await bot.send_message(chat_id=admin['id'], text=message)

    except Exception as e:
        print(f"user_activate_bot: {e}")

