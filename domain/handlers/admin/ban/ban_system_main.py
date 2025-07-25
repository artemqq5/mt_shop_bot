from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext
from aiogram_i18n import L

from domain.handlers.admin.ban import ban, unban, ban_list
from domain.states.admin.bun.BanSystemState import BanSystemState
from presentation.keyboards.admin.ban.kb_ban_system import kb_ban_menu, BanSystemBack

router = Router()

router.include_routers(
    ban.router,
    unban.router,
    ban_list.router
)


@router.callback_query(BanSystemBack.filter())
async def ban_manu_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BanSystemState.ChoiceOperation)
    await callback.message.edit_text(i18n.ADMIN.BAN_SYSTEM(), reply_markup=kb_ban_menu)
