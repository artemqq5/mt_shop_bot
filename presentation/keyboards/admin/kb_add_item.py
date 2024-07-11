import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_managment import ManagementBack


class PreviewItemPublish(CallbackData, prefix="Preview*Item*Publish"):
    state: str


kb_preview_add_item = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.PUBLISH_ITEM(), callback_data=PreviewItemPublish(state="publish").pack())],
    [InlineKeyboardButton(text=L.ADMIN.RESTART_PUBLISH(), callback_data=PreviewItemPublish(state="restart").pack())],
])

kb_publish_onemore = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ADD_ITEM(), callback_data=PreviewItemPublish(state="restart").pack())],
])