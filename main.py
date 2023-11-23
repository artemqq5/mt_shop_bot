import logging
from config.cfg import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardRemove
from aiogram.utils import executor

from data.repository import MyRepository
from handlers.design.creo_handlers import *
from handlers.design.creo_video import register_creo_video_handlers
from keyboard.base_keyboard import main_keyboard, buy_keyboard

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=storage)


# start handler
@dispatcher.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    if MyRepository().get_user(telegram_id=message.chat.id) is None:
        MyRepository().add_user(telegram_id=message.chat.id, name=message.chat.username)

    await message.answer(HELLO_MESSAGE, reply_markup=main_keyboard())


# cancel states
@dispatcher.message_handler(lambda m: m.text == CANCEL, state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.reset_state()
    await message.reply(CANCEL_OK, reply_markup=main_keyboard())


# menu handler
@dispatcher.message_handler(lambda message: message.text in (BUY, RULES, SUPPORT, ABOUT))
async def main_handler_message(message: types.Message):
    if MyRepository().get_user(telegram_id=message.chat.id) is not None:
        if message.text == BUY:
            await message.answer(CATEGORIES, reply_markup=buy_keyboard())
        elif message.text == RULES:
            await message.answer(text=NOT_IMPLEMENTED)
        elif message.text == SUPPORT:
            await message.answer(text=NOT_IMPLEMENTED)
        elif message.text == ABOUT:
            await message.answer(text=NOT_IMPLEMENTED)
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


# design handler
register_handlers_creo(dispatcher)  # base handlers
register_creo_video_handlers(dispatcher)  # for video adaptive\new


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
