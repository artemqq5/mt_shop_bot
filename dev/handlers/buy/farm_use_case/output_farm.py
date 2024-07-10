from dev.constants.accounts_constants import INPUT_PRICE_OF_ITEM


def formatted_output_account(list_data) -> str:
    account_message = ""

    account_message += f"<b>{list_data['name']}</b>\n\n"
    account_message += f"<b>{list_data['desc']}</b>\n\n"
    account_message += f"{INPUT_PRICE_OF_ITEM}<b>{list_data['price']}</b>\n\n"
    account_message += f"Type: <b>{list_data['type']}</b>\n\n"
    account_message += f"Geo: <b>{list_data['geo']}</b>\n\n\n"
    account_message += f"Visibility: <b>{list_data['visibility']}</b>\n\n"

    return account_message


def formatted_output_card(list_data) -> str:
    account_message = ""

    account_message += f"<b>{list_data['name']}</b>\n\n"
    account_message += f"<b>{list_data['desc']}</b>\n\n"
    account_message += f"{INPUT_PRICE_OF_ITEM}<b>{list_data['price']}</b>\n\n"
    account_message += f"Visibility: <b>{list_data['visibility']}</b>\n\n"

    return account_message


def formatted_output_verification(list_data) -> str:
    account_message = ""

    account_message += f"<b>{list_data['name']}</b>\n\n"
    account_message += f"<b>{list_data['desc']}</b>\n\n"
    account_message += f"{INPUT_PRICE_OF_ITEM}<b>{list_data['price']}</b>\n\n"
    account_message += f"Geo: <b>{list_data['geo']}</b>\n\n\n"
    account_message += f"Visibility: <b>{list_data['visibility']}</b>\n\n"

    return account_message


def formatted_output_cabinet(list_data) -> str:
    account_message = ""

    account_message += f"<b>{list_data['name']}</b>\n\n"
    account_message += f"<b>{list_data['desc']}</b>\n\n"
    account_message += f"{INPUT_PRICE_OF_ITEM}<b>{list_data['price']}</b>\n\n"
    account_message += f"Visibility: <b>{list_data['visibility']}</b>\n\n"

    return account_message
