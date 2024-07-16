from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.items import ItemRepository
from domain.handlers.admin.management.item import add_item, delete_item, visibility_item
from domain.states.management.ManagementItemState import ManagementItemState
from presentation.keyboards.admin.management.kb_management_item import kb_choice_item, ItemChoice, \
    ItemNavigation, kb_item_management, ChoiceItemBack, ManagementItemBack
from presentation.keyboards.admin.management.kb_managment import CategoryManagementItemList

router = Router()

router.include_routers(
    add_item.router,
    delete_item.router,
    visibility_item.router
)


@router.callback_query(CategoryManagementItemList.filter())
async def item_list(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    items = ItemRepository().items_by_category(data['category'])

    await state.set_state(ManagementItemState.SetItem)

    await callback.message.edit_text(
        i18n.ADMIN.ITEMS_GROUP_INFO(category=data['category']),
        reply_markup=kb_choice_item(items, data['category'], 1)
    )


@router.callback_query(ItemNavigation.filter(), ManagementItemState.SetItem)
async def choice_category_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    data = await state.get_data()
    items = ItemRepository().items_by_category(data['category'])

    await callback.message.edit_reply_markup(reply_markup=kb_choice_item(items, data['category'], int(page)))


@router.callback_query(ItemChoice.filter(), ManagementItemState.SetItem)
async def choice_item(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    item_id = callback.data.split(":")[1]
    item = ItemRepository().item(item_id)
    await callback.message.edit_text(
        i18n.ADMIN.PREVIEW_ITEM(title=item['title'], category=item['category'], cost=item['cost'], desc=item['desc']),
        reply_markup=kb_item_management(item)
    )


@router.callback_query(ChoiceItemBack.filter())
async def choice_item_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await item_list(callback, state, i18n)


@router.callback_query(ManagementItemBack.filter())
async def management_item_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await choice_item(callback, state, i18n)

