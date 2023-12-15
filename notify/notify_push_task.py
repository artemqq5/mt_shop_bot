from aiogram.utils.exceptions import ChatNotFound, BotBlocked

from data.constants.admin_constants import *
from data.constants.base_constants import ADMIN, CLIENT, SUB_POSITION_CREO, SUB_POSITION_ACCOUNT
from data.repository.accounts import AccountsRepository
from data.repository.creos import CreosRepository
from data.repository.orders import OrdersRepository
from data.repository.users import UsersRepository
from handlers.my_orders.message_format.task_for_notification import creo_notify_formatted, account_notify_formatted
from keyboard.menu.menu_keyboard import main_keyboard


async def notify_new_task(message, category, id_order):
    admins = UsersRepository().get_users(position=ADMIN)

    name_user = f"@{message.chat.username}" if message.chat.username is not None else ""

    if category == CREO_TYPE:
        data = CreosRepository().get_creo(id_order)
        info_task = f"<b>#{data['id']} Новый заказ | {DESIGN} | {data['type']}</b>\n\n"
        info_task += f"{data['format']} | {data['category']}\n\n"
        info_task += f"{data['description']}\n\n"
        info_task += f"дедлайн: {data['deadline']}\n\n"
        info_task += f"<b>Контакт:</b> {name_user}"
    elif category == ACCOUNT_TYPE:
        data = OrdersRepository().get_account_order(id_order)
        info_task = f"<b>#{data['id']} Новый заказ | {data['name']}</b>\n\n"
        info_task += f"geo: {data['geo']} | кол-во: {data['count']} | {data['type']}\n\n"
        info_task += f"{data['desc']}\n\n"
        info_task += f"дополнтительно: {data['desc_from_user']}\n\n"
        info_task += f"<b>Контакт:</b> {name_user}"
    else:
        info_task = "Невідоме сповіщення"  # todo optional

    try:
        for admin in admins:
            if category == CREO_TYPE and admin['sub_position'] == SUB_POSITION_CREO:
                await message.bot.send_message(chat_id=admin['id'], text=info_task)
            elif category == ACCOUNT_TYPE and admin['sub_position'] == SUB_POSITION_ACCOUNT:
                await message.bot.send_message(chat_id=admin['id'], text=info_task)
            elif admin['sub_position'] is None:
                await message.bot.send_message(chat_id=admin['id'], text=info_task)
    except Exception as e:
        print(f"notify_new_task: {e}")


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


async def message_to_admin_from_client(message, text, order_id):
    task = OrdersRepository().get_order(order_id)

    admins = UsersRepository().get_users(position=ADMIN)
    user = UsersRepository().get_user(message.chat.id)

    if task is not None:
        try:
            if task['type'] == CREO_TYPE:
                creo_task = CreosRepository().get_creo(order_id)
                for admin in admins:
                    if admin['sub_position'] != SUB_POSITION_ACCOUNT:
                        await message.bot.send_message(chat_id=admin['id'],
                                                       text=creo_notify_formatted(creo_task, text, user))
            elif task['type'] == ACCOUNT_TYPE:
                account_task = OrdersRepository().get_account_order(order_id)
                for admin in admins:
                    if admin['sub_position'] != SUB_POSITION_CREO:
                        await message.bot.send_message(chat_id=admin['id'],
                                                       text=account_notify_formatted(account_task, text, user))
        except Exception as e:
            print(f"message_to_admin_from_client: {e}")
