from aiogram.fsm.state import State, StatesGroup


class Fsm_state_list(StatesGroup):
    START = State()
    PROFILE = State()
    GAME = State()
    SOCIAL = State()
    LBOARD = State()
    DONAT = State()

# ¯\_(ツ)_/¯
