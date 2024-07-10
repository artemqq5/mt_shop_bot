from data.database import MyDataBase


class OrderRepository(MyDataBase):

    def get_orders(self, status=None, type_account=None):
        return self._get_orders_sql(status, type_account)  # get orders by type and status, by default all types of orders

    def get_user_orders(self, status, user_id, type_account):
        return self._get_user_orders_sql(status, user_id, type_account)  # get orders by type, status and client id, by default all types of orders

    def get_order(self, id_order):
        return self._get_order_sql(id_order)

    def exchange_status_order(self, id_order, new_status):
        return self._exchange_status_order_sql(id_order, new_status)

    def update_creo_order_trello(self, trello_id, trello_url, id_order):
        return self._update_creo_order_trello_sql(trello_id, trello_url, id_order)

    def add_account_order(self, name, desc, type_account, geo, count, price, id_user, desc_from_user):
        return self._add_account_order_sql(name, desc, type_account, geo, count, price, id_user, desc_from_user)

    def get_account_order(self, id_order):
        return self._get_account_order_sql(id_order)

    def get_orders_by_user_id(self, user_id):
        return self._get_orders_by_user_id_sql(user_id)


