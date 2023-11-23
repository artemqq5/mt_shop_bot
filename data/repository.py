from data.database import MyDataBase


class MyRepository(MyDataBase):

    def add_user(self, telegram_id, name):
        self.add_user_sql(telegram_id, name)

    def get_user(self, telegram_id):
        return self.get_user_sql(telegram_id)
