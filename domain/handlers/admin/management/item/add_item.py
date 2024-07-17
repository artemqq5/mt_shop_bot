from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.items import ItemRepository
from domain.states.admin.management.AddItemState import AddItemState
from domain.states.admin.management.ManageCategoryState import ManagementCategoryState
from presentation.keyboards.admin.management.kb_add_item import kb_preview_add_item, PreviewItemPublish, kb_publish_onemore
from presentation.keyboards.admin.management.kb_managment import kb_back_category_management, CategoryManagementAddItem

router = Router()


@router.callback_query(CategoryManagementAddItem.filter(), ManagementCategoryState.SetCategory)
async def add_item_management(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddItemState.title)
    data = await state.get_data()
    await callback.message.edit_text(i18n.ADMIN.TITLE_ITEM(), reply_markup=kb_back_category_management(data['category']))


@router.message(AddItemState.title)
async def set_title_item(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.answer(i18n.ADMIN.TITLE_ITEM_ERROR(count=len(message.text)), reply_markup=None)
        return

    data = await state.get_data()

    await state.update_data(title=message.text)
    await state.set_state(AddItemState.desc)
    await message.answer(i18n.ADMIN.DESC_ITEM(), reply_markup=kb_back_category_management(data['category']))


@router.message(AddItemState.desc)
async def set_desc_item(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(desc=message.html_text)
    await state.set_state(AddItemState.cost)

    data = await state.get_data()

    await message.answer(i18n.ADMIN.COST_ITEM(), reply_markup=kb_back_category_management(data['category']))


@router.message(AddItemState.cost)
async def set_cost_item(message: types.Message, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    try:
        float(message.text)
    except ValueError as e:
        await message.answer(i18n.ADMIN.COST_ITEM_ERROR(), reply_markup=kb_back_category_management(data['category']))
        return

    await state.update_data(cost=float(message.text))
    await state.set_state(AddItemState.preview)

    data = await state.get_data()

    await message.answer(i18n.ADMIN.PREVIEW_ITEM(
        title=data['title'], category=data['category'], cost=data['cost'], desc=data['desc']
    ), reply_markup=kb_preview_add_item(data['category']))


@router.callback_query(PreviewItemPublish.filter(), AddItemState.preview)
async def preview(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    mode = callback.data.split(":")[1]
    data = await state.get_data()

    if mode == "publish":
        if ItemRepository().add(data['title'], data['desc'], data['category'], data['cost']):
            await callback.message.edit_text(
                i18n.ADMIN.SUCCESS_PUBLISHED(),
                reply_markup=kb_publish_onemore(data['category'])
            )
        else:
            await callback.message.edit_text(
                i18n.ADMIN.FAIL_PUBLISHED(),
                reply_markup=kb_back_category_management(data['category'])
            )
    elif mode == "restart":
        await add_item_management(callback, state, i18n)
