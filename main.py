import logging
from config.cfg import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardRemove
from aiogram.utils import executor

from data.repository import MyRepository
from handlers.accounts.account_base_handler import register_accounts_handlers
from handlers.admin.admin_add_items import register_add_item_handlers
from handlers.admin.admin_orders_handler import register_orders_handler
from handlers.admin.admin_show_items import register_show_item_handlers
from handlers.creo.app_handler import register_creo_app_handlers
from handlers.creo.creo_base_handler import *
from handlers.creo.default_handler import register_creo_default_handlers
from handlers.creo.other_handler import register_creo_other_handlers
from handlers.info.about_us_handler import register_about_us_handlers
from handlers.info.rules_handler import register_rules_handlers
from handlers.info.support_handler import register_support_handlers
from keyboard.info.support_keyboard import support_contacts_keyboard
from keyboard.menu.menu_keyboard import main_keyboard, buy_keyboard, about_keyboard

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=storage)


# start handler
@dispatcher.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    if MyRepository().get_user(telegram_id=message.chat.id) is None:
        MyRepository().add_user(telegram_id=message.chat.id, name=message.chat.username)

    with open("source/bot_video_start.gif.mp4", 'rb') as video_file:
        await message.answer_animation(
            video_file,
            caption=HELLO_MESSAGE,
            reply_markup=main_keyboard(message)
        )


# cancel states
@dispatcher.message_handler(lambda m: m.text == CANCEL, state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        print("null")
        return
    await state.reset_state()

    await message.reply(CANCEL_OK, reply_markup=main_keyboard(message))


# menu
@dispatcher.message_handler(lambda m: m.text == MENU)
async def menu_handler(message: types.Message):
    await message.reply(MENU, reply_markup=main_keyboard(message))


# menu handler
@dispatcher.message_handler(lambda message: message.text in (BUY, RULES, SUPPORT, ABOUT))
async def main_handler(message: types.Message):
    if MyRepository().get_user(telegram_id=message.chat.id) is not None:
        if message.text == BUY:
            await message.answer(CATEGORIES, reply_markup=buy_keyboard())
        elif message.text == RULES:
            await message.answer(RULES_TEXT)
        elif message.text == SUPPORT:
            await message.answer(CONTACTS_OUR_SUPPORTS, reply_markup=support_contacts_keyboard())  # have sub handler
        elif message.text == ABOUT:
            await message.answer(text=WHAT_INTERESTED, reply_markup=about_keyboard())
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


# accounts handler
register_accounts_handlers(dispatcher)

# creo handler
register_handlers_creo(dispatcher)  # base handlers
register_creo_default_handlers(dispatcher)  # for all creo category besides (APP Design, Other (Custom creo))
register_creo_other_handlers(dispatcher)  # for Other (Custom creo)
register_creo_app_handlers(dispatcher)  # for App Design creo

# info handler
register_about_us_handlers(dispatcher)
# register_support_handlers(dispatcher) the same realization as main SUPPORT
# register_rules_handlers(dispatcher) the same realization as main RULES

# admin handler
register_orders_handler(dispatcher)
register_add_item_handlers(dispatcher)
register_show_item_handlers(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
