from datetime import datetime

from aiogram import Router, Bot, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BusinessConnection
from aiogram_i18n import I18nContext, L

from data.default_constants import CLIENT
from data.repository.categories import CategoryRepository
from data.repository.orders import OrderRepository
from data.repository.users import UserRepository
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.handlers.client.availability import main_availability
from domain.handlers.client.buy import choice_item
from domain.handlers.client.buy import choice_category_main
from domain.handlers.client.profile import profile_main, balance
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from domain.states.client.availability.AvailabilityState import AvailabilityState
from domain.states.client.buy.BuyItemState import BuyItemState
from domain.states.client.profile.ProfileState import ProfileState
from presentation.keyboards.client._default import kb_subsribe, kb_menu_client, kb_support
from presentation.keyboards.client.availability.kb_avaibility import text_availability_list, kb_availability
from presentation.keyboards.client.buy.kb_buy_category import kb_buy_category_choice
from presentation.keyboards.client.profile.kb_profile import kb_profile

router = Router()

router.include_routers(
    choice_category_main.router,
    main_availability.router,
    profile_main.router,
    balance.router
)

router.message.middleware(IsRoleMiddleware(CLIENT))
router.callback_query.middleware(IsRoleMiddleware(CLIENT))


@router.message(Command("start"), IsAdminFilter(False))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_client)


@router.message(F.text == L.CLIENT.SUPPORT())
async def support(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.CLIENT.CONNECTION_WITH_SUPPORT(), reply_markup=kb_support)


@router.message(F.text == L.CLIENT.PROFILE())
async def profile_menu(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(ProfileState.ProfileView)

    user = UserRepository().user(message.from_user.id)

    date_format = '%Y-%m-%d %H:%M:%S'
    start_date = datetime.strptime(str(user['join_at']), date_format)
    days_passed = (datetime.now() - start_date).days

    order_count = len(OrderRepository().orders_by_user_id(user['user_id']))

    await message.answer(
        i18n.CLIENT.PROFILE.MAIN_PAGE(
            balance=user['balance'],
            telegram_id=user['user_id'],
            order_count=order_count,
            lang=user.get('lang', "-"),
            date=user['join_at'],
            days=days_passed

        ), reply_markup=kb_profile
    )


@router.message(F.text == L.CLIENT.BUY())
async def buy_item_menu(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(BuyItemState.Category)

    categories = CategoryRepository().categories()
    await message.answer(i18n.CLIENT.BUY.CHOICE_CATEGORY(), reply_markup=kb_buy_category_choice(categories))


@router.message(F.text == L.CLIENT.AVAILABILITY())
async def availability_menu(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(AvailabilityState.Aviability)

    categories = CategoryRepository().categories()
    await message.answer(text_availability_list(categories, i18n), reply_markup=kb_availability(categories))


# @router.business_message(Command("start"), IsAdminFilter(False))
# async def start(message: Message, state: FSMContext, i18n: I18nContext):
#     await message.answer(text=i18n.MENU())
