from data.database import MyDataBase


class MyRepository(MyDataBase):

    def add_user(self, telegram_id, name):
        self.add_user_sql(telegram_id, name)

    def get_user(self, telegram_id):
        return self.get_user_sql(telegram_id)

    def get_orders(self, status):
        return self.get_orders_sql(status)

    def get_order(self, id_order):
        return self.get_order_sql(id_order)

    def get_creo(self, id_order):
        return self.get_creo_sql(id_order)

    def add_creo(
            self, format_creo, type_creo, category, description, id_user, geo, language, currency, format_res,
            offer, voice, source, deadline
    ):
        return self.add_creo_sql(
            format_creo, type_creo, category, description, id_user, geo, language, currency, format_res, offer,
            voice, source, deadline
        )

    def exchange_status_order(self, id_order, new_status):
        return self.exchange_status_order_sql(id_order, new_status)

    def add_account(self, type_account, name, desc, geo, count, price):
        return self.add_account_sql(type_account, name, desc, geo, count, price)

    def get_accounts(self):
        return self.get_accounts_sql()

    def get_account(self, id_account):
        return self.get_account_sql(id_account)

    def add_order_account(self, name, desc, type_account, geo, count, price, id_user, desc_from_user):
        return self.add_order_account_sql(name, desc, type_account, geo, count, price, id_user, desc_from_user)

    def get_account_order(self, id_order):
        return self.get_account_order_sql(id_order)
