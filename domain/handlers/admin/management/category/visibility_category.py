from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.categories import CategoryRepository
from presentation.keyboards.admin.management.category.kb_managment import CategoryManagementVisibility, ManagementBack

router = Router()


@router.callback_query(CategoryManagementVisibility.filter())
async def visibility_manage_category(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    visibility = callback.data.split(":")[1]
    data = await state.get_data()

    from domain.handlers.admin.management.choice_category_main import management_back
    new_callback = CallbackQuery(
        id=callback.id,
        from_user=callback.from_user,
        message=callback.message,
        chat_instance=callback.chat_instance,
        data=ManagementBack(category=data['category']).pack(),
        inline_message_id=callback.inline_message_id,
        chat=callback.message.chat,
        json=callback.json
    )

    if CategoryRepository().update_visibility(name=data['category'], visibility=int(visibility)):
        await management_back(new_callback, state, i18n)
