from data.constants.accounts_constants import INPUT_PRICE_OF_ACCOUNT


def formatted_output_account(list_data) -> str:
    account_message = ""

    account_message += f"<b>{list_data['name']}</b>\n\n"
    account_message += f"<b>{list_data['desc']}</b>\n\n"
    account_message += f"{INPUT_PRICE_OF_ACCOUNT}<b>{list_data['price']}</b>\n\n"
    account_message += f"Type: <b>{list_data['type']}</b>\n\n"
    account_message += f"Geo: <b>{list_data['geo']}</b>\n\n"

    return account_message
