from datetime import datetime

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.items import ItemRepository
from data.repository.orders import OrderRepository
from data.repository.users import UserRepository
from domain.states.client.profile.ProfileState import ProfileState
from presentation.keyboards.client.profile.kb_profile import kb_profile_orders, kb_profile, ProfileOrdersNav, \
    ProfileOrderDetail, MyOrdersProfile, ProfileBack, kb_profile_orders_back, ProfileOrdersBack

router = Router()


@router.message(F.text == L.CLIENT.PROFILE())
async def profile_menu(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(ProfileState.ProfileView)

    user = UserRepository().user(message.from_user.id)

    date_format = '%Y-%m-%d %H:%M:%S'
    start_date = datetime.strptime(str(user['join_at']), date_format)
    days_passed = (datetime.now() - start_date).days

    order_count = len(OrderRepository().orders_by_user_id(user['user_id']))

    await message.answer(
        i18n.CLIENT.PROFILE.MAIN_PAGE(
            telegram_id=user['user_id'],
            order_count=order_count,
            lang=user.get('lang', "-"),
            date=user['join_at'],
            days=days_passed

        ), reply_markup=kb_profile
    )


@router.callback_query(MyOrdersProfile.filter(), ProfileState.ProfileView)
async def profile_orders(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    orders = OrderRepository().orders_by_user_id(callback.from_user.id)

    if not orders:
        await callback.answer(i18n.CLIENT.PROFILE.EMPTY_ORDERS(buy_category_bot=i18n.CLIENT.BUY()), show_alert=True)
        return

    data = await state.get_data()
    page = data.get("last_orders_page_profile", 1)

    await state.set_state(ProfileState.Orders)
    await callback.message.edit_text(i18n.CLIENT.PROFILE.ORDERS(), reply_markup=kb_profile_orders(orders, page))


@router.callback_query(ProfileOrdersNav.filter(), ProfileState.Orders)
async def profile_orders_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    await state.update_data(last_orders_page_profile=int(page))

    orders = OrderRepository().orders_by_user_id(callback.from_user.id)
    await callback.message.edit_text(i18n.CLIENT.PROFILE.ORDERS(), reply_markup=kb_profile_orders(orders, int(page)))


@router.callback_query(ProfileBack.filter(), ProfileState.Orders)
async def profile_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await state.set_state(ProfileState.ProfileView)
    user = UserRepository().user(callback.from_user.id)

    date_format = '%Y-%m-%d %H:%M:%S'
    start_date = datetime.strptime(str(user['join_at']), date_format)
    days_passed = (datetime.now() - start_date).days

    order_count = len(OrderRepository().orders_by_user_id(user['user_id']))

    await callback.message.edit_text(
        i18n.CLIENT.PROFILE.MAIN_PAGE(
            telegram_id=user['user_id'],
            order_count=order_count,
            lang=user.get('lang', "-"),
            date=user['join_at'],
            days=days_passed

        ), reply_markup=kb_profile
    )


@router.callback_query(ProfileOrderDetail.filter(), ProfileState.Orders)
async def profile_detail_order(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    order_id = callback.data.split(":")[1]
    order = OrderRepository().order(order_id)
    item = ItemRepository().item(order['item_id'])

    await callback.message.edit_text(
        i18n.CLIENT.PROFILE.ORDER_TEMPLATE(
            id=order['id'],
            title=item['title'],
            count=order['count'],
            cost=order['total_cost'],
            desc=order['desc'],
            date=order['date']
        ),
        reply_markup=kb_profile_orders_back
    )


@router.callback_query(ProfileOrdersBack.filter(), ProfileState.Orders)
async def profile_orders_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await profile_orders(callback, state, i18n)
