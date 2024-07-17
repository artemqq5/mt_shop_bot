from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from domain.states.client.buy.BuyItemState import BuyItemState
from presentation.keyboards.client.buy.kb_buy_category import kb_buy_category_choice

router = Router()


@router.message(F.text == L.CLENT.BUY())
async def buy_item_menu(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(BuyItemState.Category)

    categories = CategoryRepository().categories()
    await message.answer(i18n.CLIENT.BUY_CHOICE_CATEGORY(), reply_markup=kb_buy_category_choice(categories))
