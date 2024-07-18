from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.items import ItemRepository
from domain.states.client.buy.BuyItemState import BuyItemState
from presentation.keyboards.client.buy.kb_buy_item import BuyItemChoice, BuyItemNavigation, kb_buy_item_choice, \
    kb_item_buy, BuyChoiceItemBack

router = Router()


@router.callback_query(BuyItemNavigation.filter(), BuyItemState.Item)
async def choice_buy_item_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]

    data = await state.get_data()
    items = ItemRepository().items_by_category(data['category'])

    await state.update_data(last_page_item_buy=int(page))

    await callback.message.edit_reply_markup(reply_markup=kb_buy_item_choice(items, int(page)))


@router.callback_query(BuyItemChoice.filter(), BuyItemState.Item)
async def choice_buy_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    item = ItemRepository().item(item_id)

    if not item:
        await callback.answer(i18n.CLIENT.BUY.NOT_EXIST(), show_alert=True)
        return

    await callback.message.edit_text(
        i18n.CLIENT.BUY.ITEM_TEMPLATE(title=item['title'], category=item['category'], cost=item['cost'], desc=item['desc']),
        reply_markup=kb_item_buy(item_id)
    )


@router.callback_query(BuyChoiceItemBack.filter())
async def item_buy_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BuyItemState.Item)

    data = await state.get_data()
    items = ItemRepository().items_by_category(data['category'])

    await callback.message.edit_text(
        text=i18n.CLIENT.BUY.CHOICE_ITEM(category=data['category']),
        reply_markup=kb_buy_item_choice(items, data.get('last_page_item_buy', 1))
    )
