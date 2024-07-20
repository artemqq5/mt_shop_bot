from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from data.default_constants import ADMIN
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.handlers.admin.ban import ban_system_main
from domain.handlers.admin.management import choice_category_main
from domain.handlers.admin.messaging import messaging_main
from domain.handlers.admin.orders import orders_list_main
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from presentation.keyboards.admin.kb_menu import kb_menu_admin

router = Router()

router.include_routers(
    choice_category_main.router,
    messaging_main.router,
    ban_system_main.router,
    orders_list_main.router
)

router.message.middleware(IsRoleMiddleware(ADMIN))
router.callback_query.middleware(IsRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_admin)

