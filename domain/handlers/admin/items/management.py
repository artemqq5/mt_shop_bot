from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from data.repository.items import ItemRepository
from domain.handlers.admin.items import add_category, add_item
from domain.states.AddItemState import AddItemState
from domain.states.ManageItemState import ManagementItemState
from presentation.keyboards.admin.kb_managment import kb_category_management, kb_choice_category, CategoryNavigation, \
    CategoryChoice, ManagementBack, CategoryManagementAddItem, kb_back_category_management, ChoiceCategoryBack

router = Router()
router.include_routers(
    add_item.router,
    add_category.router
)


@router.message(F.text == L.ADMIN.MANAGEMENT())
async def manage(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementItemState.category)

    categories = CategoryRepository().categories()
    await message.answer(i18n.ADMIN.CHOICE_CATEGORY(), reply_markup=kb_choice_category(categories, 1))


@router.callback_query(CategoryNavigation.filter(), ManagementItemState.category)
async def choice_category_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    categories = CategoryRepository().categories()

    await callback.message.edit_reply_markup(reply_markup=kb_choice_category(categories, int(page)))


@router.callback_query(CategoryChoice.filter(), ManagementItemState.category)
async def choice_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    category = callback.data.split(":")[1]
    category_model = CategoryRepository().category(category)
    items_count = len(ItemRepository().items_by_category(category))

    await callback.message.edit_text(
        text=i18n.ADMIN.CATEGORY_INFO(category=category, count=items_count),
        reply_markup=kb_category_management(category_model)
    )


@router.callback_query(CategoryManagementAddItem.filter(), ManagementItemState.category)
async def add_item_management(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    category = callback.data.split(":")[1]
    await state.set_state(AddItemState.title)
    await state.update_data(category=category)
    await callback.message.edit_text(i18n.ADMIN.TITLE_ITEM(), reply_markup=kb_back_category_management(category))


@router.callback_query(ChoiceCategoryBack.filter())
async def choice_category_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.delete()
    await manage(callback.message, state, i18n)


@router.callback_query(ManagementBack.filter())
async def management_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementItemState.category)
    await choice_category(callback, state, i18n)
