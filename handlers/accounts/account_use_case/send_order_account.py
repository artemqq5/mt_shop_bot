from data.constants.admin_constants import ACCOUNT_TYPE
from data.constants.base_constants import TASK_SEND, TASK_SEND_ERROR
from data.repository import MyRepository
from handlers.notify.notify_push_task import notify_new_task
from keyboard.menu.menu_keyboard import main_keyboard


async def send_order_account(data, message):
    if data is not None:
        try:
            result = MyRepository().add_order_account(
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

        if result:
            await message.answer(TASK_SEND, reply_markup=main_keyboard(message))
            await notify_new_task(message, ACCOUNT_TYPE)
        else:
            await message.answer(TASK_SEND_ERROR, reply_markup=main_keyboard(message))
