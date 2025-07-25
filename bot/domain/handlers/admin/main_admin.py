from aiogram import Bot, F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from bot.data.default_constants import ADMIN
from bot.data.repository.categories import CategoryRepository
from bot.data.repository.orders import OrderRepository
from bot.domain.filters.IsAdminFilter import IsAdminFilter
from bot.domain.handlers.admin.ban import ban_system_main
from bot.domain.handlers.admin.management import choice_category_main
from bot.domain.handlers.admin.messaging import messaging_main
from bot.domain.handlers.admin.orders import orders_list_main
from bot.domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from bot.domain.states.admin.bun.BanSystemState import BanSystemState
from bot.domain.states.admin.management.ManageCategoryState import (
    ManagementCategoryState,
)
from bot.domain.states.admin.messaging.MessagingState import MessagingState
from bot.domain.states.admin.orders.ListOrdersState import ListOrdersState
from bot.presentation.keyboards.admin.ban.kb_ban_system import kb_ban_menu
from bot.presentation.keyboards.admin.kb_menu import kb_menu_admin
from bot.presentation.keyboards.admin.management.category.kb_managment import (
    kb_choice_category,
)
from bot.presentation.keyboards.admin.messaging.kb_messaging import (
    kb_messaging_categories,
)
from bot.presentation.keyboards.admin.orders.kb_orders_list import kb_orders_choice

router = Router()

router.include_routers(
    choice_category_main.router, messaging_main.router, ban_system_main.router, orders_list_main.router
)

router.message.middleware(IsRoleMiddleware(ADMIN))
router.callback_query.middleware(IsRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_admin)


@router.message(F.text == L.ADMIN.BAN())
async def ban_menu(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(BanSystemState.ChoiceOperation)
    await message.answer(i18n.ADMIN.BAN_SYSTEM(), reply_markup=kb_ban_menu)


@router.message(F.text == L.ADMIN.MANAGEMENT())
async def manage(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(ManagementCategoryState.SetCategory)

    categories = CategoryRepository().categories_all()
    await message.answer(i18n.ADMIN.CHOICE_CATEGORY(), reply_markup=kb_choice_category(categories, 1))


@router.message(F.text == L.ADMIN.MESSAGING())
async def messaging(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.ADMIN.CHOICE_TYPE_MESSAGE(), reply_markup=kb_messaging_categories)
    await state.set_state(MessagingState.MessagingType)


@router.message(F.text == L.ADMIN.ORDERS())
async def order_list_main(message: types.Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    await state.clear()
    await state.set_state(ListOrdersState.ListOrders)

    orders = OrderRepository().orders()
    await message.answer(i18n.ADMIN.ORDERS_HISTORY(), reply_markup=kb_orders_choice(orders))
