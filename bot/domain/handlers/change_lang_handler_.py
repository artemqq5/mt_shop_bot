from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext, L

from bot.data.default_constants import ADMIN, CLIENT
from bot.data.repository.users import UserRepository
from bot.domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from bot.presentation.keyboards.admin.kb_menu import kb_menu_admin
from bot.presentation.keyboards.change_lang_kb.change_lang_kb import (
    ChangeLang,
    kb_change_lang,
)
from bot.presentation.keyboards.client._default import kb_menu_client

router = Router()

router.message.middleware(IsRoleMiddleware(CLIENT, ADMIN))
router.callback_query.middleware(IsRoleMiddleware(CLIENT, ADMIN))


@router.message(L.GENERAL.CHANGE_LANG())
async def change_language(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.GENERAL.CHANGE_LANG(), reply_markup=kb_change_lang)


@router.callback_query(ChangeLang.filter())
async def change_lang_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, current_user: dict[str]):
    await callback.message.delete()
    lang = callback.data.split(":")[1]

    # attempt to update the language to the same
    if lang == current_user["lang"]:
        await callback.message.answer(text=i18n.GENERAL.CHANGE_LANG.SUCCESS())
        return

    result = UserRepository().update_lang(callback.from_user.id, lang)
    if not result:
        await callback.message.answer(text=i18n.GENERAL.CHANGE_LANG.FAIL())
        return

    with i18n.use_locale(lang):
        if current_user["role"] == ADMIN:
            kb = kb_menu_admin
        else:
            kb = kb_menu_client

        await callback.message.answer(text=i18n.GENERAL.CHANGE_LANG.SUCCESS(), reply_markup=kb)
