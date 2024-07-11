from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from domain.states.ManageItemState import ManagementCategoryState
from presentation.keyboards.admin.kb_managment import CategoryManagementDelete, kb_back_category_management

router = Router()


@router.callback_query(CategoryManagementDelete.filter())
async def delete_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementCategoryState.DeleteCategory)
    data = await state.get_data()
    await callback.message.edit_text(
        i18n.ADMIN.DELETE_CATEGORY_APPROVE(category=data['category']),
        reply_markup=kb_back_category_management(data['category'])
    )
