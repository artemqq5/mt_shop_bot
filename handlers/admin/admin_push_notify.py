from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.admin_constants import *
from data.constants.base_constants import ADMIN, NO_ACCESS, ERROR_REGISTER_MESSAGE, NOT_IMPLEMENTED
from data.repository import MyRepository
from keyboard.admin.admin_push_keyboard import *
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from notify.notify_push_task import push_users
from states.push.send_push_state import SendPushState


def register_push_handlers(dispatcher):
    dispatcher.register_message_handler(push_menu, lambda m: m.text == PUSH_NOTIFICATION)
    dispatcher.register_message_handler(set_type_push, lambda m: m.text in PUSH_TYPE_LIST, state=SendPushState.type)
    dispatcher.register_message_handler(set_user_push, state=SendPushState.id)
    dispatcher.register_message_handler(set_message_push, state=SendPushState.message)


async def push_menu(message: types.Message):
    current_user = MyRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ========================
            await SendPushState.type.set()
            await message.answer(TYPE_PUSH, reply_markup=admin_push_keyboard())
            # =============================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def set_type_push(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)

    if message.text == PUSH_INDIVIDUAL:
        await SendPushState.next()
        await message.answer(SET_USER_TO_PUSH, reply_markup=cancel_keyboard())
    elif message.text == PUSH_ALL_CLIENTS:
        await SendPushState.message.set()
        await message.answer(SET_MESSAGE_TO_PUSH, reply_markup=cancel_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)


async def set_user_push(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    await SendPushState.next()
    await message.answer(SET_MESSAGE_TO_PUSH, reply_markup=cancel_keyboard())


async def set_message_push(message: types.Message, state: FSMContext):
    await state.update_data(message=message.text)
    data = await state.get_data()
    await state.finish()

    result = await push_users(message, text=data['message'], user_id=data.get('id', None))




