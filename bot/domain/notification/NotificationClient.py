from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError

from bot.data.repository.users import UserRepository
from bot.domain.handlers.admin.messaging.MessagingTools import MessagingTools


class NotificationClient:

    @staticmethod
    async def push_all_clients(data: dict[str], bot: Bot, i18n):
        counter = 0
        block = 0
        other = 0

        clients = UserRepository().clients()

        for client in clients:
            try:
                await MessagingTools.preview_message_send(data, bot, client["user_id"])
                counter += 1
            except TelegramForbiddenError as e:
                block += 1
                print(f"client({client}) | push_all_clients: {e} ")
            except Exception as e:
                other += 1
                print(f"client({client}) | push_all_clients: {e} ")

        print(f"messaging: {counter}/{len(clients)}\nblock:{block}\nother:{other}")
        return i18n.ADMIN.RESULT_NOTIFICATION(send=counter, users=len(clients), block=block, other=other)

    @staticmethod
    async def push_individual_client(data: dict[str], bot: Bot, user_id, i18n):
        counter = 0
        block = 0
        other = 0

        client = UserRepository().user(user_id)

        try:
            await MessagingTools.preview_message_send(data, bot, client["user_id"])
            counter += 1
        except TelegramForbiddenError as e:
            block += 1
            print(f"client({client}) | push_all_clients: {e} ")
        except Exception as e:
            other += 1
            print(f"client({client}) | push_all_clients: {e} ")

        print(f"messaging: {counter}/{1}\nblock:{block}\nother:{other}")
        return i18n.ADMIN.RESULT_NOTIFICATION(send=counter, users=1, block=block, other=other)
