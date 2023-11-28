import uuid

import pymysql
from config.cfg import *
from data.constants.admin_constants import CREO_TYPE, ACCOUNT_TYPE


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

    def get_orders_sql(self, status):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    if status is not None:
                        _command = f'''SELECT * FROM `orders` WHERE `status` = %s;'''
                        cursor.execute(_command, (status,))
                    else:
                        _command = f'''SELECT * FROM `orders`;'''
                        cursor.execute(_command)
                connection.commit()
                return cursor.fetchall()
        except Exception as e:
            print(f"get_orders_sql({status}): {e}")
            return None

    def get_order_sql(self, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `orders` WHERE `id_order` = %s;'''
                    cursor.execute(_command, (id_order,))
                connection.commit()
                return cursor.fetchall()[0]
        except Exception as e:
            print(f"get_order_sql: {e}")
            return None

    def get_creo_sql(self, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `creo_orders` WHERE `id_order` = %s;'''
                    cursor.execute(_command, (id_order,))
                connection.commit()
                return cursor.fetchall()[0]
        except Exception as e:
            print(f"get_creo_sql: {e}")
            return None

    def add_creo_sql(self, format_creo, type_creo, category, description, id_user, geo=None, language=None,
                     currency=None, format_res=None, offer=None, voice=None, source=None, deadline=None):
        try:
            id_order = str(uuid.uuid4())

            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''INSERT INTO `creo_orders` (
                        `id_order`, `format`, `type`, `category`, `geo`,  `language`, `currency`, `format_res`,
                         `offer`, `voice`, `source`, `description`, `deadline`
                     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
                    cursor.execute(_command, (
                        id_order, format_creo, type_creo, category, geo, language, currency, format_res,
                        offer, voice, source, description, deadline
                    ))
                connection.commit()

                with connection.cursor() as cursor:
                    _command = f'''INSERT INTO `orders` (`id_user`, `type`, `id_order`) VALUES (%s, %s, %s);'''
                    cursor.execute(_command, (id_user, CREO_TYPE, id_order))
                connection.commit()

            return True

        except Exception as e:
            print(f"add_creo_sql: {e}")
            return None

    def exchange_status_order_sql(self, id_order, new_status):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''UPDATE `orders` SET `status` = %s WHERE `id_order` = %s;'''
                    cursor.execute(_command, (new_status, id_order))
                connection.commit()
            return True
        except Exception as e:
            print(f"get_creo_sql: {e}")
            return None

    def add_account_sql(self, type_account, name, desc, geo, count, price):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''INSERT INTO `accounts` (`name`, `desc`, `geo`, `type`, `count`, `price`) VALUES (%s, %s, %s, %s, %s, %s);'''
                    cursor.execute(_command, (name, desc, geo, type_account, count, price))
                connection.commit()
            return True
        except Exception as e:
            print(f"add_account_sql: {e}")
            return None

    def get_accounts_sql(self):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `accounts`;'''
                    cursor.execute(_command)
                connection.commit()
            return cursor.fetchall()
        except Exception as e:
            print(f"get_accounts_sql: {e}")
            return None

    def get_account_sql(self, id_account):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `accounts` WHERE `id` = %s;'''
                    cursor.execute(_command, id_account)
                connection.commit()
            return cursor.fetchall()[0]
        except Exception as e:
            print(f"get_account_sql: {e}")
            return None

    def add_order_account_sql(self, name, desc, type_account, geo, count, price, id_user, desc_from_user):
        try:
            id_order = str(uuid.uuid4())

            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''INSERT INTO `account_orders` (
                               `id_order`, `name`, `desc`, `type`, `geo`, `count`, `price`, `desc_from_user`
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
                    cursor.execute(_command, (id_order, name, desc, type_account, geo, count, price, desc_from_user))
                connection.commit()

                with connection.cursor() as cursor:
                    _command = f'''INSERT INTO `orders` (`id_user`, `type`, `id_order`) VALUES (%s, %s, %s);'''
                    cursor.execute(_command, (id_user, ACCOUNT_TYPE, id_order))
                connection.commit()

            return True

        except Exception as e:
            print(f"add_order_account_sql: {e}")
            return None

    def get_account_order_sql(self, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `account_orders` WHERE `id_order` = %s;'''
                    cursor.execute(_command, id_order)
                connection.commit()
            return cursor.fetchall()[0]
        except Exception as e:
            print(f"get_account_order_sql: {e}")
            return None

    def get_users_sql(self, position=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    if position is not None:
                        _command = f'''SELECT * FROM `users` WHERE `position` = %s;'''
                        cursor.execute(_command, (position,))
                    else:
                        _command = f'''SELECT * FROM `users`;'''
                        cursor.execute(_command)
                connection.commit()
            return cursor.fetchall()
        except Exception as e:
            print(f"get_users_sql: {e}")
            return None

    def exchange_visibility_account_sql(self, visibility, id_account):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''UPDATE `accounts` SET `visibility` = %s WHERE `id` = %s;'''
                    cursor.execute(_command, (visibility, id_account))
                connection.commit()
            return True
        except Exception as e:
            print(f"exchange_visibility_account_sql: {e}")
            return None
