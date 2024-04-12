from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    start = State()


class GptState(StatesGroup):
    message_to_gpt = State()
