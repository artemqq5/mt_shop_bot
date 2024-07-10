from dev.constants.admin_constants import CREO_TYPE
from dev.constants.base_constants import TASK_SEND, TASK_SEND_ERROR
from dev.constants.design_constants import FAQ_CREO_DESC
from dev.constants.creos import CreosRepository
from notify.notify_push_task import notify_new_task
from keyboard.menu.menu_keyboard import main_keyboard


async def send_order_creo(data, message):
    if data is not None:
        try:
            result = CreosRepository().add_creo(
                format_creo=data['general']['format'],
                type_creo=data['general']['type'],
                category=data['general']['category'],
                description=data['description'],
                id_user=message.chat.id,
                geo=data.get('geo', None),
                language=data.get('language', None),
                currency=data.get('currency', None),
                format_res=data.get('format', None),
                offer=data.get('offer', None),
                voice=data.get('voice', None),
                source=data.get('source', None),
                deadline=data.get('deadline', None),
                count=data['count'],
                sub_desc=data.get('sub_description', None)
            )
        except Exception as e:
            print(f"send_order_creo: {e}")
            result = None

        if result is not None:
            await message.answer(f"{TASK_SEND}\n\n{FAQ_CREO_DESC}", reply_markup=main_keyboard(message))
            await notify_new_task(message, CREO_TYPE, result)
        else:
            await message.answer(TASK_SEND_ERROR, reply_markup=main_keyboard(message))
