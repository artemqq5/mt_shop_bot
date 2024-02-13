import datetime
import logging

from config.cfg import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardRemove
from aiogram.utils import executor

from data.repository.users import UsersRepository
from handlers.admin.admin_push_notify import register_push_handlers
from handlers.buy.accounts.account_base_handler import register_accounts_handlers
from handlers.admin.add_items.admin_add_items import register_add_item_handlers
from handlers.admin.admin_orders_handler import register_orders_handler
from handlers.admin.admin_show_items import register_show_item_handlers
from handlers.buy.agency_accounts.agency_base_handler import register_agency_handlers
from handlers.buy.apps.apps_base_handler import register_hundler_apps
from handlers.buy.cabinets.cabinet_base_handler import register_order_cabinets_handlers
from handlers.buy.cards.cards_base_handler import register_order_cards_handlers
from handlers.buy.creo.app_handler import register_creo_app_handlers
from handlers.buy.creo.creo_base_handler import *
from handlers.buy.creo.default_handler import register_creo_default_handlers
from handlers.buy.creo.other_handler import register_creo_other_handlers
from handlers.buy.verifications.verification_base_handler import register_order_verifications_handlers
from handlers.info.about_us_handler import register_about_us_handlers
from handlers.my_orders.my_orders_handler import register_my_order_handlers
from keyboard.info.support_keyboard import support_contacts_keyboard
from keyboard.menu.menu_keyboard import main_keyboard, buy_keyboard, about_keyboard
from keyboard.my_orders.my_orders_keyboard import user_view_choice_keyboard
from states.user_orders.user_orders_state import UserOrdersState

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=storage)


# start handler
@dispatcher.message_handler(commands=['start'], state='*')
async def start_cmd(message: types.Message, state: FSMContext):
    # cancel state if not None
    current_state = await state.get_state()
    if current_state is not None:
        await state.reset_state()
    # ===========================

    if UsersRepository().get_user(telegram_id=message.chat.id) is None:
        UsersRepository().add_user(
            telegram_id=message.chat.id,
            name=message.chat.username,
            time=datetime.datetime.now()
        )

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
    if current_state is not None:
        await state.reset_state()

    await message.reply(CANCEL_OK, reply_markup=main_keyboard(message))


# menu
@dispatcher.message_handler(lambda m: m.text == MENU)
async def menu_handler(message: types.Message):
    await message.reply(MENU, reply_markup=main_keyboard(message))


# menu handler
@dispatcher.message_handler(lambda message: message.text in (BUY, RULES, SUPPORT, ABOUT, MY_ORDERS))
async def main_handler(message: types.Message):
    current_user = UsersRepository().get_user(telegram_id=message.chat.id)
    if current_user is not None:
        if current_user['position'] == CLIENT:
            if message.text == BUY:
                await message.answer(CATEGORIES, reply_markup=buy_keyboard())
            elif message.text == RULES:
                await message.answer(RULES_TEXT)
            elif message.text == SUPPORT:
                await message.answer(CONTACTS_OUR_SUPPORTS, reply_markup=support_contacts_keyboard())
            elif message.text == ABOUT:
                await message.answer(text=WHAT_INTERESTED, reply_markup=about_keyboard())
            elif message.text == MY_ORDERS:
                await UserOrdersState.view.set()
                await message.answer(text=TYPE_OF_ORDER_VIEW, reply_markup=user_view_choice_keyboard())
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


# my orders
register_my_order_handlers(dispatcher)

# push
register_push_handlers(dispatcher)

# agency accounts
register_agency_handlers(dispatcher)

# apps handler
register_hundler_apps(dispatcher)

# accounts, cards, cabinets, verifications handler
register_accounts_handlers(dispatcher)
register_order_cards_handlers(dispatcher)
register_order_cabinets_handlers(dispatcher)
register_order_verifications_handlers(dispatcher)

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
