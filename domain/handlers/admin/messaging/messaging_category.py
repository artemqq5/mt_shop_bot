from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.handlers.admin.messaging import all_clients, individual
from domain.states.messaging.MessagingState import MessagingState
from presentation.keyboards.admin.kb_messaging import kb_messaging_categories, BackMessaging

router = Router()

router.include_routers(
    all_clients.router,
    individual.router
)


@router.message(F.text == L.ADMIN.MESSAGING())
async def messaging(message: types.Message, state: FSMContext, i18n: I18nContext):
    await message.answer(i18n.ADMIN.CHOICE_TYPE_MESSAGE(), reply_markup=kb_messaging_categories)
    await state.set_state(MessagingState.MessagingType)


@router.callback_query(BackMessaging.filter())
async def messaging_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(i18n.ADMIN.CHOICE_TYPE_MESSAGE(), reply_markup=kb_messaging_categories)
    await state.set_state(MessagingState.MessagingType)
