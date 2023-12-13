from aiogram.utils.exceptions import ChatNotFound, BotBlocked

from data.constants.admin_constants import *
from data.constants.base_constants import ADMIN, CLIENT, SUB_POSITION_CREO, SUB_POSITION_ACCOUNT
from data.repository.users import UsersRepository
from keyboard.menu.menu_keyboard import main_keyboard


async def notify_new_task(message, category):
    admins = UsersRepository().get_users(position=ADMIN)

    name_user = f"from @{message.chat.username}" if message.chat.username is not None else ""
    info_task = f"New task ({category}) {name_user}"

    for admin in admins:
        if category == CREO_TYPE and admin['sub_position'] == SUB_POSITION_CREO:
            await message.bot.send_message(chat_id=admin['id'], text=info_task)
        elif category == ACCOUNT_TYPE and admin['sub_position'] == SUB_POSITION_ACCOUNT:
            await message.bot.send_message(chat_id=admin['id'], text=info_task)
        elif admin['sub_position'] is None:
            await message.bot.send_message(chat_id=admin['id'], text=info_task)


async def push_users(message, text, user_id=None):
    try:
        if user_id is not None:
            await message.bot.send_message(chat_id=user_id, text=text)
            await message.answer(PUSH_HAVE_SENT, reply_markup=main_keyboard(message))
        else:
            users = UsersRepository().get_users(CLIENT)
            counter = 0
            for user in users:
                try:
                    await message.bot.send_message(chat_id=user['id'], text=text)
                    counter += 1
                except Exception as e:
                    print(f"push user(all): {e}")
            await message.answer(PUSH_HAVE_SENT_ALL(len(users), counter), reply_markup=main_keyboard(message))
    except ChatNotFound as e:
        print(f"push user(individual): {e}")
        await message.answer(PUSH_ERROR_SENT_USER_NOT_EXIST, reply_markup=main_keyboard(message))
    except BotBlocked as e:
        print(f"push user(individual): {e}")
        await message.answer(PUSH_ERROR_SENT_USER_NOT_START_BOT, reply_markup=main_keyboard(message))
