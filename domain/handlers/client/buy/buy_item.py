from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.items import ItemRepository
from domain.states.client.buy.BuyItemState import BuyItemState
from presentation.keyboards.client.buy.kb_buy_item import BuyItemCallback
from presentation.keyboards.client.buy.kb_order_item import kb_buy_preview_item, kb_buy_item_back

router = Router()


@router.callback_query(BuyItemCallback.filter(), BuyItemState.Item)
async def buy_item_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    item = ItemRepository().item(item_id)

    if not item:
        await callback.answer(i18n.CLIENT.BUY.NOT_EXIST(), show_alert=True)
        return

    await state.update_data(item=item)
    await state.set_state(BuyItemState.BuySetCount)
    await callback.message.edit_text(i18n.CLIENT.BUY.COUNT(), reply_markup=kb_buy_item_back)


@router.message(BuyItemState.BuySetCount)
async def set_buy_count(message: types.Message, state: FSMContext, i18n: I18nContext):
    try:
        num = int(message.text)
        if num <= 0:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.CLIENT.BUY.COUNT_ERROR(), reply_markup=kb_buy_item_back)
        return

    await state.update_data(count=num)
    await state.set_state(BuyItemState.BuySetDesc)
    await message.answer(i18n.CLIENT.BUY.DESC(), reply_markup=kb_buy_item_back)


@router.message(BuyItemState.BuySetDesc)
async def set_buy_desc(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 500:
        await message.answer(i18n.CLIENT.BUY.DESC_ERROR(size=len(message.text)), reply_markup=kb_buy_item_back)

    await state.update_data(desc=message.text)
    await state.set_state(BuyItemState.BuyItemPreview)

    data = await state.get_data()

    await message.answer(
        i18n.CLIENT.BUY.PREVIEW(
            title=data['item']['title'],
            count=data['count'],
            cost=round(data['count'] * data['item']['cost'], 3),
            desc=data['desc']
        ),
        reply_markup=kb_buy_preview_item
    )
