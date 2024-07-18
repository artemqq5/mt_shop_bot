from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.items import ItemRepository
from data.repository.orders import OrderRepository
from domain.notification.NotificationAdmin import NotificationAdmin
from domain.states.client.buy.BuyItemState import BuyItemState
from presentation.keyboards.client.buy.kb_buy_item import BuyItemCallback
from presentation.keyboards.client.buy.kb_order_item import kb_buy_preview_item, kb_buy_item_back, BuyOrderDescSkip, \
    BuyOrderItemSend, BuyOrderItemRestart, kb_buy_send_error, kb_buy_item_skip

router = Router()


@router.callback_query(BuyItemCallback.filter(), BuyItemState.Item)
async def buy_item_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    item = ItemRepository().item(item_id)

    if not item:
        await callback.answer(i18n.CLIENT.BUY.NOT_EXIST(), show_alert=True)
        return

    await state.update_data(item=item)
    await state.update_data(user_id=callback.from_user.id)
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

    data = await state.get_data()

    await state.update_data(count=num)
    await state.update_data(total_cost=round(num * data['item']['cost'], 3))

    await state.set_state(BuyItemState.BuySetDesc)

    await message.answer(i18n.CLIENT.BUY.DESC(), reply_markup=kb_buy_item_skip)


@router.callback_query(BuyOrderDescSkip.filter(), BuyItemState.BuySetDesc)
async def buy_desc_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.update_data(desc="-")
    await state.set_state(BuyItemState.BuyItemPreview)

    data = await state.get_data()

    await callback.message.edit_text(
        i18n.CLIENT.BUY.PREVIEW(
            title=data['item']['title'],
            count=data['count'],
            cost=data['total_cost'],
            desc=data['desc']
        ),
        reply_markup=kb_buy_preview_item(data['item']['id'])
    )


@router.message(BuyItemState.BuySetDesc)
async def set_buy_desc(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 500:
        await message.answer(i18n.CLIENT.BUY.DESC_ERROR(size=len(message.text)), reply_markup=kb_buy_item_back)

    await state.update_data(desc=message.text)
    await state.set_state(BuyItemState.BuyItemPreview)

    data = await state.get_data()

    await message.edit_text(
        i18n.CLIENT.BUY.PREVIEW(
            title=data['item']['title'],
            count=data['count'],
            cost=data['total_cost'],
            desc=data['desc']
        ),
        reply_markup=kb_buy_preview_item(data['item']['id'])
    )


@router.callback_query(BuyOrderItemSend.filter(), BuyItemState.BuyItemPreview)
async def buy_order_send(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()

    if not OrderRepository().add(
            user_id=data['user_id'],
            category=data['item']['category'],
            desc=data['desc'],
            count=data['count'],
            total_cost=data['total_cost']
    ):
        await callback.message.edit_text(
            i18n.CLIENT.BUY.SEND_ERROR(),
            reply_markup=kb_buy_send_error(data['item']['id'])
        )
        return

    await NotificationAdmin.new_order(data, bot, i18n)
    await callback.message.answer(i18n.CLIENT.BUY.SEND_SUCCESS())

    from domain.handlers.client.buy.choice_item import item_buy_back
    await item_buy_back()


@router.callback_query(BuyOrderItemRestart.filter(), BuyItemState.BuyItemPreview)
async def buy_order_restart(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await buy_item_callback(callback=callback, state=state, i18n=i18n)
