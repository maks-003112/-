import telebot

bot = telebot.TeleBot('8052926381:AAHOHiqUaQ8aI801XOVMPFOQLaNt8S3K4YU')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
