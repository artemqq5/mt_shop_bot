from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from config.cfg import ACTIVE_STATUS_TRELLO
from data.constants.base_constants import *
from handlers.admin.parse_data_db.orders_parse import *
from handlers.admin.trello_use_case.card_format import parse_to_trello_card_format
from handlers.admin.trello_use_case.send_task import MyTrelloManager, TrelloCard
from keyboard.admin.admin_keyboard import *
from keyboard.admin.admin_orders_keyboard import admin_orders_keyboard, inline_orders_keyboard, \
    managment_order_keyboard, type_of_orders_admin, send_refainement_keyboard
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.manage_orders_state import ManageOrderState


def register_orders_handler(dispatcher):
    dispatcher.register_message_handler(choice_orders_type, lambda message: message.text == ALL_ORDERS)
    dispatcher.register_message_handler(status_handler, lambda message: message.text in TYPE_OF_ORDERS,
                                        state=ManageOrderState.type)
    dispatcher.register_message_handler(list_status_orders_handler, lambda message: message.text in ORDER_TYPES_LIST,
                                        state=ManageOrderState.managment)
    dispatcher.register_callback_query_handler(details_orders_callback, lambda call: call.data in all_order_list_id(),
                                               state=ManageOrderState.managment)
    dispatcher.register_callback_query_handler(managment_order_callback,
                                               lambda call: call.data in all_order_status_change(),
                                               state=ManageOrderState.managment)
    dispatcher.register_callback_query_handler(send_to_trello_callback,
                                               lambda call: call.data in order_send_trello_list(),
                                               state=ManageOrderState.managment)
    dispatcher.register_callback_query_handler(refinement_callback,
                                               lambda call: call.data in order_refinement_list(),
                                               state=ManageOrderState.managment)
    dispatcher.register_message_handler(refinement_comment, state=ManageOrderState.refinement)


async def choice_orders_type(message: types.Message):
    current_user = MyRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            await ManageOrderState.type.set()
            await message.answer(CHOICE_TYPE_OF_ORDERS, reply_markup=type_of_orders_admin())
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


# category of orders (REVIEW_ORDERS, ACTIVE_ORDERS, COMPLETED_ORDERS, CANCELED_ORDERS)
async def status_handler(message: types.Message, state: FSMContext):
    if message.text == ACCOUNTS:
        await state.update_data(type=ACCOUNT_TYPE)

        await ManageOrderState.next()
        await message.answer(STATUS_OF_ORDERS, reply_markup=admin_orders_keyboard())

    elif message.text == DESIGN:
        await state.update_data(type=CREO_TYPE)

        await ManageOrderState.next()
        await message.answer(STATUS_OF_ORDERS, reply_markup=admin_orders_keyboard())

    else:
        await message.answer(NOT_IMPLEMENTED)


# Output orders from database
async def list_status_orders_handler(message: types.Message, state: FSMContext):
    # show all order with status: review -------------------------------------------------
    type_account = await state.get_data()
    if message.text == REVIEW_ORDERS:
        orders = MyRepository().get_orders(REVIEW, type_account=(type_account['type'], ))
        if len(orders) > 0:
            await message.answer(REVIEW_ORDERS, reply_markup=inline_orders_keyboard(orders, type_account['type']))
        else:
            await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

    # show all order with status: active -------------------------------------------------
    elif message.text == ACTIVE_ORDERS:
        orders = MyRepository().get_orders(ACTIVE, type_account=(type_account['type'], ))
        if len(orders) > 0:
            await message.answer(ACTIVE_ORDERS, reply_markup=inline_orders_keyboard(orders, type_account['type']))
        else:
            await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

    # show all order with status: on_approve -------------------------------------------------
    elif message.text == ON_APPROVE_ORDERS:
        orders = MyRepository().get_orders(ON_APPROVE, type_account=(type_account['type'],))
        if len(orders) > 0:
            await message.answer(ON_APPROVE_ORDERS, reply_markup=inline_orders_keyboard(orders, type_account['type']))
        else:
            await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

    # show all order with status: completed -------------------------------------------------
    elif message.text == COMPLETED_ORDERS:
        orders = MyRepository().get_orders(COMPLETED, type_account=(type_account['type'], ))
        if len(orders) > 0:
            await message.answer(COMPLETED_ORDERS, reply_markup=inline_orders_keyboard(orders, type_account['type']))
        else:
            await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

    # show all order with status: cancel -------------------------------------------------
    elif message.text == CANCELED_ORDERS:
        orders = MyRepository().get_orders(CANCELED, type_account=(type_account['type'], ))
        if len(orders) > 0:
            await message.answer(CANCELED_ORDERS, reply_markup=inline_orders_keyboard(orders, type_account['type']))
        else:
            await message.answer(ORDERS_IS_EMPTY, reply_markup=admin_orders_keyboard())

    # not implemented -------------------------------------------------
    else:
        await message.answer(NOT_IMPLEMENTED)


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
        if current_user['position'] == ADMIN and current_user['sub_position'] != SUB_POSITION_ACCOUNT:
            order_id = callback.data.split("_")[1]
            task = MyRepository().get_order(order_id)
            task_creo = MyRepository().get_creo(order_id)
            client = MyRepository().get_user(task['id_user'])

            if task['status'] == REVIEW:

                result = MyTrelloManager().generate_task(parse_to_trello_card_format(task_creo, client))

                if result is not None:
                    MyRepository().exchange_status_order(order_id, ACTIVE)  # change status to active
                    MyRepository().update_creo_order_trello(result['id'], result['url'], order_id)  # add trello data to database
                    MyTrelloManager().set_status_field(result['id'])  # set status in trello
                    await callback.message.answer(TASK_SUCCESFUL_SEND)

                    result_webhook = MyTrelloManager().set_webhook_card(result['id'])
                    print(result_webhook.json())
                else:
                    await callback.message.answer(TASK_FAIL_SEND)

        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def refinement_callback(callback: types.CallbackQuery, state: FSMContext):
    current_user = MyRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN and current_user['sub_position'] != SUB_POSITION_ACCOUNT:
            order_id = callback.data.split("_")[1]

            await ManageOrderState.next()
            await state.update_data(refinement=order_id)
            await callback.message.answer(COMMENT_TO_REFINEMENT, reply_markup=cancel_keyboard())

        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def refinement_comment(message: types.Message, state: FSMContext):
    order_id = await state.get_data()
    task = MyRepository().get_order(order_id['refinement'])
    task_creo = MyRepository().get_creo(order_id['refinement'])

    if task['status'] == ON_APPROVE:
        result_status = MyTrelloManager().set_status_field(task_creo['trello_id'], ACTIVE_STATUS_TRELLO)
        result_comment = MyTrelloManager().write_comment_card(task_creo['trello_id'], message.text)
        if result_status is not None and result_comment is not None:
            MyRepository().exchange_status_order(order_id['refinement'], ACTIVE)  # change status to active
            await message.answer(REFINEMENT_SUCCESFULY_SEND, reply_markup=admin_orders_keyboard())
        else:
            await message.answer(STATUS_NOT_EXCHANGE, reply_markup=admin_orders_keyboard())

    await ManageOrderState.managment.set()
