import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.repository.items import ItemRepository


class AvailabilityNavigation(CallbackData, prefix="AvailabilityNavigation"):
    page: int


def kb_availability(categories, current_page=1):
    inline_kb = []

    total_pages = sum(1 for category in categories if ItemRepository().items_by_category(category['name']))

    if not total_pages:
        return None

    nav = []
    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=AvailabilityNavigation(page=current_page - 1).pack()
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
            callback_data=AvailabilityNavigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


def text_availability_list(input_categories, i18n, current_page: int = 1):
    categories = list(category for category in input_categories if ItemRepository().items_by_category(category['name']))

    start_index = (current_page - 1)
    end_index = min(start_index + 1, len(categories))

    message = ""

    # load from db
    for i in range(start_index, end_index):
        message += i18n.CLIENT.AVAILABILITY.CATEGORY(category=categories[i]['name'])
        message += "\n"

        for item in ItemRepository().items_by_category(categories[i]['name']):
            message += i18n.CLIENT.AVAILABILITY.ITEM(title=item['title'], cost=item['cost'])
            message += "\n"

    if not len(message):
        message = i18n.CLIENT.AVAILABILITY.NO_ITEMS()

    return message

