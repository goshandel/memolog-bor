import os
from PIL import Image
import io
import telebot as telebot
from buttons import start_markup, get_meme, choice_month, year_list, month_list, choice_year, add_meme1
from config import token
from database import Users_base, Years_base, Memes_base, image_to_base64, decode_base64_image
from info import start_text, help_info, help_from_users_info, read_meme_info, choice_info, \
    choice_info_none_n1, choice_info_none_n2, memes_info, error_desk, for_admin_list, no_admin

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
    user_db.add_meme(callback.message.chat.id, memes)
    user_db.close()
    bot.edit_message_text(text=memes, chat_id=callback.message.chat.id,  parse_mode='html',
                          message_id=callback.message.message_id)
    bot.send_message(callback.message.chat.id, memes_info, parse_mode='html')
    years_bd.close()
    bot.register_next_step_handler(callback.message, get_description)
def get_description(message):
    user_db = Users_base()
    memes = user_db.get_meme(message.chat.id)
    memes = memes.lower()
    meme = message.text.lower()
    if not meme in memes:
        bot.send_message(message.chat.id, error_desk, reply_markup=start_markup, parse_mode='html')
        bot.register_next_step_handler(message, get_description)
        return
    user_db.add_meme(message.chat.id, message.text)
    user_db.close()
    memes_db = Memes_base()
    photo_base64 = memes_db.get_photo(message.text)
    description = memes_db.get_description(message.text)
    img = decode_base64_image(photo_base64)
    img.save("temp_image.jpg")
    bot.send_photo(chat_id=message.chat.id, photo=open("temp_image.jpg", "rb"), caption=description)
    os.remove("temp_image.jpg")
    memes_db.close()
@bot.message_handler(commands=["new_meme"])
def add_new_meme(message):
    users_db = Users_base()
    if not users_db.check_admin(message.chat.id):
        bot.send_message(message.chat.id, no_admin, parse_mode='html', reply_markup=start_markup)
        return
    users_db.close()
    bot.send_message(message.chat.id, "для начал выбери дату как только выберешь напиши название мема", reply_markup=add_meme1)
    bot.register_next_step_handler(message, add_name)
def add_name(message):
    name = message.text
    name_for_year = name + '\n'
    memes_db = Memes_base()
    users_db = Users_base()
    year_month = users_db.get_year_month(message.chat.id)
    years_db = Years_base()
    if not years_db.check_year_month(year_month):
        years_db.add_new_month(year_month)
    years_db.add_meme(year_month, name_for_year)
    memes_db.add_new_meme(name)
    users_db.add_meme(message.chat.id, name)
    users_db.close()
    memes_db.close()
    years_db.close()
    bot.send_message(message.chat.id, "Напиши описание")
    bot.register_next_step_handler(message, add_description)
def add_description(message):
    description = message.text
    memes_db = Memes_base()
    users_db = Users_base()
    meme = users_db.get_meme(message.chat.id)
    memes_db.add_description(str(description), meme)
    users_db.close()
    memes_db.close()
    bot.send_message(message.chat.id, "отрпавь фото мема форматом 1:1")
    bot.register_next_step_handler(message, add_photo)
def add_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    try:
        image = Image.open(io.BytesIO(downloaded_file))
        width, height = image.size
        if width != height:
            bot.send_message(message.chat.id, "Изображение не является квадратом.")
            return
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при открытии изображения.")
        return
    save_path = 'photo.jpg'
    with open(save_path, 'wb') as f:
        f.write(downloaded_file)
    base64_img = image_to_base64(save_path)
    if base64_img:
        memes_db = Memes_base()
        users_db = Users_base()
        meme = users_db.get_meme(message.chat.id)
        memes_db.add_photo(str(base64_img), meme)
        users_db.close()
        memes_db.close()
        bot.send_message(message.chat.id, "Спасибо")
        os.remove(save_path)
    else:
        bot.send_message(message.chat.id, "Не удалось обработать изображение.")

@bot.message_handler(commands=["users"])
def get_users(message):
    users_db = Users_base()
    if not users_db.check_admin(message.chat.id):
        bot.send_message(message.chat.id, no_admin, parse_mode='html', reply_markup=start_markup)
        return
    users_db.close()
    users_db = Users_base()
    users = users_db.get_all_users()
    first_three_values = []
    for user_tuple in users:
        first_three_values.append(user_tuple[:3])
    message_text = "\n".join(
        [f"{i + 1}. Айди: {value[0]}, Имя: {value[1]}, Никнейм: {value[2]}" for i, value in enumerate(first_three_values)])
    bot.send_message(message.chat.id, message_text)
    users_db.close()
@bot.message_handler(commands=["new_admin"])
def new_admin(message):
    users_db = Users_base()
    if not users_db.check_admin(message.chat.id):
        bot.send_message(message.chat.id, no_admin, parse_mode='html', reply_markup=start_markup)
        return
    users_db.close()
    bot.send_message(message.chat.id, "отправь айди пользователя. если что тебе следовало ввести  /users")
    bot.register_next_step_handler(message, add_admin)
def add_admin(message):
    users_db = Users_base()
    if not users_db.check_admin(message.chat.id):
        bot.send_message(message.chat.id, no_admin, parse_mode='html', reply_markup=start_markup)
        return
    users_db.close()
    users_db = Users_base()
    try:
        users_db.new_admin(int(message.chat.id))
        bot.send_message(message.chat.id, "готово!")
    except:
        bot.send_message(message.chat.id, "проверь айди")
    users_db.close()
@bot.message_handler(commands=["get_council"])
def return_council(message):
    users_db = Users_base()
    if not users_db.check_admin(message.chat.id):
        bot.send_message(message.chat.id, no_admin, parse_mode='html', reply_markup=start_markup)
        return
    users_db.close()
    users_db = Users_base()
    council = users_db.update_and_return_council()
    bot.send_message(message.chat.id, council)
    users_db.close()
@bot.message_handler(commands=["help"])
def return_council(message):
    users_db = Users_base()
    if not users_db.check_admin(message.chat.id):
        bot.send_message(message.chat.id, no_admin, parse_mode='html', reply_markup=start_markup)
        return
    users_db.close()
    bot.send_message(message.chat.id, for_admin_list)
bot.infinity_polling()