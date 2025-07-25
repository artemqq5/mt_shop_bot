from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from bot.data.repository.categories import CategoryRepository
from bot.domain.states.admin.management.ManageCategoryState import (
    ManagementCategoryState,
)
from bot.presentation.keyboards.admin.management.category.kb_create_category import (
    kb_create_category_next,
)
from bot.presentation.keyboards.admin.management.category.kb_managment import (
    CreateNewCategory,
    kb_back_category_choice,
)

router = Router()


@router.callback_query(CreateNewCategory.filter())
async def create_new_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementCategoryState.CreateCategory)
    await callback.message.edit_text(i18n.ADMIN.CATEGORY_NAME(), reply_markup=kb_back_category_choice)


@router.message(ManagementCategoryState.CreateCategory)
async def set_name_category(message: Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.answer(
            i18n.ADMIN.NAME_CATEGORY_ERROR(count=len(message.text)), reply_markup=kb_back_category_choice
        )
        return

    if not CategoryRepository().add(message.text):
        await message.answer(i18n.ADMIN.CATEGORY_FAIL_ADD(), reply_markup=kb_back_category_choice)
        return

    await message.answer(i18n.ADMIN.CATEGORY_SUCCESS_ADD(name=message.text), reply_markup=kb_create_category_next)
