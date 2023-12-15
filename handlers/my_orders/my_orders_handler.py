from aiogram import types
from aiogram.dispatcher import FSMContext

from data.constants.admin_constants import CREO_TYPE, ACCOUNT_TYPE, SET_MESSAGE_TO_PUSH, PUSH_HAVE_SENT, \
    PUSH_HAVE_NOT_SENT
from data.constants.base_constants import *
from data.repository.accounts import AccountsRepository
from data.repository.orders import OrdersRepository
from handlers.my_orders.message_format.view_task_message import creo_task_view, account_task_view
from handlers.my_orders.message_format.statistic_message import general_statistic_format
from keyboard.base_keyboard import cancel_keyboard
from keyboard.my_orders.my_orders_keyboard import *
from notify.notify_push_task import message_to_admin_from_client
from states.user_orders.user_orders_state import UserOrdersState


def register_my_order_handlers(dispatcher):
    dispatcher.register_message_handler(user_type_view, lambda m: m.text in LIST_OF_USER_VIEW,
                                        state=UserOrdersState.view)
    dispatcher.register_message_handler(user_status_view, lambda m: m.text in (ACTIVE_ORDERS, COMPLETED_ORDERS),
                                        state=UserOrdersState.status)
    dispatcher.register_callback_query_handler(user_task_active_view_query,
                                               lambda call: call.data.split("_")[0] == ACTIVE,
                                               state=UserOrdersState.status)
    dispatcher.register_callback_query_handler(user_task_completed_view_query,
                                               lambda call: call.data.split("_")[0] == COMPLETED,
                                               state=UserOrdersState.status)
    dispatcher.register_callback_query_handler(user_task_question,
                                               lambda call: call.data.split("_")[0] == MESSAGE_,
                                               state=UserOrdersState.status)
    dispatcher.register_message_handler(task_question_message, state=UserOrdersState.message)


async def user_type_view(message: types.Message, state: FSMContext):
    text = message.text
    if text == GENERAL_STATISTICS:
        await message.answer(general_statistic_format(message), reply_markup=user_view_choice_keyboard())
    elif text == DESIGN:
        await state.update_data(view=CREO_TYPE)
        await UserOrdersState.next()
        await message.answer(STATUS_OF_ORDERS_USER, reply_markup=user_view_type_orders_keyboard())
    elif text == ACCOUNTS:
        await state.update_data(view=ACCOUNT_TYPE)
        await UserOrdersState.next()
        await message.answer(STATUS_OF_ORDERS_USER, reply_markup=user_view_type_orders_keyboard())


async def user_status_view(message: types.Message, state: FSMContext):
    type_order = await state.get_data()
    if message.text == ACTIVE_ORDERS:
        orders = OrdersRepository().get_user_orders(ACTIVE, message.chat.id, type_order['view'])
        await message.answer(ACTIVE_ORDERS, reply_markup=user_task_keyboard(orders))
    elif message.text == COMPLETED_ORDERS:
        orders = OrdersRepository().get_user_orders(COMPLETED, message.chat.id, type_order['view'])
        await message.answer(COMPLETED_ORDERS, reply_markup=user_task_keyboard(orders))


async def user_task_active_view_query(callback: types.CallbackQuery):
    task_type = callback.data.split("_")[1]
    task_id = callback.data.split("_")[2]

    if task_type == CREO_TYPE:
        task = creo_task_view(CreosRepository().get_creo(task_id))
    elif task_type == ACCOUNT_TYPE:
        task = account_task_view(OrdersRepository().get_account_order(task_id))
    else:
        task = TASK_NOT_AVAILABLE

    await callback.message.answer(task, reply_markup=call_about_task_keyboard(task_id))


async def user_task_completed_view_query(callback: types.CallbackQuery):
    task_type = callback.data.split("_")[1]
    task_id = callback.data.split("_")[2]

    if task_type == CREO_TYPE:
        task = creo_task_view(CreosRepository().get_creo(task_id))
    elif task_type == ACCOUNT_TYPE:
        task = account_task_view(OrdersRepository().get_account_order(task_id))
    else:
        task = TASK_NOT_AVAILABLE

    await callback.message.answer(task)


async def user_task_question(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data.split("_")[1]
    await UserOrdersState.next()
    await state.update_data(message=task_id)
    await callback.message.answer(SET_MESSAGE_TO_PUSH, reply_markup=cancel_keyboard())


async def task_question_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message_to_admin_from_client(message, message.text, data['message'])
    await UserOrdersState.view.set()
    await message.answer(text=PUSH_HAVE_SENT, reply_markup=user_view_choice_keyboard())

