import pymysql
from config.cfg import *


class MyDataBase:

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            db="mt_shop_db",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def add_user_sql(self, telegram_id, name):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''INSERT INTO `users` (`id`, `name`) VALUES (%s, %s);'''
                    cursor.execute(_command, (telegram_id, name))
                connection.commit()
        except Exception as e:
            print(f"add_user_sql: {e}")

    def get_user_sql(self, telegram_id):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `users` WHERE `id` = %s;'''
                    cursor.execute(_command, (telegram_id,))
                connection.commit()
                return cursor.fetchall()[0]
        except Exception as e:
            print(f"get_user_sql: {e}")
            return None
