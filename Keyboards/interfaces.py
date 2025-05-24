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
                 InlineKeyboardButton(text='Social Stats', callback_data='social'),
                 InlineKeyboardButton(text='Leader board', callback_data='leader'),
                 InlineKeyboardButton(text='Donat', callback_data='donat'))
    return keyboard.as_markup()


def social_ref_link():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Ref link', callback_data='link'),
                 InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()


def stars_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='1⭐️', callback_data='stars:1'),
                 InlineKeyboardButton(text='5⭐️', callback_data='stars:5'),
                 InlineKeyboardButton(text='10⭐️', callback_data='stars:10'),
                 InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()


def donation_keyboard(amount):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=f'{amount} XTR', pay=True),
                 InlineKeyboardButton(text='🔙', callback_data='🔙🔙'))
    return keyboard.as_markup()


def back():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🔙', callback_data='🔙'))
    return keyboard.as_markup()

# ¯\_(ツ)_/¯
