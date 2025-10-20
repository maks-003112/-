import os
import telebot

bot = os.getenv('TELEGRAM_BOT_TOKEN')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
