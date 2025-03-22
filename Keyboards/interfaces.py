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
                 InlineKeyboardButton(text='Profile View', callback_data='profile'))
    return keyboard.as_markup()


def profile_window():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()

# ¯\_(ツ)_/¯
