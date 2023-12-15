from data.constants.admin_constants import CREO_TYPE, ACCOUNT_TYPE
from data.constants.agency_accounts_constants import AGENCY_TYPE
from data.constants.apps_constants import APPS_TYPE
from data.repository.orders import OrdersRepository


def general_statistic_format(message) -> str:
    final_message = ""

    creo_orders = 0
    accounts_orders = 0
    # apps_orders = 0
    # agency_accounts_orders = 0

    orders = OrdersRepository().get_orders_by_user_id(message.chat.id)
    for order in orders:
        if order['type'] == CREO_TYPE:
            creo_orders += 1
        elif order['type'] == ACCOUNT_TYPE:
            accounts_orders += 1
        # elif order['type'] == AGENCY_TYPE:
        #     agency_accounts_orders += 1
        # elif order['type'] == APPS_TYPE:
        #     apps_orders += 1

    final_message += f"<b>Общая статистика</b>\n\n"
    final_message += f"<b>Всего заказов:</b> {len(orders)}\n"
    final_message += f"<b>Крео:</b> {creo_orders}\n"
    final_message += f"<b>Аккаунты:</b> {accounts_orders}\n"
    # final_message += f"<b>Приложения:</b> {apps_orders}\n"
    # final_message += f"<b>Агентские аккаунты:</b> {agency_accounts_orders}\n"

    return final_message
