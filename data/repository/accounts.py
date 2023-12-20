from data.database import MyDataBase


class AccountsRepository(MyDataBase):

    def delete_account(self, account_id):
        return self._delete_account(account_id)

    def add_account(self, type_account, name, desc, geo, count, price):
        return self._add_account_sql(type_account, name, desc, geo, count, price)

    def get_accounts(self, source=None):
        return self._get_accounts_sql(source)

    def get_account(self, id_account):
        return self._get_account_sql(id_account)

    def exchange_visibility_account(self, visibility, id_account):
        return self._exchange_visibility_account_sql(visibility, id_account)
    