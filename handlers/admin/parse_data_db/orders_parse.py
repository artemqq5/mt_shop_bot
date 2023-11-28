from data.constants.admin_constants import ORDER_STATUS_LIST, TRELLO_, REVIEW, CREO_TYPE
from data.repository import MyRepository


def format_view_order(order_params: dict[str, str], user_contact) -> str:
    formated_order = ""
    for param in order_params:
        formated_order += f"<b>{param}:</b> {order_params[param]}\n"

    formated_order += "\n"
    formated_order += f"<b>username:</b> @{user_contact['name']}\n"
    formated_order += f"<b>telegram id:</b> {user_contact['id']}\n"

    return formated_order


def all_order_list_id() -> list[str]:
    list_id = []

    for list_order in MyRepository().get_orders(status=None):
        list_id.append(list_order['id_order'])

    return list_id


def all_order_status_change() -> list[str]:
    list_id = []

    for list_order in MyRepository().get_orders(status=None):
        for status in ORDER_STATUS_LIST:
            list_id.append(f"{ORDER_STATUS_LIST[status]}_{list_order['id_order']}")

    return list_id


def order_send_trello_list() -> list[str]:
    list_id = []

    for list_order in MyRepository().get_orders(status=REVIEW):
        if list_order['type'] == CREO_TYPE:
            list_id.append(f"{TRELLO_}_{list_order['id_order']}")

    return list_id
