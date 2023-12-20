import uuid

import pymysql
from config.cfg import *
from data.constants.admin_constants import *


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

    def _add_user_sql(self, telegram_id, name):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''INSERT INTO `users` (`id`, `name`) VALUES (%s, %s);'''
                    cursor.execute(_command, (telegram_id, name))
                connection.commit()
        except Exception as e:
            print(f"add_user_sql: {e}")

    def _get_user_sql(self, telegram_id):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''SELECT * FROM `users` WHERE `id` = %s;'''
                    cursor.execute(_command, (telegram_id,))
                return cursor.fetchone()
        except Exception as e:
            print(f"get_user_sql: {e}")
            return None

    def _get_orders_sql(self, status=None, type_account=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    if type_account is None:
                        if status is None:
                            _command = '''SELECT * FROM `orders` WHERE `type` IN (%s, %s);'''
                            cursor.execute(_command, (CREO_TYPE, ACCOUNT_TYPE))
                        else:
                            _command = '''SELECT * FROM `orders` WHERE `status` = %s AND `type` IN (%s, %s);'''
                            cursor.execute(_command, (status, CREO_TYPE, ACCOUNT_TYPE))
                    else:
                        if status is None:
                            _command = '''SELECT * FROM `orders` WHERE `type` = %s;'''
                            cursor.execute(_command, type_account)
                        else:
                            _command = '''SELECT * FROM `orders` WHERE `status` = %s AND `type` = %s;'''
                            cursor.execute(_command, (status, type_account))
                return cursor.fetchall()
        except Exception as e:
            print(f"get_orders_sql({status}): {e}")
            return None

    def _get_user_orders_sql(self, status, user_id, type_account):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    if status == ACTIVE:
                        _command = '''SELECT * FROM `orders` WHERE `status` IN (%s, %s, %s) AND `type` = %s AND `id_user` = %s;'''
                        cursor.execute(_command, (ACTIVE, REVIEW, ON_APPROVE, type_account, user_id))
                    else:
                        _command = '''SELECT * FROM `orders` WHERE `status` IN (%s, %s) AND `type` = %s AND `id_user` = %s;'''
                        cursor.execute(_command, (COMPLETED, CANCELED, type_account, user_id))
                return cursor.fetchall()
        except Exception as e:
            print(f"_get_user_orders_sql({status}): {e}")
            return None

    def _get_order_sql(self, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''SELECT * FROM `orders` WHERE `id_order` = %s;'''
                    cursor.execute(_command, (id_order,))
                return cursor.fetchone()
        except Exception as e:
            print(f"get_order_sql: {e}")
            return None

    def _get_creo_sql(self, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''SELECT * FROM `creo_orders` WHERE `id_order` = %s;'''
                    cursor.execute(_command, (id_order,))
                return cursor.fetchone()
        except Exception as e:
            print(f"get_creo_sql: {e}")
            return None

    def _add_creo_sql(self, format_creo, type_creo, category, description, id_user, geo=None, language=None,
                      currency=None, format_res=None, offer=None, voice=None, source=None, deadline=None, count=1,
                      sub_desc=None):
        try:
            id_order = str(uuid.uuid4())

            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''INSERT INTO `creo_orders` (
                        `id_order`, `format`, `type`, `category`, `geo`,  `language`, `currency`, `format_res`,
                         `offer`, `voice`, `source`, `description`, `deadline`, `count`, `sub_description`
                     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
                    cursor.execute(_command, (
                        id_order, format_creo, type_creo, category, geo, language, currency, format_res,
                        offer, voice, source, description, deadline, count, sub_desc
                    ))
                connection.commit()

                with connection.cursor() as cursor:
                    _command = '''INSERT INTO `orders` (`id_user`, `type`, `id_order`) VALUES (%s, %s, %s);'''
                    cursor.execute(_command, (id_user, CREO_TYPE, id_order))
                connection.commit()

            return id_order

        except Exception as e:
            print(f"add_creo_sql: {e}")
            return None

    def _exchange_status_order_sql(self, id_order, new_status):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = "UPDATE `orders` SET `status` = %s WHERE `id_order` = %s;"
                    cursor.execute(_command, (new_status, id_order))
                connection.commit()
            return True
        except Exception as e:
            print(f"exchange_status_order_sql: {e}")
            return None

    def _add_account_sql(self, type_account, name, desc, geo, count, price):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''INSERT INTO `accounts` (`name`, `desc`, `geo`, `type`, `count`, `price`) VALUES (%s, %s, %s, %s, %s, %s);'''
                    cursor.execute(_command, (name, desc, geo, type_account, count, price))
                connection.commit()
            return True
        except Exception as e:
            print(f"add_account_sql: {e}")
            return None

    def _get_accounts_sql(self, source=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    if source is None:
                        _command = '''SELECT * FROM `accounts`;'''
                        cursor.execute(_command)
                    else:
                        _command = '''SELECT * FROM `accounts` WHERE `type` = %s;'''
                        cursor.execute(_command, source)
            return cursor.fetchall()
        except Exception as e:
            print(f"get_accounts_sql: {e}")
            return None

    def _get_account_sql(self, id_account):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''SELECT * FROM `accounts` WHERE `id` = %s;'''
                    cursor.execute(_command, id_account)
            return cursor.fetchone()
        except Exception as e:
            print(f"get_account_sql: {e}")
            return None

    def _add_account_order_sql(self, name, desc, type_account, geo, count, price, id_user, desc_from_user):
        try:
            id_order = str(uuid.uuid4())

            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''INSERT INTO `account_orders` (
                               `id_order`, `name`, `desc`, `type`, `geo`, `count`, `price`, `desc_from_user`
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
                    cursor.execute(_command, (id_order, name, desc, type_account, geo, count, price, desc_from_user))
                connection.commit()

                with connection.cursor() as cursor:
                    _command = '''INSERT INTO `orders` (`id_user`, `type`, `id_order`) VALUES (%s, %s, %s);'''
                    cursor.execute(_command, (id_user, ACCOUNT_TYPE, id_order))
                connection.commit()

            return id_order

        except Exception as e:
            print(f"add_order_account_sql: {e}")
            return None

    def _get_account_order_sql(self, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''SELECT * FROM `account_orders` WHERE `id_order` = %s;'''
                    cursor.execute(_command, id_order)
            return cursor.fetchone()
        except Exception as e:
            print(f"get_account_order_sql: {e}")
            return None

    def _get_users_sql(self, position=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    if position is not None:
                        _command = '''SELECT * FROM `users` WHERE `position` = %s;'''
                        cursor.execute(_command, (position,))
                    else:
                        _command = '''SELECT * FROM `users`;'''
                        cursor.execute(_command)
            return cursor.fetchall()
        except Exception as e:
            print(f"get_users_sql: {e}")
            return None

    def _exchange_visibility_account_sql(self, visibility, id_account):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''UPDATE `accounts` SET `visibility` = %s WHERE `id` = %s;'''
                    cursor.execute(_command, (visibility, id_account))
                connection.commit()
            return True
        except Exception as e:
            print(f"exchange_visibility_account_sql: {e}")
            return None

    def _update_creo_order_trello_sql(self, trello_id, trello_url, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''UPDATE `creo_orders` SET `trello_id` = %s, `trello_url` = %s WHERE `id_order` = %s;'''
                    cursor.execute(_command, (trello_id, trello_url, id_order))
                connection.commit()
            return True
        except Exception as e:
            print(f"update_creo_order_trello: {e}")
            return None

    def _get_orders_by_user_id_sql(self, user_id):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''SELECT * FROM `orders` WHERE `id_user` = %s;'''
                    cursor.execute(_command, user_id)
            return cursor.fetchall()
        except Exception as e:
            print(f"_get_orders_by_user_id_sql: {e}")
            return None

    def _update_dropbox_link(self, id_order, link):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''UPDATE `creo_orders` SET `dropbox` = %s WHERE `id_order` = %s;'''
                    cursor.execute(_command, (link, id_order))
                connection.commit()
            return True
        except Exception as e:
            print(f"_update_dropbox_link: {e}")
            return None

    def _delete_account(self, account_id):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = '''DELETE FROM `accounts` WHERE `id` = %s;'''
                    cursor.execute(_command, account_id)
                connection.commit()
            return True
        except Exception as e:
            print(f"_delete_account: {e}")
            return None
