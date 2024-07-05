from aiogram import types
from aiogram.dispatcher import FSMContext

from data.constants.admin_constants import SYSTEM_OF_BAN, BAN_USER_CATEGORY, INPUT_USER_ID_OR_USERNAME_FOR_BAN, \
    BAN_MESSAGE, BAN_MESSAGE_TOO_LONG, BAN_MESSAGE_PRE_VIEW, BAN_USER, ERROR_BANNED, SUCCESSFUL_BANNED, \
    DEFAULT_BAN_MESSAGE, SHOW_BANNED_USERS, BANNED_USERS_EMPTY
from data.constants.base_constants import SKIP
from data.repository.users import UsersRepository
from dev.keyboard.admin.admin_keyboard import admin_ban_system_keyboard, ban_user_keyboard
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from states.admin.ban_state import BanSystemState


def register_ban_system_handlers(dispatcher):
    dispatcher.register_message_handler(
        ban_category, lambda message: message.text == SYSTEM_OF_BAN
    )

    dispatcher.register_message_handler(
        all_banned_users, lambda message: message.text == SHOW_BANNED_USERS
    )

    dispatcher.register_message_handler(
        ban_user, lambda message: message.text == BAN_USER_CATEGORY
    )

    dispatcher.register_message_handler(
        ban_message, state=BanSystemState.ban
    )

    dispatcher.register_message_handler(
        ban_pre_finish, state=BanSystemState.message
    )

    dispatcher.register_message_handler(
        ban_finish, lambda message: message.text == BAN_USER, state=BanSystemState.finish
    )


async def ban_category(message: types.Message):
    await message.answer(SYSTEM_OF_BAN, reply_markup=admin_ban_system_keyboard())


async def all_banned_users(message: types.Message):
    list_of_banned_users = UsersRepository().get_all_banned_users()
    body = ""

    for user in list_of_banned_users:
        body += f"id: {user['id']}\nusername: @{user['name']}\nmessage: {user['banned_message']}\n\n"

    if not body:
        body = BANNED_USERS_EMPTY

    await message.answer(f"<b>{SHOW_BANNED_USERS}</b>\n\n{body}")


async def ban_user(message: types.Message):
    await BanSystemState.ban.set()
    await message.answer(INPUT_USER_ID_OR_USERNAME_FOR_BAN, reply_markup=cancel_keyboard())


async def ban_message(message: types.Message, state: FSMContext):
    await state.update_data(usertag=message.text)
    await BanSystemState.message.set()
    await message.answer(BAN_MESSAGE, reply_markup=skip_keyboard())


async def ban_pre_finish(message: types.Message, state: FSMContext):
    if len(message.text) > 255:
        await message.answer(BAN_MESSAGE_TOO_LONG, reply_markup=cancel_keyboard())
        return

    if message.text != SKIP:
        await state.update_data(message=message.text)
    else:
        await state.update_data(message=DEFAULT_BAN_MESSAGE)

    data = await state.get_data()

    await BanSystemState.finish.set()
    await message.answer(BAN_MESSAGE_PRE_VIEW.format(data['message']), reply_markup=ban_user_keyboard())


async def ban_finish(message: types.Message, state: FSMContext):
    data = await state.get_data()

    try:
        if data['usertag'].startswith("@"):
            if not UsersRepository().ban_user_by_username(data['usertag'].replace("@", "")):
                raise Exception

            UsersRepository().update_ban_message_by_username(data['usertag'].replace("@", ""), data['message'])

        else:
            if not UsersRepository().ban_user_by_id(data['usertag']):
                raise Exception

            UsersRepository().update_ban_message_by_id(data['usertag'], data['message'])

        await message.answer(SUCCESSFUL_BANNED, reply_markup=admin_ban_system_keyboard())
    except Exception as e:
        print(f"ban_finish: {e}")
        await message.answer(ERROR_BANNED, reply_markup=admin_ban_system_keyboard())
    finally:
        await state.set_data({})
        await state.finish()
