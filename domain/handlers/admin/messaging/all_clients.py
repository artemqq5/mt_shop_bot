from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.handlers.admin.messaging.MessagingTools import MessagingTools
from domain.states.messaging.AllClientsMessagingState import AllClientsMessagingState
from domain.states.messaging.MessagingState import MessagingState
from presentation.keyboards.admin.kb_messaging import AllClientsMessaging, kb_back_messaging, kb_messaging_categories, \
    kb_skip_messaging_media, kb_skip_messaging_button, MediaMessagingSkip, kb_repeat_button_messaging, \
    RepeatButtonChoice, kb_send_message_all_clients, SendMessageAllClients, RestartMessage, ButtonMessagingSkip

router = Router()


@router.callback_query(AllClientsMessaging.filter(), MessagingState.MessagingType)
async def set_message(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AllClientsMessagingState.Message)
    await callback.message.edit_text(i18n.ADMIN.SET_MESSAGE(), reply_markup=kb_back_messaging)


@router.message(AllClientsMessagingState.Message)
async def set_media(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(message=message.html_text)
    await state.update_data(buttons=[])

    await message.answer(i18n.ADMIN.SET_MEDIA(), reply_markup=kb_skip_messaging_media)
    await state.set_state(AllClientsMessagingState.Media)


@router.callback_query(MediaMessagingSkip.filter(), AllClientsMessagingState.Media)
async def media_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AllClientsMessagingState.ButtonText)
    await callback.message.answer(i18n.ADMIN.SET_BUTTON(), reply_markup=kb_skip_messaging_button)


@router.message(AllClientsMessagingState.Media, (F.photo | F.animation | F.video))
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

    await state.set_state(AllClientsMessagingState.ButtonText)
    await message.answer(i18n.ADMIN.SET_BUTTON(), reply_markup=kb_skip_messaging_button)


@router.callback_query(ButtonMessagingSkip.filter(), AllClientsMessagingState.ButtonText)
async def button_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    button = callback.data.split(":")[1]
    if not int(button):
        await state.set_state(AllClientsMessagingState.Preview)
        data = await state.get_data()
        await MessagingTools.preview_message(data, callback.message)
        await callback.message.edit_text(i18n.ADMIN.PREVIEW_MESSAGING(), reply_markup=kb_send_message_all_clients)
    else:
        await callback.message.edit_text(i18n.ADMIN.SET_BUTTON_TEXT(), reply_markup=kb_back_messaging)


@router.message(AllClientsMessagingState.ButtonText)
async def set_button_text(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.answer(i18n.ADMIN.BUTTON_TEXT_ERROR(count=len(message.text)), reply_markup=kb_back_messaging)
        return

    await MessagingTools.add_new_button(state)
    await MessagingTools.add_text_last_button(state, message.text)
    await state.set_state(AllClientsMessagingState.ButtonUrl)
    await message.answer(i18n.ADMIN.SET_BUTTON_URL(), reply_markup=kb_back_messaging)


@router.message(AllClientsMessagingState.ButtonUrl)
async def set_button_url(message: types.Message, state: FSMContext, i18n: I18nContext):
    if not MessagingTools.is_valid_url(message.text):
        await message.answer(i18n.ADMIN.BUTTON_URL_ERROR(), reply_markup=kb_back_messaging)
        return

    await MessagingTools.add_url_last_button(state, message.text)
    await state.set_state(AllClientsMessagingState.RepeatButton)
    await message.answer(i18n.ADMIN.SET_BUTTON_NEXT(), reply_markup=kb_repeat_button_messaging)


@router.callback_query(RepeatButtonChoice.filter(), AllClientsMessagingState.RepeatButton)
async def repeat_button(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    repeat = callback.data.split(":")[1]
    if int(repeat):
        await state.set_state(AllClientsMessagingState.ButtonText)
        await callback.message.answer(i18n.ADMIN.SET_BUTTON_TEXT(), reply_markup=kb_back_messaging)
    else:
        await state.set_state(AllClientsMessagingState.Preview)
        data = await state.get_data()

        await MessagingTools.preview_message(data, callback.message)
        await callback.message.answer(i18n.ADMIN.PREVIEW_MESSAGING(), reply_markup=kb_send_message_all_clients)


@router.callback_query(SendMessageAllClients.filter(), AllClientsMessagingState.Preview)
async def preview_send(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    print("send all clients")


@router.callback_query(RestartMessage.filter(), AllClientsMessagingState.Preview)
async def preview_start_again(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await set_message(callback, state, i18n)
