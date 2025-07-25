from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.items import ItemRepository
from presentation.keyboards.admin.management.item.kb_management_item import ItemManagementVisibility

router = Router()


@router.callback_query(ItemManagementVisibility.filter())
async def visibility_manage_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    visibility = callback.data.split(":")[2]

    from domain.handlers.admin.management.item.choice_item import management_item_back

    if ItemRepository().update_visibility(item_id=int(item_id), visibility=int(visibility)):
        await management_item_back(callback, state, i18n)
