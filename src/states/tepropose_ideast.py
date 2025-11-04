from aiogram.fsm.state import State, StatesGroup


class TeproposeIdeast(StatesGroup):
    suggestions = State()
    first_message_sent = State()