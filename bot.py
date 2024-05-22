#делай через пороли пожалуйста
# мв в начале кода проходили как
# из комманд только start
# примеры паролей я могу скинуть
import telebot as telebot
from config import token
from database import Users_base
from info import start_text

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def challenge_to_duel(message):
    users_db = Users_base()
    if not users_db.check_user_exists(message.chat.id):
        users_db.add_user(message.chat.id, message.chat.first_name, message.chat.username)
    bot.send_message(message.chat.id, start_text, parse_mode='html')
bot.infinity_polling()