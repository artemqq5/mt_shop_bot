from data.database import MyDataBase


class AccountsRepository(MyDataBase):

    def delete_account(self, account_id):
        return self._delete_account_sql(account_id)

    def delete_card(self, account_id):
        return self._delete_card_sql(account_id)

    def delete_cabinet(self, account_id):
        return self._delete_cabinet_sql(account_id)

    def delete_verification(self, account_id):
        return self._delete_verification_sql(account_id)

    def add_account(self, type_account, name, desc, geo, price):
        return self._add_account_sql(type_account, name, desc, geo, price)

    def add_cabinet(self, name, desc, price):
        return self._add_cabinet_sql(name, desc, price)

    def add_card(self, name, desc, price):
        return self._add_card_sql(name, desc, price)

    def add_verification(self, name, geo, desc, price):
        return self._add_verification_sql(name, geo, desc, price)

    def get_accounts(self, source=None):
        return self._get_accounts_sql(source)

    def get_cards(self):
        return self._get_cards_sql()

    def get_cabinets(self):
        return self._get_cabinets_sql()

    def get_verifications(self):
        return self._get_verifications_sql()

    def get_account(self, id_account):
        return self._get_account_sql(id_account)

    def get_card(self, id_account):
        return self._get_card_sql(id_account)

    def get_cabinet(self, id_account):
        return self._get_cabinet_sql(id_account)

    def get_verification(self, id_account):
        return self._get_verification_sql(id_account)

    def exchange_visibility_account(self, visibility, id_account):
        return self._exchange_visibility_account_sql(visibility, id_account)

    def exchange_visibility_card(self, visibility, id_account):
        return self._exchange_visibility_card_sql(visibility, id_account)

    def exchange_visibility_cabinet(self, visibility, id_account):
        return self._exchange_visibility_cabinet_sql(visibility, id_account)

    def exchange_visibility_verification(self, visibility, id_account):
        return self._exchange_visibility_verification_sql(visibility, id_account)
