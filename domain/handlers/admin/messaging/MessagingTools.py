from aiogram.fsm.context import FSMContext


class MessagingTools:
    @staticmethod
    async def is_valid_url(url: str) -> bool:
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