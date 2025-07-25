from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from bot.data.repository.items import ItemRepository
from bot.domain.handlers.admin.management.item import (
    add_item,
    delete_item,
    visibility_item,
)
from bot.domain.states.admin.management.ManagementItemState import ManagementItemState
from bot.presentation.keyboards.admin.management.category.kb_managment import (
    CategoryManagementItemList,
)
from bot.presentation.keyboards.admin.management.item.kb_management_item import (
    ChoiceItemBack,
    ItemChoice,
    ItemNavigation,
    ManagementItemBack,
    kb_choice_item,
    kb_item_management,
)

router = Router()

router.include_routers(add_item.router, delete_item.router, visibility_item.router)


@router.callback_query(CategoryManagementItemList.filter())
async def item_list(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    items = ItemRepository().items_by_category_all(data["category"])
    page = data.get("last_page_item_manage", 1) if len(items) > 5 else 1

    await state.set_state(ManagementItemState.SetItem)

    await callback.message.edit_text(
        i18n.ADMIN.ITEMS_GROUP_INFO(category=data["category"]),
        reply_markup=kb_choice_item(items, data["category"], page),
    )


@router.callback_query(ItemNavigation.filter(), ManagementItemState.SetItem)
async def choice_item_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    data = await state.get_data()
    items = ItemRepository().items_by_category_all(data["category"])

    await state.update_data(last_page_item_manage=int(page))

    await callback.message.edit_reply_markup(reply_markup=kb_choice_item(items, data["category"], int(page)))


@router.callback_query(ItemChoice.filter(), ManagementItemState.SetItem)
async def choice_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    item = ItemRepository().item_all(item_id)
    await callback.message.edit_text(
        i18n.ADMIN.PREVIEW_ITEM(title=item["title"], category=item["category"], cost=item["cost"], desc=item["desc"]),
        reply_markup=kb_item_management(item),
    )


@router.callback_query(ChoiceItemBack.filter())
async def choice_item_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await item_list(callback, state, i18n)


@router.callback_query(ManagementItemBack.filter())
async def management_item_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await choice_item(callback, state, i18n)
