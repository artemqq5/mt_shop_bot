from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

router = Router()


@router.message(F.text == L.ADMIN.ORDERS)
async def order_list_main(message: types.Message, state: FSMContext, i18n: I18nContext):
    # orders =
    pass