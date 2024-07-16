from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.users import UserRepository
from domain.states.bun.BanSystemState import BanSystemState
from presentation.keyboards.admin.ban.kb_ban_list import kb_ban_list_nav, text_ban_list, BanListNavigation
from presentation.keyboards.admin.ban.kb_ban_system import ListBannedUsersCallback

router = Router()


@router.callback_query(ListBannedUsersCallback.filter(), BanSystemState.ChoiceOperation)
async def ban_list_user_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BanSystemState.BanListUser)
    ban_users = UserRepository().banned_users()

    await callback.message.edit_text(
        text_ban_list(ban_users, i18n),
        reply_markup=kb_ban_list_nav(ban_users)
    )


@router.callback_query(BanListNavigation.filter(), BanSystemState.BanListUser)
async def ban_list_navigation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    ban_users = UserRepository().banned_users()

    await callback.message.edit_text(
        text_ban_list(ban_users, i18n, int(page)),
        reply_markup=kb_ban_list_nav(ban_users, int(page))
    )
