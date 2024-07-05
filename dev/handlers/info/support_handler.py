from aiogram import types

from data.constants.base_constants import SUPPORT
from data.constants.info_constants import CONTACTS_OUR_SUPPORTS
from dev.keyboard.info.support_keyboard import support_contacts_keyboard


def register_support_handlers(dispatcher):
    dispatcher.register_message_handler(support_handler, lambda message: message.text == SUPPORT)


async def support_handler(message: types.Message):
    await message.answer(CONTACTS_OUR_SUPPORTS, reply_markup=support_contacts_keyboard())

