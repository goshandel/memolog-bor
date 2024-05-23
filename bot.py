#делай через пороли пожалуйста
# мв в начале кода проходили как
# из комманд только start
# примеры паролей я могу скинуть
import telebot as telebot

from buttons import start_markup, get_meme, choice_month, year_list, month_list, choice_year
from config import token
from database import Users_base, Years_base
from info import start_text, help_info, help_from_users_info, read_meme_info, choice_info, \
    choice_info_none_n1, choice_info_none_n2, memes_info

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def challenge_to_duel(message):
    users_db = Users_base()
    if not users_db.check_user_exists(message.chat.id):
        users_db.add_user(message.chat.id, message.chat.first_name, message.chat.username)
    bot.send_message(message.chat.id, start_text, parse_mode='html', reply_markup=start_markup)
    users_db.close()


def specification(message):
    password = "ГДЕ 🌎 Я"
    return password.lower() in message.text.lower()

@bot.message_handler(content_types=['text'], func=specification)
def say_hello(message):
    bot.send_message(message.chat.id, help_info, parse_mode='html', reply_markup=start_markup)


def help_from_users(message):
    password = "🛟ШИРОКУЮ НА ШИРОКУЮ🛟"
    return password.lower() in message.text.lower()

@bot.message_handler(content_types=['text'], func=help_from_users)
def say_hello(message):
    bot.send_message(message.chat.id, help_from_users_info, parse_mode='html')
    bot.register_next_step_handler(message, save_council)

def save_council(message):
    text = message.text
    id = message.chat.id
    users_db = Users_base()
    users_db.add_council(id, text)
    users_db.close()
    bot.send_message(message.chat.id, "модеры подумаяют решать ли это💋", reply_markup=start_markup)


def read_meme(message):
    password = "ВЫБРАТЬ МЕМ🔍"
    return password.lower() in message.text.lower()

@bot.message_handler(content_types=['text'], func=read_meme)
def say_hello(message):
    bot.send_message(message.chat.id, read_meme_info, parse_mode='html', reply_markup=get_meme)

@bot.callback_query_handler(func=lambda callback: callback.data == "year")
def choice_month_(callback):
    bot.edit_message_text(text=choice_info, chat_id=callback.message.chat.id,  parse_mode='html',
                          message_id=callback.message.message_id, reply_markup=choice_year)

@bot.callback_query_handler(func=lambda callback: callback.data == "month")
def choice_month_(callback):
    bot.edit_message_text(text=choice_info, chat_id=callback.message.chat.id,  parse_mode='html',
                          message_id=callback.message.message_id, reply_markup=choice_month)

@bot.callback_query_handler(func=lambda callback: callback.data in year_list)
def choice_month_(callback):
    user_db = Users_base()
    user_db.add_year(callback.message.chat.id, int(callback.data))
    user_db.close()
    bot.edit_message_text(text=read_meme_info, chat_id=callback.message.chat.id, parse_mode='html',
                          message_id=callback.message.message_id, reply_markup=get_meme)

@bot.callback_query_handler(func=lambda callback: callback.data in month_list)
def choice_month_(callback):
    user_db = Users_base()
    user_db.add_month(callback.message.chat.id, int(callback.data))
    user_db.close()
    bot.edit_message_text(text=read_meme_info, chat_id=callback.message.chat.id, parse_mode='html',
                          message_id=callback.message.message_id, reply_markup=get_meme)

@bot.callback_query_handler(func=lambda callback: callback.data == "accept")
def choice_month_(callback):
    user_db = Users_base()
    id = callback.message.chat.id
    year_month = user_db.get_year_month(id)
    user_db.close()
    if year_month == None:
        bot.edit_message_text(text=choice_info_none_n1, chat_id=callback.message.chat.id,  parse_mode='html',
                              message_id=callback.message.message_id)
        return
    years_bd = Years_base()
    if not years_bd.check_year_month(year_month):
        bot.edit_message_text(text=choice_info_none_n2, chat_id=callback.message.chat.id,  parse_mode='html',
                          message_id=callback.message.message_id)

        return
    memes = years_bd.get_meme(year_month)
    bot.edit_message_text(text=memes, chat_id=callback.message.chat.id,  parse_mode='html',
                          message_id=callback.message.message_id)
    bot.send_message(callback.message.chat.id, memes_info)


bot.infinity_polling()