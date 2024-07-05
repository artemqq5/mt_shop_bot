from data.constants.admin_constants import SUCCSESFULL_ADDED, FAIL_ADDED
from data.repository.accounts import AccountsRepository
from keyboard.menu.menu_keyboard import main_keyboard


async def add_account_case(data, message):
    if data is not None:
        try:
            result = AccountsRepository().add_account(
                name=data['name'],
                desc=data['desc'],
                geo=data['geo'],
                type_account=data['type'],
                price=data['price'],
            )
        except Exception as e:
            print(f"add_account_case: {e}")
            result = None

        if result:
            await message.answer(SUCCSESFULL_ADDED, reply_markup=main_keyboard(message))
        else:
            await message.answer(FAIL_ADDED, reply_markup=main_keyboard(message))


async def add_cabinet_case(data, message):
    if data is not None:
        try:
            result = AccountsRepository().add_cabinet(
                name=data['name'],
                desc=data['desc'],
                price=data['price'],
            )
        except Exception as e:
            print(f"add_cabinet_case: {e}")
            result = None

        if result:
            await message.answer(SUCCSESFULL_ADDED, reply_markup=main_keyboard(message))
        else:
            await message.answer(FAIL_ADDED, reply_markup=main_keyboard(message))


async def add_card_case(data, message):
    if data is not None:
        try:
            result = AccountsRepository().add_card(
                name=data['name'],
                desc=data['desc'],
                price=data['price'],
            )
        except Exception as e:
            print(f"add_card_case: {e}")
            result = None

        if result:
            await message.answer(SUCCSESFULL_ADDED, reply_markup=main_keyboard(message))
        else:
            await message.answer(FAIL_ADDED, reply_markup=main_keyboard(message))


async def add_verification_case(data, message):
    if data is not None:
        try:
            result = AccountsRepository().add_verification(
                name=data['name'],
                geo=data['geo'],
                desc=data['desc'],
                price=data['price'],
            )
        except Exception as e:
            print(f"add_verification_case: {e}")
            result = None

        if result:
            await message.answer(SUCCSESFULL_ADDED, reply_markup=main_keyboard(message))
        else:
            await message.answer(FAIL_ADDED, reply_markup=main_keyboard(message))

