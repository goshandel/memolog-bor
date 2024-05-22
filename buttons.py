from telebot.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
info = KeyboardButton("ГДЕ 🌎 Я")
get_meme = KeyboardButton("ВЫБРАТЬ МЕМ🔍")
council = KeyboardButton("🛟ШИРОКУЮ НА ШИРОКУЮ🛟")
start_markup.add(info, get_meme, council)
