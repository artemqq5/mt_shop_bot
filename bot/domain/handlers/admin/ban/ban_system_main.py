from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from bot.domain.handlers.admin.ban import ban, ban_list, unban
from bot.domain.states.admin.bun.BanSystemState import BanSystemState
from bot.presentation.keyboards.admin.ban.kb_ban_system import (
    BanSystemBack,
    kb_ban_menu,
)

router = Router()

router.include_routers(ban.router, unban.router, ban_list.router)


@router.callback_query(BanSystemBack.filter())
async def ban_manu_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BanSystemState.ChoiceOperation)
    await callback.message.edit_text(i18n.ADMIN.BAN_SYSTEM(), reply_markup=kb_ban_menu)
