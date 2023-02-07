import telebot

bot = telebot.TeleBot("5881190851:AAFtLLkvjldXAF7xUbPArEOE1gxqmqXhngo", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как дела?")
 
@bot.message_handler(content_types=['text'])
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)
 
bot.infinity_polling()