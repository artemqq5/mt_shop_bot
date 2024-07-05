from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject, ReplyKeyboardRemove

from data.repository.users import UserRepository
from domain.notification.NotificationAdmin import NotificationAdmin
from presentation.keyboards.user._default import keyboard_subsribe
from private_cfg import CHANNEL_ID


class UserRegistrationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        tg_user = event.from_user
        current_user = UserRepository().user(tg_user.id)

        if not current_user:
            if not UserRepository().add(tg_user.id, tg_user.username, tg_user.language_code):
                await event.bot.send_message(chat_id=tg_user.id, text=data['i18n'].REGISTER_FAIL())
                return None

            current_user = UserRepository().user(tg_user.id)

            # notify admin about registration
            await NotificationAdmin().user_activate_bot(tg_user.id, event.bot, data['i18n'])

        if current_user['banned']:
            await event.bot.send_message(chat_id=tg_user.id, text=data['i18n'].BAN_MESSAGE(), reply_markup=ReplyKeyboardRemove())
            return None

        if not await is_user_subscribed(tg_user.id, event.bot):
            await event.bot.send_message(chat_id=tg_user.id, text=data['i18n'].SUBSCRIBE_CHANNEL(), reply_markup=keyboard_subsribe)

        return await handler(event, data)


async def is_user_subscribed(user_id, bot) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        # The status can be 'member', 'administrator', 'creator' or 'left'/'kicked'
        if member.status not in ['left', 'kicked']:
            return True
    except Exception as e:
        print(f"error is_user_subscribed (An error occurred): {e}")
    return False



