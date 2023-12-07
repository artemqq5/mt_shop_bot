from data.constants.base_constants import ADMIN
from data.repository import MyRepository


async def notify_new_task(message, category):
    admins = MyRepository().get_users(position=ADMIN)

    name_user = f"from @{message.chat.username}" if message.chat.username is not None else ""
    info_task = f"New task ({category}) {name_user}"

    for admin in admins:
        await message.bot.send_message(chat_id=admin['id'], text=info_task)
