from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message
from Keyboards.interfaces import psc_gamemode, starting_menu
from Handlers.database import user_in
from States.user_states import Fsm_state_list
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command('start'))
async def psc_starting(message: Message, state: FSMContext):
    await state.set_state(Fsm_state_list.START)
    await message.answer(text='Hello there!',
                         reply_markup=starting_menu())
    user_in(message.chat.id, message.from_user.username)

# ¯\_(ツ)_/¯'
