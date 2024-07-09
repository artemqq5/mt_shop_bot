from aiogram import Router, F, types
from aiogram_i18n import I18nContext, L

from data.repository.categories import CategoryRepository
from presentation.keyboards.admin.kb_add_item import kb_choice_category

router = Router()


@router.message(F.text == L.ADMIN.ADD_ITEM())
async def add_item(message: types.Message, i18n: I18nContext):
    categories = CategoryRepository().categories()
    await message.answer(i18n.ADMIN.ADD_ITEM.CHOICE_CATEGORY(), reply_markup=kb_choice_category(categories))
