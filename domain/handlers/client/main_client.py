from aiogram import Router, Bot, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BusinessConnection
from aiogram_i18n import I18nContext, L

from data.default_constants import CLIENT
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.handlers.client.availability import main_availability
from domain.handlers.client.buy import choice_item
from domain.handlers.client.buy import choice_category_main
from domain.handlers.client.profile import profile_main
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from presentation.keyboards.client._default import kb_subsribe, kb_menu_client, kb_support

router = Router()

router.include_routers(
    choice_category_main.router,
    main_availability.router,
    profile_main.router
)

router.message.middleware(IsRoleMiddleware(CLIENT))


@router.message(Command("start"), IsAdminFilter(False))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_client)


@router.message(F.text == L.CLIENT.SUPPORT())
async def support(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.CLIENT.CONNECTION_WITH_SUPPORT(), reply_markup=kb_support)


# @router.business_message(Command("start"), IsAdminFilter(False))
# async def start(message: Message, state: FSMContext, i18n: I18nContext):
#     await message.answer(text=i18n.MENU())
