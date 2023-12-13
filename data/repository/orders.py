from data.constants.admin_constants import CREO_TYPE, ACCOUNT_TYPE
from data.database import MyDataBase


class OrdersRepository(MyDataBase):

    def get_orders(self, status, type_account=(CREO_TYPE, ACCOUNT_TYPE)):
        return self.get_orders_sql(status, type_account)

    def get_order(self, id_order):
        return self.get_order_sql(id_order)

    def exchange_status_order(self, id_order, new_status):
        return self.exchange_status_order_sql(id_order, new_status)

    def update_creo_order_trello(self, trello_id, trello_url, id_order):
        return self.update_creo_order_trello_sql(trello_id, trello_url, id_order)

    def add_order_account(self, name, desc, type_account, geo, count, price, id_user, desc_from_user):
        return self.add_order_account_sql(name, desc, type_account, geo, count, price, id_user, desc_from_user)

    def get_account_order(self, id_order):
        return self.get_account_order_sql(id_order)
    