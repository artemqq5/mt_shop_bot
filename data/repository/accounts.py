from data.database import MyDataBase


class AccountsRepository(MyDataBase):

    def add_account(self, type_account, name, desc, geo, count, price):
        return self.add_account_sql(type_account, name, desc, geo, count, price)

    def get_accounts(self, source=None):
        return self.get_accounts_sql(source)

    def get_account(self, id_account):
        return self.get_account_sql(id_account)

    def exchange_visibility_account(self, visibility, id_account):
        return self.exchange_visibility_account_sql(visibility, id_account)
    