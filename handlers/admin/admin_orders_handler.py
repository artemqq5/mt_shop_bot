from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from data.constants.base_constants import *
from handlers.admin.parse_data_db.orders_parse import *
from handlers.admin.trello_use_case.card_format import parse_to_trello_card_format
from handlers.admin.trello_use_case.send_task import MyTrelloManager, TrelloCard
from keyboard.admin.admin_keyboard import *
from keyboard.admin.admin_orders_keyboard import admin_orders_keyboard, inline_orders_keyboard, managment_order_keyboard
from keyboard.menu.menu_keyboard import main_keyboard


def register_orders_handler(dispatcher):
    dispatcher.register_message_handler(all_orders_handler, lambda message: message.text == ALL_ORDERS)
    dispatcher.register_message_handler(status_orders_handler, lambda message: message.text in ORDER_TYPES_LIST)
    dispatcher.register_callback_query_handler(details_orders_callback, lambda call: call.data in all_order_list_id())
    dispatcher.register_callback_query_handler(managment_order_callback,
                                               lambda call: call.data in all_order_status_change())
    dispatcher.register_callback_query_handler(send_to_trello_callback,
                                               lambda call: call.data in order_send_trello_list())


# category of orders (REVIEW_ORDERS, ACTIVE_ORDERS, COMPLETED_ORDERS, CANCELED_ORDERS)
async def all_orders_handler(message: types.Message):
    current_user = MyRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            await message.answer(ALL_ORDERS_LABEL, reply_markup=admin_orders_keyboard())
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


# Output orders from database
async def status_orders_handler(message: types.Message):
    current_user = MyRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:

            # show all order with status: review -------------------------------------------------
            if message.text == REVIEW_ORDERS:
                orders = MyRepository().get_orders(REVIEW)
                if len(orders) > 0:
                    await message.answer(REVIEW_ORDERS, reply_markup=inline_orders_keyboard(orders))
                else:
                    await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

            # show all order with status: active -------------------------------------------------
            elif message.text == ACTIVE_ORDERS:
                orders = MyRepository().get_orders(ACTIVE)
                if len(orders) > 0:
                    await message.answer(ACTIVE_ORDERS, reply_markup=inline_orders_keyboard(orders))
                else:
                    await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

            # show all order with status: completed -------------------------------------------------
            elif message.text == COMPLETED_ORDERS:
                orders = MyRepository().get_orders(COMPLETED)
                if len(orders) > 0:
                    await message.answer(COMPLETED_ORDERS, reply_markup=inline_orders_keyboard(orders))
                else:
                    await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

            # show all order with status: cancel -------------------------------------------------
            elif message.text == CANCELED_ORDERS:
                orders = MyRepository().get_orders(CANCELED)
                if len(orders) > 0:
                    await message.answer(CANCELED_ORDERS, reply_markup=inline_orders_keyboard(orders))
                else:
                    await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

            # not implemented -------------------------------------------------
            else:
                await message.answer(NOT_IMPLEMENTED)
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def details_orders_callback(callback: types.CallbackQuery):
    current_user = MyRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:

            order = MyRepository().get_order(callback.data)
            client = MyRepository().get_user(order['id_user'])

            if order is not None:
                if order['type'] == CREO_TYPE:
                    order_creo = MyRepository().get_creo(callback.data)
                    await callback.message.answer(
                        format_view_order(order_creo, client),
                        reply_markup=managment_order_keyboard(order)
                    )
                elif order['type'] == ACCOUNT_TYPE:
                    order_account = MyRepository().get_account_order(callback.data)
                    await callback.message.answer(
                        format_view_order(order_account, client),
                        reply_markup=managment_order_keyboard(order)
                    )
                else:
                    await callback.message.answer(NOT_IMPLEMENTED)
            else:
                await callback.message.answer(TASK_NOT_AVAILABLE)

        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def managment_order_callback(callback: types.CallbackQuery):
    current_user = MyRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            order_set_status = callback.data.split("_")[0]
            order_id = callback.data.split("_")[1]

            result = MyRepository().exchange_status_order(order_id, order_set_status)

            if result is not None:
                await callback.message.answer(STATUS_SUCCESFULY_EXCHANGE)
            else:
                await callback.message.answer(STATUS_NOT_EXCHANGE)

        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def send_to_trello_callback(callback: types.CallbackQuery):
    current_user = MyRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            order_id = callback.data.split("_")[1]
            task = MyRepository().get_order(order_id)
            task_creo = MyRepository().get_creo(order_id)
            client = MyRepository().get_user(task['id_user'])

            if task['status'] == REVIEW:

                result = MyTrelloManager().generate_task(parse_to_trello_card_format(task_creo, client))

                if result is not None:
                    MyRepository().exchange_status_order(order_id, ACTIVE)
                    await callback.message.answer(TASK_SUCCESFUL_SEND)

                    # id_card = result.json()['id']
                    # result_webhook = MyTrelloManager().set_webhook_card(id_card)
                    # print(result_webhook) todo set webhook in future
                else:
                    await callback.message.answer(TASK_FAIL_SEND)

        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())
