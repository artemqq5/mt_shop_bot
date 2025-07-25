import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.ban.kb_ban_system import BanSystemBack


class BanListNavigation(CallbackData, prefix="BanListNavigation"):
    page: int


def kb_ban_list_nav(ban_users, current_page: int = 1):
    inline_kb = []

    total_pages = math.ceil(len(ban_users) / 4)

    nav = []
    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=BanListNavigation(page=current_page - 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data="None"
        ))

    nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data=BanListNavigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)
    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=BanSystemBack().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


def text_ban_list(ban_users, i18n, current_page: int = 1):

    start_index = (current_page - 1) * 4
    end_index = min(start_index + 4, len(ban_users))

    message = ""

    # load from db
    for i in range(start_index, end_index):
        message += i18n.ADMIN.BAN_LIST_TEMPLATE(
            username=ban_users[i]['username'],
            id=ban_users[i]['user_id'],
            lang=str(ban_users[i]['lang'])
        )
        message += "\n\n"

    if not len(message):
        message = i18n.ADMIN.NO_BANNED_USERS()

    return message
