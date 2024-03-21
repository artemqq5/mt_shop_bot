from aiogram.types import ReplyKeyboardRemove

from data.repository.users import UsersRepository


async def is_banned(message):
    current_user = UsersRepository().get_user(telegram_id=message.chat.id)

    if current_user and current_user['banned']:
        await message.answer(current_user['banned_message'], reply_markup=ReplyKeyboardRemove())
        return True
