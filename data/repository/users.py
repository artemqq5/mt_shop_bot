from data.database import MyDataBase


class UserRepository(MyDataBase):

    def add_user(self, telegram_id, name, time):
        return self._add_user_sql(telegram_id, name, time)

    def get_user(self, telegram_id):
        return self._get_user_sql(telegram_id)

    def get_users(self, position):  # get users by position or All by default
        return self._get_users_sql(position)

    def ban_user_by_id(self, user_id):
        COMMAND_ = "UPDATE `users` SET `banned` = 1 WHERE `id` = %s;"
        return self._update(COMMAND_, (user_id,))

    def ban_user_by_username(self, username):
        COMMAND_ = "UPDATE `users` SET `banned` = 1 WHERE `name` = %s;"
        return self._update(COMMAND_, (username,))

    def update_ban_message_by_id(self, user_id, user_ban_message):
        COMMAND_ = "UPDATE `users` SET `banned_message` = %s WHERE `id` = %s;"
        return self._update(COMMAND_, (user_ban_message, user_id))

    def update_ban_message_by_username(self, username, user_ban_message):
        COMMAND_ = "UPDATE `users` SET `banned_message` = %s WHERE `name` = %s;"
        return self._update(COMMAND_, (user_ban_message, username))

    def get_all_banned_users(self):
        COMMAND_ = "SELECT * FROM `users` WHERE `banned` = 1;"
        return self._select(query=COMMAND_)
