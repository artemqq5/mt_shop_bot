from datetime import datetime

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.orders import OrderRepository
from data.repository.users import UserRepository
from domain.states.client.profile.ProfileState import ProfileState
from presentation.keyboards.client.profile.kb_profile import kb_profile_orders

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

        ), reply_markup=kb_profile_orders
    )

# @router.callback_query(, ProfileState.ProfileView)