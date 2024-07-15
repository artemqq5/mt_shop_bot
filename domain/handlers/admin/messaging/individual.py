from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.states.messaging.MessagingState import MessagingState
from presentation.keyboards.admin.kb_messaging import IndividualMessaging

router = Router()


@router.callback_query(IndividualMessaging.filter(), MessagingState.MessagingType)
async def individual_messaging(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    pass
