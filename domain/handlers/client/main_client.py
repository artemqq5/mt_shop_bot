from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from data.default_constants import CLIENT
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware

router = Router()

router.message.middleware(IsRoleMiddleware(CLIENT))


@router.message(Command("start"), IsAdminFilter(False))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await message.answer(text=i18n.MENU())
