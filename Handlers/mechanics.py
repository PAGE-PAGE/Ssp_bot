from random import choice
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, LabeledPrice
from aiogram.exceptions import TelegramBadRequest
from Keyboards.interfaces import psc_gamemode, back, starting_menu, social_ref_link, stars_keyboard, donation_keyboard
from States.user_states import Fsm_state_list
from aiogram.fsm.context import FSMContext
from Handlers.database import *
router = Router()


@router.callback_query(F.data == '🔙')
async def i_always_come_back(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.START)
    await callback.message.edit_text(text='Hello there!',
                                     reply_markup=starting_menu())
    await callback.answer()


@router.callback_query(F.data == '🔙🔙')
async def i_always_come_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()

@router.callback_query(F.data == 'profile', StateFilter(Fsm_state_list.START))
async def profile_managing(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.PROFILE)
    get = gpd_wld(callback.from_user.id)
    await callback.message.edit_text(text=f'''<b>---YOUR PROFILE---
Name: "{get[0][0]}"
Wins: {get[0][1]}
Looses: {get[0][2]}
Draws: {get[0][3]}
</b>''', reply_markup=back(), parse_mode='HTML')
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
    if action == comp:
        res = 'DRAW'
        draw_counter(id)
    if action == '🗿' and comp == '✂️' or action == '📃' and comp == '🗿' or action == '✂️' and comp == '📃':
        res = 'WIN'
        win_counter(id)
        check_for_bonus(id)
    if action == '🗿' and comp == '📃' or action == '📃' and comp == '✂️' or action == '✂️' and comp == '🗿':
        res = 'LOSE'
        loses_counter(id)
    try:
        await callback.message.edit_text(
            text=f'Your choice: <b>{action}</b>\nComputer choice: <b>{comp}</b>\nMatch end with your: <b>{res}</b>',
            reply_markup=psc_gamemode(), parse_mode="HTML")
        await callback.answer()
    except TelegramBadRequest:
        await callback.answer()


@router.callback_query(F.data == 'link')
async def generate_ref_link(callback: CallbackQuery):
    await callback.message.answer(f"Your ref link:\n"
                                  f"<code>https://t.me/aparfins_bot?start={callback.from_user.id}</code>", parse_mode='HTML')
    await callback.answer()


@router.callback_query(F.data == 'social', StateFilter(Fsm_state_list.START))
async def view_social_stats(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.SOCIAL)
    nick = callback.from_user.username
    for a, b in enumerate(lb_info(), 1):
        if nick == b[0]:
            break
    get = get_friends(callback.from_user.id), get_bonuses(callback.from_user.id)
    if a == 1:
        a = '🥇'
    elif a == 2:
        a = '🥈'
    elif a == 3:
        a = '🥉'
    await callback.message.edit_text(text=f'''<b>---YOUR SOCIAL STATS---
Friends: {get[0]}
Bonuses: {get[1]}
Lb place: {nick} {a}
</b>''', reply_markup=social_ref_link(), parse_mode='HTML')
    await callback.answer()


@router.callback_query(F.data == 'leader', StateFilter(Fsm_state_list.START))
async def view_social_stats(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.LBOARD)
    b = ''
    for a, c in enumerate(lb_info(), 1):
        b += f'#{a} {c[0]} Wins:{c[1]}\n'
    await callback.message.edit_text(text=f'''<b>---LEADER BOARD---
{b}
    </b>''', reply_markup=back(), parse_mode='HTML')
    await callback.answer()


@router.callback_query(F.data == 'donat', StateFilter(Fsm_state_list.START))
async def u1y1t1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Fsm_state_list.DONAT)
    await callback.message.edit_text(text=f'''<b>-----DONAT-----
!Donat to give me more time to life🤩
        </b>''', reply_markup=stars_keyboard(), parse_mode='HTML')
    await callback.answer()


@router.callback_query(F.data == 'stars:1', StateFilter(Fsm_state_list.DONAT))
@router.callback_query(F.data == 'stars:5', StateFilter(Fsm_state_list.DONAT))
@router.callback_query(F.data == 'stars:10', StateFilter(Fsm_state_list.DONAT))
async def payment_xleb(callback: CallbackQuery, state: FSMContext):
    amount = int(callback.data.split(':')[1])
    prices = [LabeledPrice(label="XTR", amount=amount)]
    await callback.message.answer_invoice(
        title='donation',
        description='You donate:',
        prices=prices,
        provider_token="",
        payload=f"{amount}_stars",
        currency="XTR",
        reply_markup=donation_keyboard(amount)
    )
    await state.set_state(Fsm_state_list.START)
    await callback.answer()


@router.callback_query()
async def trash(callback: CallbackQuery):
    await callback.answer('Are blindfolded? !BACK! , who is it for')

# ¯\_(ツ)_/¯
