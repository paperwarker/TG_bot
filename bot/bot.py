import telebot
import config
from telebot import types

bot=telebot.TeleBot(config.TOKEN)

arr=[ "Заниматься проектированием и созданием различных приборов",
"Решать задачи, связанные с оптимизацией и улучшением производства",
"Изучать как устроена психика человека", "Охранять природу от негативного человеческого влияния",
"Работать с людьми и помогать им ", "Изучать физические процессы и применять полученные знания на практике",
"Работать с финансами и экономическими процессами", "Создавать компьютерные прогаммы и тестировать их",
"Проектировать и разрабатываеть различные инженерные сооружения", "Анализировать данные и на их основе принимать решения",
"Работать с химическими элементами и создавать различные материалы", "Применять математические знания в различных задачах",
"Совершенствовать компьютеры и вычислительне машины", "Изготавливать и обслуживать платы и микросхемы",
"Создавать компьютерные сети и обеспечивать их", "Заниматься работой с документами", "Работать в правовой сфере и регулировать отношения между гражданами и предприятиями",
"Управлять бизнес-процессами и изучать их", "Работать на сложном химическом оборудовании, проводить опыты с химическими веществами",
"Трудиться в сфере, связанной с государственным управлением", "Производить и продавать новую технику и технологии",
"Изучать взаимоотношения людей и применять знания на практике", "Создавать языковые модели и заниматься и их анализом",
"Проектировать разные компьютерные системы и поддерживать их функционирование", "Анализировать рынок товаров и услуг, выбирать направления развития предприятия",
"Помогать людям поддерживать психологическое здоровье", "Придумывать и реализовывать альтернативные способы получения энергии", 
"Создавать новые изделия и материалы, применяя знания химии и физики", "Дорабатывать и совершенствовать существующие технологии и технические решения",
"Зниматься дизайном программных продуктов" ]



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
    markup=types.InlineKeyboardMarkup(row_width=5)
    item1=types.InlineKeyboardButton("1", callback_data="one")
    item2=types.InlineKeyboardButton("2", callback_data="two")
    item3=types.InlineKeyboardButton("3", callback_data="three")
    item4=types.InlineKeyboardButton("4", callback_data="four")
    item5=types.InlineKeyboardButton("5", callback_data="five")
    markup.add(item1, item2, item3, item4, item5)
    try:
        if call.message:
               
            if call.data=="yes":
                
                bot.send_message(call.message.chat.id, "первый вопрос", reply_markup=markup)
                for i in range(30):
                    if call.data=="one" or call.data=="two" or call.data=="three" or call.data=="four" or call.data=="five":
                        bot.send_message(call.message.chat.id, arr[i], reply_markup=markup) 
                    bot.register_next_step_handler()
                    
                
            elif call.data=="no":
                bot.send_message(call.message.chat.id, "Зачем ты тогда пришел?")

            elif call.data=="one" or call.data=="two" or call.data=="three" or call.data=="four" or call.data=="five":
                for i in range(30):
                    bot.send_message(call.message.chat.id, arr[i], reply_markup=markup) 
                    

    except Exception as e:
        print(repr(e)) 

def questions():
    markup=types.InlineKeyboardMarkup(row_width=5)
    item1=types.InlineKeyboardButton("1", callback_data="one")
    item2=types.InlineKeyboardButton("2", callback_data="two")
    item3=types.InlineKeyboardButton("3", callback_data="three")
    item4=types.InlineKeyboardButton("4", callback_data="four")
    item5=types.InlineKeyboardButton("5", callback_data="five")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(call.message.chat.id, "первый вопрос", reply_markup=markup)

bot.polling(none_stop=True)

def questions():
    markup=types.InlineKeyboardMarkup(row_width=5)
    item1=types.InlineKeyboardButton("1", callback_data="one")
    item2=types.InlineKeyboardButton("2", callback_data="two")
    item3=types.InlineKeyboardButton("3", callback_data="three")
    item4=types.InlineKeyboardButton("4", callback_data="four")
    item5=types.InlineKeyboardButton("5", callback_data="five")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(call.message.chat.id, "первый вопрос", reply_markup=markup)