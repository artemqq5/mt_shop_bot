from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from data.repository.items import ItemRepository
from domain.handlers.client.buy import choice_item, buy_item
from domain.states.client.buy.BuyItemState import BuyItemState
from presentation.keyboards.client.buy.kb_buy_category import kb_buy_category_choice, BuyCategoryChoice, \
    BuyCategoryNavigation
from presentation.keyboards.client.buy.kb_buy_item import kb_buy_item_choice, BuyChoiceCategoryBack

router = Router()

router.include_routers(
    choice_item.router,
    buy_item.router
)


@router.message(F.text == L.CLIENT.BUY())
async def buy_item_menu(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(BuyItemState.Category)

    categories = CategoryRepository().categories()
    await message.answer(i18n.CLIENT.BUY.CHOICE_CATEGORY(), reply_markup=kb_buy_category_choice(categories))


@router.callback_query(BuyCategoryNavigation.filter(), BuyItemState.Category)
async def choice_buy_category_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    categories = CategoryRepository().categories()

    await state.update_data(last_page_category_buy=int(page))

    await callback.message.edit_reply_markup(reply_markup=kb_buy_category_choice(categories, int(page)))


@router.callback_query(BuyCategoryChoice.filter())
async def choice_buy_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    category = callback.data.split(":")[1]

    if not CategoryRepository().category(category):
        await callback.answer(i18n.CLIENT.BUY.NOT_EXIST(), show_alert=True)
        return

    items = ItemRepository().items_by_category(category)

    if len(items) <= 0:
        await callback.answer(i18n.CLIENT.BUY.EMPTY_ITEMS(), show_alert=True)
        return

    await state.update_data(category=category)
    await state.set_state(BuyItemState.Item)

    await callback.message.edit_text(
        text=i18n.CLIENT.BUY.CHOICE_ITEM(category=category),
        reply_markup=kb_buy_item_choice(items)
    )


@router.callback_query(BuyChoiceCategoryBack.filter(), BuyItemState.Item)
async def choice_buy_category_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    await state.set_state(BuyItemState.Category)

    categories = CategoryRepository().categories()

    await callback.message.edit_text(
        i18n.CLIENT.BUY.CHOICE_CATEGORY(),
        reply_markup=kb_buy_category_choice(categories, data.get('last_page_category_buy', 1))
    )
