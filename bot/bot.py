import telebot
import config
from telebot import types


bot=telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    
    spi=open("sticker.webp", "rb")
    bot.send_sticker(message.chat.id, spi)
    bot.send_message(message.chat.id, "Привет, чумба! \n Я бот ГУДа и я слышал, ты ищешь место для образования. \n Я могу помочь тебе, но сначала назови свое имя".format(message.from_user, bot.get_me()), parse_mode='html')
    
    
@bot.message_handler(content_types=['text'])
def name(message):
    if message.chat.type=="private":
        markup=types.InlineKeyboardMarkup(row_width=2)
        item1=types.InlineKeyboardButton("Да", callback_data="yes")
        item2=types.InlineKeyboardButton("Нет", callback_data="no")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Привет, "+message.text+"!!! \n Ты готов ответить на несколько вопросов".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data=="yes":
                bot.send_message(call.message.chat.id, "Отлично, давай начнем")
            elif call.data=="no":
                bot.send_message(call.message.chat.id, "Зачем ты тогда пришел?")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вопросы",reply_markup=None)  
    except Exception as e:
        print(repr(e)) 

bot.polling(none_stop=True)

def questions(question):
    markup=types.InlineKeyboardMarkup(row_width=5)
    item1=types.InlineKeyboardButton("1", callback_data="one")
    item2=types.InlineKeyboardButton("2", callback_data="two")
    item3=types.InlineKeyboardButton("3", callback_data="three")
    item4=types.InlineKeyboardButton("4", callback_data="four")
    item5=types.InlineKeyboardButton("5", callback_data="five")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, question.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)