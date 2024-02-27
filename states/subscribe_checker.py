from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.cfg import CHANNEL_ID, CHANNEL_URL

YOU_ARE_NOT_SUBSCRIBE = (
    "Подпишись на канал, чтобы иметь доступ ко всем нужным расходникам для залива и иметь возможность использовать "
    "этот бот.\n\n"
    "<b>При подписке на канал вы получаете промокод 10% на первый заказ в боте!</b>\n\n"
    "После подписки напиши /start чтобы проверить статус")


async def is_user_subscribed(user_id, bot) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        # The status can be 'member', 'administrator', 'creator' or 'left'/'kicked'
        if member.status not in ['left', 'kicked']:
            return True
    except Exception as e:
        print(f"error is_user_subscribed (An error occurred): {e}")
    return False


def keyboard_subsribe() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    channel_button = InlineKeyboardButton(text="Shop Masons", url=CHANNEL_URL)
    keyboard.add(channel_button)
    return keyboard
