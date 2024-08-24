from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.default_constants import ALL_CLIENT_MESSAGING
from domain.handlers.admin.messaging.MessagingTools import MessagingTools
from domain.notification.NotificationClient import NotificationClient
from domain.states.admin.messaging.MessagingState import MessagingState
from presentation.keyboards.admin.messaging.kb_messaging import kb_back_messaging, kb_messaging_categories, \
    kb_skip_messaging_media, kb_skip_messaging_button, MediaMessagingSkip, kb_repeat_button_messaging, \
    RepeatButtonChoice, kb_send_message_all_clients, SendMessageAllClients, ButtonMessagingSkip, \
    ChoiceTypeMessaging
from presentation.keyboards.admin.messaging.kb_messaging import BackMessaging

router = Router()


@router.callback_query(BackMessaging.filter())
async def messaging_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(i18n.ADMIN.CHOICE_TYPE_MESSAGE(), reply_markup=kb_messaging_categories)
    await state.set_state(MessagingState.MessagingType)


@router.callback_query(ChoiceTypeMessaging.filter(), MessagingState.MessagingType)
async def set_type(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    type_m = callback.data.split(":")[1]
    await state.update_data(type_messaging=type_m)

    if type_m == ALL_CLIENT_MESSAGING:
        await state.set_state(MessagingState.Message)
        await callback.message.edit_text(i18n.ADMIN.SET_MESSAGE(), reply_markup=kb_back_messaging)
    else:
        await state.set_state(MessagingState.TelegramID)
        await callback.message.edit_text(i18n.ADMIN.SET_USER_ID(), reply_markup=kb_back_messaging)


@router.message(MessagingState.TelegramID)
async def set_telegram_id(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(telegram_id=message.text)
    await state.set_state(MessagingState.Message)
    await message.answer(i18n.ADMIN.SET_MESSAGE(), reply_markup=kb_back_messaging)


@router.message(MessagingState.Message)
async def set_media(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(message=message.html_text)
    await state.update_data(buttons=[])

    await message.answer(i18n.ADMIN.SET_MEDIA(), reply_markup=kb_skip_messaging_media)
    await state.set_state(MessagingState.Media)


@router.callback_query(MediaMessagingSkip.filter(), MessagingState.Media)
async def media_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(MessagingState.ButtonText)
    await callback.message.answer(i18n.ADMIN.SET_BUTTON(), reply_markup=kb_skip_messaging_button)


@router.message(MessagingState.Media, (F.photo | F.animation | F.video))
async def set_button(message: types.Message, state: FSMContext, i18n: I18nContext):
    if message.content_type == 'photo':
        await state.update_data(photo=message.photo[-1].file_id)
    elif message.content_type == 'animation':
        await state.update_data(animation=message.document.file_id)
    elif message.content_type == 'video':
        await state.update_data(video=message.video.file_id)
    else:
        await message.answer(i18n.ADMIN.MEDIA_WRONG(), reply_markup=kb_skip_messaging_media)
        return

    await state.set_state(MessagingState.ButtonText)
    await message.answer(i18n.ADMIN.SET_BUTTON(), reply_markup=kb_skip_messaging_button)


@router.callback_query(ButtonMessagingSkip.filter(), MessagingState.ButtonText)
async def button_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    button = callback.data.split(":")[1]
    if not int(button):
        await state.set_state(MessagingState.Preview)
        data = await state.get_data()
        await MessagingTools.preview_message_send(data, bot, callback.from_user.id)
        await callback.message.answer(i18n.ADMIN.PREVIEW_MESSAGING(), reply_markup=kb_send_message_all_clients)
    else:
        await callback.message.edit_text(i18n.ADMIN.SET_BUTTON_TEXT(), reply_markup=kb_back_messaging)


@router.message(MessagingState.ButtonText)
async def set_button_text(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.answer(i18n.ADMIN.BUTTON_TEXT_ERROR(count=len(message.text)), reply_markup=kb_back_messaging)
        return

    await MessagingTools.add_new_button(state)
    await MessagingTools.add_text_last_button(state, message.text)
    await state.set_state(MessagingState.ButtonUrl)
    await message.answer(i18n.ADMIN.SET_BUTTON_URL(), reply_markup=kb_back_messaging)


@router.message(MessagingState.ButtonUrl)
async def set_button_url(message: types.Message, state: FSMContext, i18n: I18nContext):
    if not MessagingTools.is_valid_url(message.text):
        await message.answer(i18n.ADMIN.BUTTON_URL_ERROR(), reply_markup=kb_back_messaging)
        return

    await MessagingTools.add_url_last_button(state, message.text)
    await state.set_state(MessagingState.RepeatButton)
    await message.answer(i18n.ADMIN.SET_BUTTON_NEXT(), reply_markup=kb_repeat_button_messaging)


@router.callback_query(RepeatButtonChoice.filter(), MessagingState.RepeatButton)
async def repeat_button(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    repeat = callback.data.split(":")[1]
    if int(repeat):
        await state.set_state(MessagingState.ButtonText)
        await callback.message.edit_text(i18n.ADMIN.SET_BUTTON_TEXT(), reply_markup=kb_back_messaging)
    else:
        await state.set_state(MessagingState.Preview)
        data = await state.get_data()

        await MessagingTools.preview_message_send(data, bot, callback.from_user.id)
        await callback.message.answer(i18n.ADMIN.PREVIEW_MESSAGING(), reply_markup=kb_send_message_all_clients)


@router.callback_query(SendMessageAllClients.filter(), MessagingState.Preview)
async def preview_send(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()

    if data.get('telegram_id', None):
        result = await NotificationClient.push_individual_client(data, bot, data.get('telegram_id'), i18n)
    else:
        result = await NotificationClient.push_all_clients(data, bot, i18n)

    await state.clear()
    await callback.message.edit_text(result, reply_markup=kb_back_messaging)
