from aiogram import types
from aiogram.dispatcher import FSMContext


def register_creo_video_handlers(dispatcher):
    dispatcher.register_message_handler(callback=start_order_creo)


async def start_order_creo(message: types.Message, state: FSMContext):
    pass
