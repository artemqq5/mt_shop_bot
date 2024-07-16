from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.categories import CategoryRepository
from data.repository.items import ItemRepository
from domain.states.management.ManageCategoryState import ManagementCategoryState
from presentation.keyboards.admin.management.kb_delete_category import kb_category_delete, CategoryApproveDelete
from presentation.keyboards.admin.management.kb_managment import CategoryManagementDelete, kb_back_category_choice

router = Router()


@router.callback_query(CategoryManagementDelete.filter())
async def delete_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementCategoryState.DeleteCategory)
    data = await state.get_data()
    await callback.message.edit_text(
        i18n.ADMIN.DELETE_CATEGORY_APPROVE(category=data['category']),
        reply_markup=kb_category_delete(data['category'])
    )


@router.callback_query(CategoryApproveDelete.filter(), ManagementCategoryState.DeleteCategory)
async def delete_approve_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if CategoryRepository().delete(data['category']):
        # optional delete management with same category
        ItemRepository().delete_by_category(data['category'])

        await callback.message.edit_text(
            i18n.ADMIN.DELETE_SUCCESS(),
            reply_markup=kb_back_category_choice
        )
    else:
        await callback.message.edit_text(
            i18n.ADMIN.DELETE_FAIL(),
            reply_markup=kb_back_category_choice
        )
