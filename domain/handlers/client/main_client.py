from aiogram import Router, Bot, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BusinessConnection
from aiogram_i18n import I18nContext

from data.default_constants import CLIENT
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.handlers.client.buy import buy_main
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from presentation.keyboards.client._default import kb_subsribe, kb_menu_client

router = Router()

router.include_routers(
    buy_main.router
)

router.message.middleware(IsRoleMiddleware(CLIENT))


@router.message(Command("start"), IsAdminFilter(False))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_client)


# @router.business_message(Command("start"), IsAdminFilter(False))
# async def start(message: Message, state: FSMContext, i18n: I18nContext):
#     await message.answer(text=i18n.MENU())
