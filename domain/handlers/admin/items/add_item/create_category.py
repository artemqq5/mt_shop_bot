from aiogram import Router

from presentation.keyboards.admin.kb_add_item import CreateNewCategory

router = Router()

@router.callback_query(CreateNewCategory.filter())
async def choice_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    category = callback.data.split(":")[1]
    await state.update_data(category=category)
    await state.set_state(AddItemState.title)

    await callback.message.answer(i18n.ADMIN.TITLE_ITEM())