from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.items import ItemRepository
from data.repository.orders import OrderRepository
from data.repository.users import UserRepository
from domain.states.admin.orders.ListOrdersState import ListOrdersState
from presentation.keyboards.admin.orders.kb_orders_list import kb_orders_choice, ChoiceOrderItem, OrderItemNavigation, \
    kb_order_back, OrderItemBack

router = Router()


@router.message(F.text == L.ADMIN.ORDERS())
async def order_list_main(message: types.Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    await state.clear()
    await state.set_state(ListOrdersState.ListOrders)

    orders = OrderRepository().orders()
    await message.answer(i18n.ADMIN.ORDERS_HISTORY(), reply_markup=kb_orders_choice(orders))


@router.callback_query(OrderItemNavigation.filter(), ListOrdersState.ListOrders)
async def choice_order_item_navigation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    orders = OrderRepository().orders()

    await callback.message.edit_text(i18n.ADMIN.ORDERS(), reply_markup=kb_orders_choice(orders, int(page)))


@router.callback_query(ChoiceOrderItem.filter(), ListOrdersState.ListOrders)
async def choice_order_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    order_id = callback.data.split(":")[1]
    page = callback.data.split(":")[2]

    await state.set_state(ListOrdersState.OrderView)

    order = OrderRepository().order(order_id)
    item = ItemRepository().item_all(order['item_id'])
    user = UserRepository().user(order['user_id'])

    username = f"@{user['username']}" if user['username'] else i18n.ADMIN.USERNAME_HAVNT()

    await callback.message.edit_text(
        i18n.ADMIN.ORDER_ITEM_TEMPLATE(
            id=order['id'],
            date=order['date'],
            name=item['title'],
            category=order['category'],
            count=order['count'],
            price=order['total_cost'],
            desc=str(order['desc']),
            user_id=order['user_id'],
            username=username
        ),
        reply_markup=kb_order_back(int(page))
    )


@router.callback_query(OrderItemBack.filter(), ListOrdersState.OrderView)
async def order_item_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    await state.set_state(ListOrdersState.ListOrders)
    orders = OrderRepository().orders()

    await callback.message.edit_text(i18n.ADMIN.ORDERS_HISTORY(), reply_markup=kb_orders_choice(orders, int(page)))
