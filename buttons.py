from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
start_markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
info = KeyboardButton("ГДЕ 🌎 Я")
get_year_month = KeyboardButton("ВЫБРАТЬ МЕМ🔍")
council = KeyboardButton("🛟ШИРОКУЮ НА ШИРОКУЮ🛟")
start_markup.add(info, get_year_month, council)

get_meme = InlineKeyboardMarkup(row_width=1)
get_meme.add(InlineKeyboardButton("год🎈", callback_data="year"),
             InlineKeyboardButton("месяц🌝", callback_data="month"),
             InlineKeyboardButton("получить мем✅", callback_data="accept"),)

choice_year = InlineKeyboardMarkup(row_width=5)
y_2024 = InlineKeyboardButton("2024", callback_data="2024")
y_2023 = InlineKeyboardButton("2023", callback_data="2023")
y_2022 = InlineKeyboardButton("2022", callback_data="2022")
y_2021 = InlineKeyboardButton("2021", callback_data="2021")
y_2020 = InlineKeyboardButton("2020", callback_data="2020")
y_2019 = InlineKeyboardButton("2019", callback_data="2019")
y_2018 = InlineKeyboardButton("2018", callback_data="2018")
y_2017 = InlineKeyboardButton("2017", callback_data="2017")
y_2016 = InlineKeyboardButton("2016", callback_data="2016")
y_2015 = InlineKeyboardButton("2015", callback_data="2015")
y_2014 = InlineKeyboardButton("2014", callback_data="2014")
y_2013 = InlineKeyboardButton("2013", callback_data="2013")
y_2012 = InlineKeyboardButton("2012", callback_data="2012")
choice_year.add(y_2024, y_2023, y_2022, y_2021, y_2020)
choice_year.add(y_2019, y_2018, y_2017)
choice_year.add(y_2016, y_2015, y_2013, y_2012)
year_list = ["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012"]

choice_month = InlineKeyboardMarkup(row_width=4)
December  = InlineKeyboardButton("ДЕК", callback_data="декабрь")
January  = InlineKeyboardButton("ЯНВ", callback_data="январь")
February  = InlineKeyboardButton("ФЕВ", callback_data="февраль")
March  = InlineKeyboardButton("МАРТ", callback_data="март")
April  = InlineKeyboardButton("АПР", callback_data="апрель")
May  = InlineKeyboardButton("МАЙ", callback_data="май")
June  = InlineKeyboardButton("ИЮНЬ", callback_data="июнь")
July  = InlineKeyboardButton("ИЮЛЬ", callback_data="июль")
August  = InlineKeyboardButton("АВГ", callback_data="август")
September  = InlineKeyboardButton("СЕНТ", callback_data="сентябрь")
October  = InlineKeyboardButton("ОКТ", callback_data="октябрь")
November  = InlineKeyboardButton("НОЯ", callback_data="ноябрь")
choice_month.add(December, January, February, March, April, May, June, July, August, September, October, November)
month_list = ["декабрь", "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь"]
