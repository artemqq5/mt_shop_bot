from data.database import MyDataBase


class UsersRepository(MyDataBase):

    def add_user(self, telegram_id, name, time):
        return self._add_user_sql(telegram_id, name, time)

    def get_user(self, telegram_id):
        return self._get_user_sql(telegram_id)

    def get_users(self, position):  # get users by position or All by default
        return self._get_users_sql(position)
