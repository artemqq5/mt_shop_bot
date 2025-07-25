from aiogram.fsm.context import FSMContext
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup


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
    async def preview_message_send(data, bot, user_id):

        if len(data.get('buttons', [])) > 0:
            kb_buttons = []
            for btn in data.get('buttons'):
                kb_buttons.append([InlineKeyboardButton(text=btn['btn_text'], url=btn['btn_url'])])
            kb_buttons = InlineKeyboardMarkup(inline_keyboard=kb_buttons)
        else:
            kb_buttons = None

        if data.get('photo', None):
            await bot.send_photo(
                chat_id=user_id,
                photo=data.get('photo'),
                caption=data['message'],
                reply_markup=kb_buttons
            )
        elif data.get('video', None):
            await bot.send_video(
                chat_id=user_id,
                video=data.get('video'),
                caption=data['message'],
                reply_markup=kb_buttons
            )
        elif data.get('animation', None):
            await bot.send_animation(
                chat_id=user_id,
                animation=data.get('animation'),
                caption=data['message'],
                reply_markup=kb_buttons
            )
        else:
            await bot.send_message(
                chat_id=user_id,
                text=data['message'],
                reply_markup=kb_buttons
            )
