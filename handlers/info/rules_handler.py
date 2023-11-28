from aiogram import types

from data.constants.base_constants import RULES
from data.constants.info_constants import CONTACTS_OUR_SUPPORTS, RULES_TEXT
from keyboard.info.support_keyboard import support_contacts_keyboard


def register_rules_handlers(dispatcher):
    dispatcher.register_message_handler(rules_handler, lambda message: message.text == RULES)


async def rules_handler(message: types.Message):
    await message.answer(RULES_TEXT)
