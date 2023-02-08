import telebot
from random import randrange
game =  False


bot = telebot.TeleBot("Token", parse_mode=None)
@bot.message_handler(commands=['игра'])
def send_welcome(message):
    game = True
    bot.reply_to(message, 'Игра началась')
    
@bot.message_handler(commands=['Вычисли выражение'])
def send_welcome(message):
    bot.reply_to(message, 'Введите выражение')    
    
@bot.message_handler(content_types=['text'])
def echo_all(message):
    global game
    if message.text == 'игра':
        bot.reply_to(message, "Введите число ")
        game = True   
        number = randrange(1000)+ 1
        guess = message.text
        count = 0
        while guess != number:
            bot.reply_to(message, "Введите число ")
            count+=1
            if guess < number and message.text.isdigit():
                bot.reply_to(message, "Загаданное число меньше")
            elif guess > number and message.text.isdigit():
                bot.reply_to(message, "Загаданное число больше")
    game = False        
    bot.reply_to(message, "Вы отгадали число, количество попыток", count)
    
    
@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'Вычисли выражение':
        bot.reply_to(message, "Введите выражение")
        num = message.text
        if num.isdigit():
            print(message, f' ответ:  {eval(num)}')
        bot.reply_to(message, message.text) 
        
        
         
 
bot.infinity_polling()