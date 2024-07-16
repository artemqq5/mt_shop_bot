from aiogram import Router

from data.repository.items import ItemRepository
from presentation.keyboards.admin.management.kb_delete_item import kb_item_delete, ItemApproveDelete
from presentation.keyboards.admin.management.kb_management_item import ItemManagementDelete, kb_back_item_choice

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext
from domain.states.management.ManagementItemState import ManagementItemState

router = Router()


@router.callback_query(ItemManagementDelete.filter())
async def delete_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    item = ItemRepository().item(item_id)

    await state.set_state(ManagementItemState.DeleteItem)
    await callback.message.edit_text(
        i18n.ADMIN.DELETE_ITEM_APPROVE(item=item['title']),
        reply_markup=kb_item_delete(item)
    )


@router.callback_query(ItemApproveDelete.filter(), ManagementItemState.DeleteItem)
async def delete_approve_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]

    if ItemRepository().delete(item_id):
        await callback.message.edit_text(
            i18n.ADMIN.DELETE_SUCCESS(),
            reply_markup=kb_back_item_choice
        )
    else:
        await callback.message.edit_text(
            i18n.ADMIN.DELETE_FAIL(),
            reply_markup=kb_back_item_choice
        )
