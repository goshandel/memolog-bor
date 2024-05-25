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

choice_month = InlineKeyboardMarkup(row_width=3)
December  = InlineKeyboardButton("ДЕК", callback_data="12")
January  = InlineKeyboardButton("ЯНВ", callback_data="01")
February  = InlineKeyboardButton("ФЕВ", callback_data="02")
March  = InlineKeyboardButton("МАРТ", callback_data="03")
April  = InlineKeyboardButton("АПР", callback_data="04")
May  = InlineKeyboardButton("МАЙ", callback_data="05")
June  = InlineKeyboardButton("ИЮНЬ", callback_data="06")
July  = InlineKeyboardButton("ИЮЛЬ", callback_data="07")
August  = InlineKeyboardButton("АВГ", callback_data="08")
September  = InlineKeyboardButton("СЕНТ", callback_data="09")
October  = InlineKeyboardButton("ОКТ", callback_data="10")
November  = InlineKeyboardButton("НОЯ", callback_data="11")
choice_month.add(December, January, February, March, April, May, June, July, August, September, October, November)
month_list = ["12", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

add_meme1 = InlineKeyboardMarkup(row_width=1)
add_meme1.add(InlineKeyboardButton("год🎈", callback_data="year_for_admin"),
             InlineKeyboardButton("месяц🌝", callback_data="month_for_admin"))

choice_year_for_admin = InlineKeyboardMarkup(row_width=5)
y_2024_for_admin = InlineKeyboardButton("2024", callback_data="02024")
y_2023_for_admin = InlineKeyboardButton("2023", callback_data="02023")
y_2022_for_admin = InlineKeyboardButton("2022", callback_data="02022")
y_2021_for_admin = InlineKeyboardButton("2021", callback_data="02021")
y_2020_for_admin = InlineKeyboardButton("2020", callback_data="02020")
y_2019_for_admin = InlineKeyboardButton("2019", callback_data="02019")
y_2018_for_admin = InlineKeyboardButton("2018", callback_data="02018")
y_2017_for_admin = InlineKeyboardButton("2017", callback_data="02017")
y_2016_for_admin = InlineKeyboardButton("2016", callback_data="02016")
y_2015_for_admin = InlineKeyboardButton("2015", callback_data="02015")
y_2014_for_admin = InlineKeyboardButton("2014", callback_data="02014")
y_2013_for_admin = InlineKeyboardButton("2013", callback_data="02013")
y_2012_for_admin = InlineKeyboardButton("2012", callback_data="02012")
choice_year_for_admin.add(y_2024_for_admin, y_2023_for_admin, y_2022_for_admin, y_2021_for_admin, y_2020_for_admin)
choice_year_for_admin.add(y_2019_for_admin, y_2018_for_admin, y_2017_for_admin)
choice_year_for_admin.add(y_2016_for_admin, y_2015_for_admin, y_2013_for_admin, y_2012_for_admin)
year_list_for_admin = ["02024", "02023", "02022", "02021", "02020", "02019", "02018", "02017", "02016", "02015", "02014", "02013", "02012"]

choice_month_for_admin = InlineKeyboardMarkup(row_width=3)
December_for_admin = InlineKeyboardButton("ДЕК", callback_data="012")
January_for_admin = InlineKeyboardButton("ЯНВ", callback_data="001")
February_for_admin = InlineKeyboardButton("ФЕВ", callback_data="002")
March_for_admin = InlineKeyboardButton("МАРТ", callback_data="003")
April_for_admin = InlineKeyboardButton("АПР", callback_data="004")
May_for_admin = InlineKeyboardButton("МАЙ", callback_data="005")
June_for_admin = InlineKeyboardButton("ИЮНЬ", callback_data="006")
July_for_admin = InlineKeyboardButton("ИЮЛЬ", callback_data="007")
August_for_admin = InlineKeyboardButton("АВГ", callback_data="008")
September_for_admin = InlineKeyboardButton("СЕНТ", callback_data="009")
October_for_admin = InlineKeyboardButton("ОКТ", callback_data="010")
November_for_admin = InlineKeyboardButton("НОЯ", callback_data="011")
choice_month_for_admin.add(December_for_admin, January_for_admin, February_for_admin,
                           March_for_admin, April_for_admin, May_for_admin,
                           June_for_admin, July_for_admin, August_for_admin,
                           September_for_admin, October_for_admin, November_for_admin)
month_list_for_admin = ["012", "001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011"]
