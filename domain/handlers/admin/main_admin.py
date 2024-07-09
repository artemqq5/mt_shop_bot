from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from data.constants.default_constants import ADMIN
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware

router = Router()

router.message.middleware(IsRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: Message, state: FSMContext):
    await message.answer("Admin")
