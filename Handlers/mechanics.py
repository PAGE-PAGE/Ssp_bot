from random import choice
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from Keyboards.interfaces import psc_gamemode, profile_window, starting_menu
from States.user_states import Fsm_state_list
from aiogram.fsm.context import FSMContext
from Handlers.database import draw_counter, loses_counter, win_counter, gpd_wld

router = Router()


@router.callback_query(F.data == '🔙')
async def i_always_come_back(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.START)
    await callback.message.edit_text(text='Hello there!',
                                     reply_markup=starting_menu())
    await callback.answer()


@router.callback_query(F.data == 'profile', StateFilter(Fsm_state_list.START))
async def profile_managing(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.PROFILE)
    get = gpd_wld(callback.from_user.id)
    await callback.message.edit_text(text=f'''<b>---YOUR PROFILE---
Name: {get[0][0]}
Wins: {get[0][1]}
Looses: {get[0][2]}
Draws: {get[0][3]}
                                       
Lb place:
</b>''', reply_markup=profile_window(), parse_mode='HTML')
    await callback.answer()


@router.callback_query(F.data == 'ssp', StateFilter(Fsm_state_list.START))
async def starting_game_pose(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.GAME)
    await callback.message.edit_text(text='<b>Choose to start</b>',
                                     reply_markup=psc_gamemode(), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == '📃', StateFilter(Fsm_state_list.GAME))
@router.callback_query(F.data == '✂️', StateFilter(Fsm_state_list.GAME))
@router.callback_query(F.data == '🗿', StateFilter(Fsm_state_list.GAME))
async def answer(callback: CallbackQuery):
    action = callback.data
    id = callback.from_user.id
    comp = choice(['🗿', '📃', '✂️'])
    res = ''
    if action == '🗿':
        if comp == '🗿':
            res = 'DRAW'
            draw_counter(id)
        if comp == '📃':
            res = 'LOSE'
            loses_counter(id)
        if comp == '✂️':
            res = 'WIN'
            win_counter(id)
    if action == '📃':
        if comp == '🗿':
            res = 'WIN'
            win_counter(id)
        if comp == '📃':
            res = '️DRAW'
            draw_counter(id)
        if comp == '✂️':
            res = 'LOSE'
            loses_counter(id)
    if action == '✂️':
        if comp == '🗿':
            res = 'LOSE'
            loses_counter(id)
        if comp == '📃':
            res = 'WIN'
            win_counter(id)
        if comp == '✂️':
            res = 'DRAW'
            draw_counter(id)
    try:
        await callback.message.edit_text(
            text=f'Your choice: <b>{action}</b>\nComputer choice: <b>{comp}</b>\nMatch end with your: <b>{res}</b>',
            reply_markup=psc_gamemode(), parse_mode="HTML")
        await callback.answer()
    except TelegramBadRequest:
        await callback.answer()


@router.callback_query()
async def trash(callback: CallbackQuery):
    await callback.answer('Are blindfolded? !BACK! , who is it for')

# ¯\_(ツ)_/¯
