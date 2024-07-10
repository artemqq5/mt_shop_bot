from dev.constants.admin_constants import CARD_TYPE, CABINET_TYPE, VERIFICATION_TYPE
from dev.constants.base_constants import TASK_SEND, TASK_SEND_ERROR
from dev.constants.orders import OrdersRepository
from notify.notify_push_task import notify_new_task
from keyboard.menu.menu_keyboard import main_keyboard


async def send_order_account(data, message):
    if data is not None:
        try:
            result = OrdersRepository().add_account_order(
                id_user=message.chat.id,
                name=data['account']['name'],
                desc=data['account']['desc'],
                desc_from_user=data.get('desc', None),
                type_account=data['account']['type'],
                geo=data['account']['geo'],
                count=data['count'],
                price=data['account']['price'],
            )

        except Exception as e:
            print(f"send_order_account: {e}")
            result = None

        if result is not None:
            await message.answer(TASK_SEND, reply_markup=main_keyboard(message))
            await notify_new_task(message, data['account']['type'], result)
        else:
            await message.answer(TASK_SEND_ERROR, reply_markup=main_keyboard(message))


async def send_order_card(data, message):
    if data is not None:
        try:
            result = OrdersRepository().add_account_order(
                id_user=message.chat.id,
                name=data['account']['name'],
                desc=data['account']['desc'],
                desc_from_user=data.get('desc', None),
                type_account=CARD_TYPE,
                geo=None,
                count=data['count'],
                price=data['account']['price'],
            )

        except Exception as e:
            print(f"send_order_card: {e}")
            result = None

        if result is not None:
            await message.answer(TASK_SEND, reply_markup=main_keyboard(message))
            await notify_new_task(message, CARD_TYPE, result)
        else:
            await message.answer(TASK_SEND_ERROR, reply_markup=main_keyboard(message))


async def send_order_cabinet(data, message):
    if data is not None:
        try:
            result = OrdersRepository().add_account_order(
                id_user=message.chat.id,
                name=data['account']['name'],
                desc=data['account']['desc'],
                desc_from_user=data.get('desc', None),
                type_account=CABINET_TYPE,
                geo=None,
                count=data['count'],
                price=data['account']['price'],
            )

        except Exception as e:
            print(f"send_order_cabinet: {e}")
            result = None

        if result is not None:
            await message.answer(TASK_SEND, reply_markup=main_keyboard(message))
            await notify_new_task(message, CABINET_TYPE, result)
        else:
            await message.answer(TASK_SEND_ERROR, reply_markup=main_keyboard(message))


async def send_order_verification(data, message):
    if data is not None:
        try:
            result = OrdersRepository().add_account_order(
                id_user=message.chat.id,
                name=data['account']['name'],
                desc=data['account']['desc'],
                desc_from_user=data.get('desc', None),
                type_account=VERIFICATION_TYPE,
                geo=data['account']['geo'],
                count=data['count'],
                price=data['account']['price'],
            )

        except Exception as e:
            print(f"send_order_verification: {e}")
            result = None

        if result is not None:
            await message.answer(TASK_SEND, reply_markup=main_keyboard(message))
            await notify_new_task(message, VERIFICATION_TYPE, result)
        else:
            await message.answer(TASK_SEND_ERROR, reply_markup=main_keyboard(message))

