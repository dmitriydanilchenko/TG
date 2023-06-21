from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/image')
b4 = KeyboardButton('/stiker')
kb.add(b1,b2).add(b3,b4)
