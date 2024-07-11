from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from data.default_constants import ADMIN
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.handlers.admin.items import management
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from presentation.keyboards.admin.kb_menu import kb_menu_admin

router = Router()

router.include_routers(
    management.router,
)

router.message.middleware(IsRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_admin)

