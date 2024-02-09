from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.base_constants import *
from data.repository.users import UsersRepository
from handlers.buy.farm_use_case.output_farm import formatted_output_account, formatted_output_card, \
    formatted_output_cabinet, formatted_output_verification
from keyboard.accounts.accounts_keyboard import source_account_keyboard
from keyboard.admin.admin_items_keyboard import *
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.show_item_state import ShowItemState, ShowAccountState, ShowVerificationsState, ShowCabinetsState, \
    ShowCardsState


def register_show_item_handlers(dispatcher):
    dispatcher.register_message_handler(
        type_of_show_item,
        lambda message: message.text == SHOW_ITEMS
    )

    dispatcher.register_message_handler(
        choice_account_type,
        lambda message: message.text in LIST_OF_ITEMS_TYPE,
        state=[ShowItemState.type,
               ShowAccountState.source,
               ShowCardsState.source,
               ShowCabinetsState.source,
               ShowVerificationsState.source]
    )

    dispatcher.register_message_handler(
        source_account_item,
        lambda message: message.text in LIST_OF_ACCOUNTS_TYPE,
        state=ShowAccountState.source
    )

    dispatcher.register_callback_query_handler(
        account_detail_handler,
        lambda call: call.data in list_of_callback_menagment_accounts(),
        state=ShowAccountState.source
    )

    dispatcher.register_callback_query_handler(
        cards_detail_handler,
        lambda call: call.data in list_of_callback_menagment_cards(),
        state=ShowCardsState.source
    )

    dispatcher.register_callback_query_handler(
        cabinets_detail_handler,
        lambda call: call.data in list_of_callback_menagment_cabinets(),
        state=ShowCabinetsState.source
    )

    dispatcher.register_callback_query_handler(
        verifications_detail_handler,
        lambda call: call.data in list_of_callback_menagment_verifications(),
        state=ShowVerificationsState.source
    )


async def type_of_show_item(message: types.Message, state: FSMContext):
    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ====================
            await ShowItemState.type.set()  # set state to show item
            await message.answer(CHOICE_TYPE_OF_SHOW, reply_markup=choice_type_item_keyboard())
            # ==========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def choice_account_type(message: types.Message, state: FSMContext):
    await state.finish()

    if message.text == ACCOUNT_ITEM:
        await ShowAccountState.source.set()
        await message.answer(CHOICE_TYPE_OF_ACCOUNT, reply_markup=source_account_keyboard())
    elif message.text == CARDS_FARM:
        await ShowCardsState.source.set()
        await message.answer(CARDS_FARM, reply_markup=show_item_cards_keyboard())
    elif message.text == CABINETS_FARM:
        await ShowCabinetsState.source.set()
        await message.answer(CABINETS_FARM, reply_markup=show_item_cabinets_keyboard())
    elif message.text == VERIFICATIONS_FARM:
        await ShowVerificationsState.source.set()
        await message.answer(VERIFICATIONS_FARM, reply_markup=show_item_verifications_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)


async def source_account_item(message: types.Message):
    await message.answer(ACCOUNT_ITEM, reply_markup=show_item_accounts_keyboard(message.text))


async def account_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    current_user = UsersRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # print(callback.data)
            # main ======================
            if HIDE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_account(HIDE_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif OPEN_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_account(OPEN_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif DELETE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().delete_account(callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_DELTED)
                else:
                    await callback.message.answer(FAIL_DELTED)
            else:
                account_info = AccountsRepository().get_account(callback.data)
                await callback.message.answer(formatted_output_account(account_info),
                                              reply_markup=manag_account_keyboard(callback.data))
            # ============================
        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def cards_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    current_user = UsersRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # print(callback.data)
            # main ======================
            if HIDE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_card(HIDE_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif OPEN_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_card(OPEN_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif DELETE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().delete_card(callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_DELTED)
                else:
                    await callback.message.answer(FAIL_DELTED)
            else:
                account_info = AccountsRepository().get_card(callback.data)
                await callback.message.answer(formatted_output_card(account_info),
                                              reply_markup=manag_card_keyboard(callback.data))
            # ============================
        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def cabinets_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    current_user = UsersRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # print(callback.data)
            # main ======================
            if HIDE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_cabinet(HIDE_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif OPEN_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_cabinet(OPEN_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif DELETE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().delete_cabinet(callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_DELTED)
                else:
                    await callback.message.answer(FAIL_DELTED)
            else:
                account_info = AccountsRepository().get_cabinet(callback.data)
                await callback.message.answer(formatted_output_cabinet(account_info),
                                              reply_markup=manag_cabinet_keyboard(callback.data))
            # ============================
        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def verifications_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    current_user = UsersRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # print(callback.data)
            # main ======================
            if HIDE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_verification(HIDE_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif OPEN_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().exchange_visibility_verification(OPEN_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif DELETE_STATE in callback.data and current_user['sub_position'] != SUB_POSITION_CREO:
                result = AccountsRepository().delete_verification(callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_DELTED)
                else:
                    await callback.message.answer(FAIL_DELTED)
            else:
                account_info = AccountsRepository().get_verification(callback.data)
                await callback.message.answer(formatted_output_verification(account_info),
                                              reply_markup=manag_verification_keyboard(callback.data))
            # ============================
        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())
