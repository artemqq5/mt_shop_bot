from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repository.users import UserRepository
from domain.states.admin.bun.BanSystemState import BanSystemState
from presentation.keyboards.admin.ban.kb_ban_system import kb_ban_system_back, UnBanUserCallback
from presentation.keyboards.admin.ban.kb_unban import kb_unban_user_next, UnBanOneMoreCallback

router = Router()


@router.callback_query(UnBanUserCallback.filter(), BanSystemState.ChoiceOperation)
async def unban_user_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BanSystemState.UnBanUserID)
    await callback.message.edit_text(i18n.ADMIN.UNBAN_USER_ID(), reply_markup=kb_ban_system_back)


@router.message(BanSystemState.UnBanUserID)
async def unbun_user(message: Message, state: FSMContext, i18n: I18nContext):
    if message.text.startswith("@"):
        username = message.text.split("@")[1]
        result = UserRepository().update_ban_by_username(username, False)
    else:
        result = UserRepository().update_ban_by_id(message.text, False)

    if not result:
        await message.answer(i18n.ADMIN.UNBAN_ERROR(), reply_markup=kb_unban_user_next)
        return

    await message.answer(i18n.ADMIN.UNBAN_SUCCESS(), reply_markup=kb_unban_user_next)


@router.callback_query(UnBanOneMoreCallback.filter(), BanSystemState.UnBanUserID)
async def unban_user_next_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await unban_user_callback(callback, state, i18n)
