#делай через пороли пожалуйста
# мв в начале кода проходили как
# из комманд только start
# примеры паролей я могу скинуть
import telebot as telebot
from config import token
from database import Users_base

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def challenge_to_duel(message):
    base = Users_base()
    if not base.check_user_exists(message.chat.id):
        base.add_user(message.chat.id, message.chat.first_name, message.chat.username)
    bot.send_message(message.chat.id, "привет")