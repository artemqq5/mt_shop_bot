from aiogram import types

from dev.constants.base_constants import RULES
from dev.constants.info_constants import RULES_TEXT


def register_rules_handlers(dispatcher):
    dispatcher.register_message_handler(rules_handler, lambda message: message.text == RULES)


async def rules_handler(message: types.Message):
    await message.answer(RULES_TEXT)
