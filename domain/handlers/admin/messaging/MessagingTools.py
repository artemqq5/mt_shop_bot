from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboards.admin.kb_messaging import kb_send_message_all_clients


class MessagingTools:
    @staticmethod
    def is_valid_url(url: str) -> bool:
        return url.startswith("https://")

    @staticmethod
    async def add_new_button(state: FSMContext):
        data = await state.get_data()
        buttons = data.get("buttons", [])
        buttons.append({})
        await state.update_data(buttons=buttons)

    @staticmethod
    async def add_text_last_button(state: FSMContext, text: str):
        data = await state.get_data()
        buttons = data.get("buttons", [{}])
        buttons[-1]['btn_text'] = text

        await state.update_data(buttons=buttons)

    @staticmethod
    async def add_url_last_button(state: FSMContext, text: str):
        data = await state.get_data()
        buttons = data.get("buttons", [{}])
        buttons[-1]['btn_url'] = text

        await state.update_data(buttons=buttons)

    @staticmethod
    async def preview_message(data, message: Message):

        if len(data.get('buttons', [])) > 0:
            kb_buttons = []
            for btn in data.get('buttons'):
                print(btn)
                kb_buttons.append([InlineKeyboardButton(text=btn['btn_text'], url=btn['btn_url'])])
            kb_buttons = InlineKeyboardMarkup(inline_keyboard=kb_buttons)
        else:
            kb_buttons = None

        if data.get('photo', None):
            await message.answer_photo(
                photo=data.get('photo'),
                caption=data['message'],
                reply_markup=kb_buttons
            )
        elif data.get('video', None):
            await message.answer_video(
                video=data.get('video'),
                caption=data['message'],
                reply_markup=kb_buttons
            )
        elif data.get('animation', None):
            await message.answer_animation(
                animation=data.get('animation'),
                caption=data['message'],
                reply_markup=kb_buttons
            )
        else:
            await message.answer(
                text=data['message'],
                reply_markup=kb_buttons
            )

