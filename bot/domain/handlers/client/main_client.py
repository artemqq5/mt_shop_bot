from datetime import datetime

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from bot.data.default_constants import CLIENT
from bot.data.repository.categories import CategoryRepository
from bot.data.repository.orders import OrderRepository
from bot.data.repository.users import UserRepository
from bot.domain.filters.IsAdminFilter import IsAdminFilter
from bot.domain.handlers.client.availability import main_availability
from bot.domain.handlers.client.buy import choice_category_main
from bot.domain.handlers.client.profile import balance, profile_main
from bot.domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from bot.domain.states.client.availability.AvailabilityState import AvailabilityState
from bot.domain.states.client.buy.BuyItemState import BuyItemState
from bot.domain.states.client.profile.ProfileState import ProfileState
from bot.presentation.keyboards.client._default import kb_menu_client, kb_support
from bot.presentation.keyboards.client.availability.kb_avaibility import (
    kb_availability,
    text_availability_list,
)
from bot.presentation.keyboards.client.buy.kb_buy_category import kb_buy_category_choice
from bot.presentation.keyboards.client.profile.kb_profile import kb_profile

router = Router()

router.include_routers(choice_category_main.router, main_availability.router, profile_main.router, balance.router)

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

    date_format = "%Y-%m-%d %H:%M:%S"
    start_date = datetime.strptime(str(user["join_at"]), date_format)
    days_passed = (datetime.now() - start_date).days

    order_count = len(OrderRepository().orders_by_user_id(user["user_id"]))

    await message.answer(
        i18n.CLIENT.PROFILE.MAIN_PAGE(
            balance=user["balance"],
            telegram_id=user["user_id"],
            order_count=order_count,
            lang=user.get("lang", "-"),
            date=user["join_at"],
            days=days_passed,
        ),
        reply_markup=kb_profile,
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
