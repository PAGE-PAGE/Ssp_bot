from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def psc_gamemode():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🗿', callback_data='🗿'),
                 InlineKeyboardButton(text='✂️', callback_data='✂️'),
                 InlineKeyboardButton(text='📃', callback_data='📃'),
                 InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()


def starting_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Start Psc-Game', callback_data='ssp'),
                 InlineKeyboardButton(text='Profile View', callback_data='profile'),
                 InlineKeyboardButton(text='Social Stats', callback_data='social'))
    return keyboard.as_markup()


def social_ref_link():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Ref link', callback_data='link'),
                 InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()


def profile_window():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()

# ¯\_(ツ)_/¯
