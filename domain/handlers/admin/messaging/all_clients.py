from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.states.messaging.AllClientsMessagingState import AllClientsMessagingState
from domain.states.messaging.MessagingState import MessagingState
from presentation.keyboards.admin.kb_messaging import AllClientsMessaging, kb_back_messaging, kb_messaging_categories

router = Router()


@router.callback_query(AllClientsMessaging.filter(), MessagingState.MessagingType)
async def set_message(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AllClientsMessagingState.Message)
    await callback.message.edit_text(i18n.ADMIN.SET_MESSAGE(), reply_markup=kb_back_messaging)


@router.message(AllClientsMessagingState.Message)
async def set_media(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(message=message.html_text)
    await message.answer(i18n.ADMIN.SET_MEDIA(), reply_markup=kb_back_messaging)
    await state.set_state(AllClientsMessagingState.Media)


@router.message(AllClientsMessagingState.Media, (F.photo | F.animation | F.video | (F.text & F.text == L.SKIP())))
async def set_button()