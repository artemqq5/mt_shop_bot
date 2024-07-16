from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repository.users import UserRepository
from domain.states.bun.BanSystemState import BanSystemState
from presentation.keyboards.admin.ban.kb_ban import kb_ban_user_next, BanOneMoreCallback
from presentation.keyboards.admin.ban.kb_ban_system import BanUserCallback, kb_ban_system_back
router = Router()


@router.callback_query(BanUserCallback.filter(), BanSystemState.ChoiceOperation)
async def ban_user_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BanSystemState.BanUserID)
    await callback.message.edit_text(i18n.ADMIN.BAN_USER_ID(), reply_markup=kb_ban_system_back)


@router.message(BanSystemState.BanUserID)
async def bun_user(message: Message, state: FSMContext, i18n: I18nContext):
    if message.text.startswith("@"):
        username = message.text.split("@")[1]
        print(username)
        result = UserRepository().update_ban_by_username(username, True)
    else:
        result = UserRepository().update_ban_by_id(message.text, True)

    if not result:
        await message.answer(i18n.ADMIN.BAN_ERROR(), reply_markup=kb_ban_user_next)
        return

    await message.answer(i18n.ADMIN.BAN_SUCCESS(), reply_markup=kb_ban_user_next)


@router.callback_query(BanOneMoreCallback.filter(), BanSystemState.BanUserID)
async def ban_user_next_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await ban_user_callback(callback, state, i18n)
