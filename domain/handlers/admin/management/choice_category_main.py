from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from data.repository.items import ItemRepository
from domain.handlers.admin.management.category import visibility_category, add_category, delete_category
from domain.handlers.admin.management.item import choice_item
from domain.states.admin.management.ManageCategoryState import ManagementCategoryState
from presentation.keyboards.admin.management.category.kb_managment import kb_category_management, kb_choice_category, \
    CategoryNavigation, \
    CategoryChoice, ManagementBack, ChoiceCategoryBack

router = Router()
router.include_routers(
    add_category.router,
    delete_category.router,
    visibility_category.router,
    choice_item.router
)


@router.callback_query(CategoryNavigation.filter(), ManagementCategoryState.SetCategory)
async def choice_category_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    categories = CategoryRepository().categories_all()

    await state.update_data(last_page_category_manage=int(page))

    await callback.message.edit_reply_markup(reply_markup=kb_choice_category(categories, int(page)))


@router.callback_query(CategoryChoice.filter(), ManagementCategoryState.SetCategory)
async def choice_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    category = callback.data.split(":")[1]

    category_model = CategoryRepository().category_all(category)
    items_count = len(ItemRepository().items_by_category(category))

    await state.update_data(category=category)

    await callback.message.edit_text(
        text=i18n.ADMIN.CATEGORY_INFO(category=category, count=items_count),
        reply_markup=kb_category_management(category_model)
    )


@router.callback_query(ChoiceCategoryBack.filter())
async def choice_category_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementCategoryState.SetCategory)
    data = await state.get_data()

    categories = CategoryRepository().categories_all()
    page = data.get('last_page_category_manage', 1) if len(categories) > 5 else 1

    await callback.message.edit_text(
        i18n.ADMIN.CHOICE_CATEGORY(),
        reply_markup=kb_choice_category(categories, page)
    )


@router.callback_query(ManagementBack.filter())
async def management_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ManagementCategoryState.SetCategory)
    await choice_category(callback, state, i18n)
