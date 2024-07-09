from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from domain.states.AddItemState import AddItemState
from presentation.keyboards.admin.kb_add_item import kb_choice_category, CategoryChoice

router = Router()


@router.message(F.text == L.ADMIN.ADD_ITEM())
async def add(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddItemState.category)

    categories = CategoryRepository().categories()
    await message.answer(i18n.ADMIN.ADD_ITEM.CHOICE_CATEGORY(), reply_markup=kb_choice_category(categories))


@router.callback_query(CategoryChoice.filter(), AddItemState.category)
async def choice_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    category = callback.data.split(":")[1]
    await state.update_data(category=category)
    await state.set_state(AddItemState.title)

    await callback.message.answer(i18n.ADMIN.TITLE_ITEM())


@router.message(AddItemState.title)
async def set_title_item(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.edit_text(i18n.ADMIN.TITLE_ITEM_ERROR(count=len(message.text)))
        return

    await state.update_data(title=message.text)
    await state.set_state(AddItemState.desc)
    await message.edit_text(i18n.ADMIN.DESC_ITEM())


@router.message(AddItemState.desc)
async def set_desc_item(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(desc=message.text)
    await state.set_state(AddItemState.cost)
    await message.edit_text(i18n.ADMIN.COST_ITEM())


@router.message(AddItemState.cost)
async def set_cost_item(message: types.Message, state: FSMContext, i18n: I18nContext):
    if not message.text.isdigit():
        await message.edit_text(i18n.ADMIN.COST_ITEM_ERROR())
        return

    await state.update_data(cost=message.text)
    await state.set_state(AddItemState.cost)
    await message.edit_text(i18n.ADMIN.COST_ITEM())

    await message.edit_text()




