import uuid

from aiogram import Bot, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from bot.data.repository.items import ItemRepository
from bot.data.repository.orders import OrderRepository
from bot.data.repository.users import UserRepository
from bot.domain.notification.NotificationAdmin import NotificationAdmin
from bot.domain.states.client.buy.BuyItemState import BuyItemState
from bot.presentation.keyboards.client.buy.kb_buy_item import BuyItemCallback
from bot.presentation.keyboards.client.buy.kb_order_item import (
    BuyOrderDescSkip,
    BuyOrderItemRestart,
    BuyOrderItemSend,
    kb_buy_item_back,
    kb_buy_item_skip,
    kb_buy_preview_item,
    kb_buy_send_error,
)
from bot.presentation.keyboards.client.profile.kb_balance import kb_balance_replenish

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
    await state.update_data(total_cost=round(num * data["item"]["cost"], 3))

    await state.set_state(BuyItemState.BuySetDesc)

    await message.answer(i18n.CLIENT.BUY.DESC(), reply_markup=kb_buy_item_skip)


@router.callback_query(BuyOrderDescSkip.filter(), BuyItemState.BuySetDesc)
async def buy_desc_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.update_data(desc="-")
    await state.set_state(BuyItemState.BuyItemPreview)

    data = await state.get_data()

    await callback.message.edit_text(
        i18n.CLIENT.BUY.PREVIEW(
            title=data["item"]["title"], count=data["count"], cost=data["total_cost"], desc=data["desc"]
        ),
        reply_markup=kb_buy_preview_item(data["item"]["id"]),
    )


@router.message(BuyItemState.BuySetDesc)
async def set_buy_desc(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 500:
        await message.answer(i18n.CLIENT.BUY.DESC_ERROR(size=len(message.text)), reply_markup=kb_buy_item_back)

    await state.update_data(desc=message.text)
    await state.set_state(BuyItemState.BuyItemPreview)

    data = await state.get_data()

    await message.answer(
        i18n.CLIENT.BUY.PREVIEW(
            title=data["item"]["title"], count=data["count"], cost=data["total_cost"], desc=data["desc"]
        ),
        reply_markup=kb_buy_preview_item(data["item"]["id"]),
    )


@router.callback_query(BuyOrderItemSend.filter(), BuyItemState.BuyItemPreview)
async def buy_order_send(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()

    identify = str(uuid.uuid4())
    user = UserRepository().user(callback.from_user.id)

    if user["balance"] < data["total_cost"]:
        difference = data["total_cost"] - user["balance"]
        await callback.message.edit_text(
            i18n.CLIENT.BALANCE_INSUFFICIENT(
                balance=user["balance"], invoice=data["total_cost"], difference=difference
            ),
            reply_markup=kb_balance_replenish,
        )
        await NotificationAdmin.balance_insufficient(data, bot, i18n)
        return

    if not OrderRepository().add(
        user_id=data["user_id"],
        category=data["item"]["category"],
        item_id=data["item"]["id"],
        item_title=data["item"]["title"],
        desc=data["desc"],
        count=data["count"],
        total_cost=data["total_cost"],
        identify=identify,
    ):
        await callback.message.edit_text(
            i18n.CLIENT.BUY.SEND_ERROR(), reply_markup=kb_buy_send_error(data["item"]["id"])
        )
        return

    balance_value = user["balance"] - data["total_cost"]
    UserRepository().update_balance(user["user_id"], balance_value)

    await NotificationAdmin.new_order(identify, bot, i18n)
    await callback.message.answer(i18n.CLIENT.BUY.SEND_SUCCESS())

    from bot.domain.handlers.client.buy.choice_item import item_buy_back

    await item_buy_back(callback, state, i18n)


@router.callback_query(BuyOrderItemRestart.filter(), BuyItemState.BuyItemPreview)
async def buy_order_restart(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await buy_item_callback(callback, state, i18n)
