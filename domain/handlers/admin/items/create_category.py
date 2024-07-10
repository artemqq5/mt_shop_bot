from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repository.categories import CategoryRepository
from domain.states.CreateCategoryState import CreateCategoryState
from presentation.keyboards.admin.kb_add_item import CreateNewCategory
from presentation.keyboards.admin.kb_create_category import CreateNewCategoryBack, kb_create_category_back, \
    kb_create_category_next

router = Router()


@router.callback_query(CreateNewCategory.filter())
async def create_new_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateCategoryState.name)
    await callback.message.edit_text(i18n.ADMIN.CATEGORY_NAME(), reply_markup=kb_create_category_back)


@router.callback_query(CreateNewCategoryBack.filter(), CreateCategoryState.name)
async def create_new_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    from domain.handlers.admin.items.add_item import add_item

    await state.clear()
    await add_item(callback.message, state, i18n)


@router.message(CreateCategoryState.name)
async def set_name_category(message: Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.answer(i18n.ADMIN.NAME_CATEGORY_ERROR(count=len(message.text)))
        return

    if not CategoryRepository().add(message.text):
        await message.answer(i18n.ADMIN.CATEGORY_FAIL_ADD())
        return

    await message.answer(i18n.ADMIN.CATEGORY_SUCCESS_ADD(name=message.text), reply_markup=kb_create_category_next)

