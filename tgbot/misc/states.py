
from aiogram.dispatcher.filters.state import StatesGroup, State

class Balance(StatesGroup):
    B_exchange = State()
    B_recipient = State()
    B_value = State()
    B_curency = State()
