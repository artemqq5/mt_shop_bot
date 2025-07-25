from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from domain.states.client.availability.AvailabilityState import AvailabilityState
from presentation.keyboards.client.availability.kb_avaibility import text_availability_list, kb_availability, \
    AvailabilityNavigation

router = Router()


@router.callback_query(AvailabilityNavigation.filter(), AvailabilityState.Aviability)
async def availability_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    categories = CategoryRepository().categories()
    await callback.message.edit_text(text_availability_list(categories, i18n, int(page)), reply_markup=kb_availability(categories, int(page)))
