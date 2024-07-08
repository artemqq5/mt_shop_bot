from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from data.constants.default_constants import ADMIN, CLIENT
from domain.middlewares.IsUserAdmin import IsUserAdmin

router = Router()

router.message.middleware(IsUserAdmin(CLIENT))


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Client")
