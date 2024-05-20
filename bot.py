#делай через пороли пожалуйста
# мв в начале кода проходили как
# из комманд только start
# примеры паролей я могу скинуть
import telebot as telebot
from config import token

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def challenge_to_duel(message):
    bot.send_message(message.chat.id, "привет")