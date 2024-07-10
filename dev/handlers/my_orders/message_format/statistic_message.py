from dev.constants.admin_constants import CREO_TYPE, ACCOUNT_TYPE_FB, ACCOUNT_TYPE_GOOGLE, CARD_TYPE, CABINET_TYPE, \
    VERIFICATION_TYPE
from dev.constants.orders import OrdersRepository


def general_statistic_format(message) -> str:
    final_message = ""

    creo_orders = 0
    accounts_orders = 0
    cards_orders = 0
    cabinets_orders = 0
    verification_orders = 0

    orders = OrdersRepository().get_orders_by_user_id(message.chat.id)
    for order in orders:
        if order['type'] == CREO_TYPE:
            creo_orders += 1
        elif order['type'] in (ACCOUNT_TYPE_FB, ACCOUNT_TYPE_GOOGLE):
            accounts_orders += 1
        elif order['type'] == CARD_TYPE:
            cards_orders += 1
        elif order['type'] == CABINET_TYPE:
            cabinets_orders += 1
        elif order['type'] == VERIFICATION_TYPE:
            verification_orders += 1

    final_message += f"<b>Общая статистика</b>\n\n"
    final_message += f"<b>Всего заказов:</b> {len(orders)}\n"
    final_message += f"<b>Крео:</b> {creo_orders}\n"
    final_message += f"<b>Аккаунты:</b> {accounts_orders}\n"
    final_message += f"<b>Карты ПБ:</b> {cards_orders}\n"
    final_message += f"<b>Личные кабинеты Банков:</b> {cabinets_orders}\n"
    final_message += f"<b>Верификация:</b> {verification_orders}\n"

    return final_message
