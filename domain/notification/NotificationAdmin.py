from datetime import datetime

from aiogram import Bot
from aiogram_i18n import I18nContext

from data.repository.invoices import InvoiceRepository
from data.repository.items import ItemRepository
from data.repository.orders import OrderRepository
from data.repository.users import UserRepository


class NotificationAdmin:

    @staticmethod
    async def user_activate_bot(user_id: int, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)

        for admin in admins:
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.NEW_USER(
                            username=user['username'],
                            user_id=user['user_id'],
                            join_at=user['join_at']
                        )
                    )
                    counter += 1
            except Exception as e:
                print(f"user_activate_bot: {e}")

        print(f"messaging user_activate_bot {counter}/{len(admins)}")

    @staticmethod
    async def new_order(identify, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        order = OrderRepository().order_by_identify(identify)
        user = UserRepository().user(order['user_id'])

        for admin in admins:
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    username = f"@{user['username']}" if user['username'] else i18n.ADMIN.USERNAME_HAVNT()
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.NEW_ORDER(
                            id=order['id'],
                            date=order['date'],
                            name=order['item_title'],
                            category=order['category'],
                            count=order['count'],
                            price=order['total_cost'],
                            desc=order['desc'],
                            user_id=user['user_id'],
                            username=username
                        )
                    )
                    counter += 1

            except Exception as e:
                print(f"new_order: {e}")

        print(f"messaging new_order {counter}/{len(admins)}")

    @staticmethod
    async def balance_insufficient(data, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        user = UserRepository().user(data['user_id'])

        difference = data['total_cost']-user['balance']

        for admin in admins:
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    username = f"@{user['username']}" if user['username'] else i18n.ADMIN.USERNAME_HAVNT()

                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.BALANCE_INSUFFICIENT(
                            balance=user['balance'],
                            invoice=data['total_cost'],
                            difference=difference,
                            date=datetime.now(),
                            name=data['item']['title'],
                            category=data['item']['category'],
                            count=data['count'],
                            desc=data['desc'],
                            user_id=user['user_id'],
                            username=username
                        )
                    )
                    counter += 1

            except Exception as e:
                print(f"balance_insufficient: {e}")

        print(f"messaging balance_insufficient {counter}/{len(admins)}")

    @staticmethod
    async def invoice_init(external_id, bot: Bot, i18n: I18nContext):
        counter = 0
        admins = UserRepository().admins()
        invoice = InvoiceRepository().invoice(external_id)
        user = UserRepository().user(invoice['user_id'])

        for admin in admins:
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    username = f"@{user['username']}" if user['username'] else i18n.ADMIN.USERNAME_HAVNT()

                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.INVOICE_INIT(
                            balance=user['balance'],
                            value=invoice['value'],
                            number=str(int(invoice['number'])),
                            id=invoice['external_id'],
                            date=datetime.now(),
                            user_id=user['user_id'],
                            username=username
                        )
                    )
                    counter += 1
            except Exception as e:
                print(f"invoice_init: {e}")

        print(f"messaging invoice_init {counter}/{len(admins)}")

    # @staticmethod
    # async def invoice_completed(external_id, bot: Bot, i18n: I18nContext):
    #     counter = 0
    #     admins = UserRepository().admins()
    #     invoice = InvoiceRepository().invoice(external_id)
    #     user = UserRepository().user(invoice['user_id'])
    #
    #     username = f"@{user['username']}" if user['username'] else i18n.ADMIN.USERNAME_HAVNT()
    #
    #     try:
    #         for admin in admins:
    #             with i18n.use_locale(admin.get('lang', 'en')):
    #                 await bot.send_message(
    #                     chat_id=admin['user_id'],
    #                     text=i18n.NOTIFICATION.INVOICE_COMPLETED(
    #                         balance=user['balance'],
    #                         value=invoice['value'],
    #                         number=invoice['number'],
    #                         id=invoice['external_id'],
    #                         date=datetime.now(),
    #                         user_id=user['user_id'],
    #                         username=username
    #                     )
    #                 )
    #                 counter += 1
    #
    #     except Exception as e:
    #         print(f"invoice_init: {e}")
    #
    #     print(f"messaging invoice_init {counter}/{len(admins)}")

