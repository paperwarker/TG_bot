import sqlite3
import telebot
import config
from telebot import types

class InlineKeyboard:
    def __init__(self, bot):
        self.bot=bot

    def create_keybord(self, button_list):
        keyboard_markup=types.InlineKeyboardMarkup(row_width=5)

        buttons=[]
        for button_text, callback_data in button_list:
            button=types.InlineKeyboardButton(button_text, callback_data=callback_data)
            buttons.append(button)

        keyboard_markup.add(*buttons)
        return keyboard_markup

#TOKEN = '6072312598:AAGU1bXqOHTaO3vReEIXcW7DEPT2x1OgD0U'
#TOKEN = '6131343180:AAGleThVfO6O6lK6pIGev82qhzB1q88WwXU' #my private bot
bot = telebot.TeleBot(config.TOKEN)
inline_keybord = InlineKeyboard(bot)

technozhr = [0, 0, 0, 0, 0, 0]
technomag = [0, 0, 0, 0, 0, 0]
keep_soul = [0, 0, 0, 0, 0, 0]
alchemist = [0, 0, 0, 0, 0, 0]
keep_civil = [0, 0, 0, 0, 0, 0]
keep_world = [0, 0, 0, 0, 0, 0]
oracle = [0, 0, 0, 0, 0, 0]

global name 
global surname 
global email  
global city
global phone 
global school 
global us_id

arr = ["Осуществлять монтаж или сборку машин и приборов",
"Обслужиать и ремонтировать различные механизмы",
"Выяснять проблемы людей, проводить диагностику, искать причины проблем и объяснять их людям", "Изобретать и производить новые химические соединения (лаки, краски, бытововую химию и др.)",
"Создавать эффективную систему документооборота, перемещения товаров для работы предприятия", "Организовывать и управлять производством новой техники и технологий",
"Создавать одежду, обувь, предметы мебели и др. предметы быта", "Обеспечивать людей комфортным и безопасным жильем, поддерживать в рабочем состоянии городскую инфраструктуру",
"Обучать людей, преподавать в учебных заведениях, сообщать, разъяснять людям нужные им сведения", "Защищать природу от негативного воздействия человеческой цивилизации, обеспечивать жизнеспособность планеты",
"Держать людей в курсе событий, сообщать им важную информацию", "Создавать произведения фото- и видеоискусства",
"Анализировать статистические данные, составлять прогнозы и планы развития", "Руководить работой других людей и организовать людей для выполнения рабочих задач и мероприятий",
"Придумывать способы улучшить производство", "Составлять точные описания, отчеты о наблюдениях, явлениях, событиях, измеряемых объектах и др., открывать фундаментальные законы природы", "Делать изделия с уникальными свойствами из новых материалов",
"Исследовать свойства и природу веществ, придумывать и производить новые материалы", "Создавать, модернизировать и следить за безопасностью компьютерных сетей и программного обеспечения",
"Развивать у людей различные способности", "Обслуживать приборы, следить за их работой, регулировать и настраивать придумывать, изобретать новую технику и технологии (корабли, автомобили, космические корабли, энергостанции, компьютерную технику и программное обеспечение и др.)",
"Производить и продавать новую технику и технологии", "Следить за развитием науки и выбирать, какие технологии будут помогать человечеству эффективно развиваться",
"Выводить новые сорта растений, новые породы животных", "Добывать ресурсы для существования человеческой цивилизации (продукты питания, энергию, воду и пр.) и доставлять их людям",
"Помогать людям поддерживать физическое и психологическое здоровье, лечить, поддерживать в тяжелой ситуации, продвигать здоровый образ жизни", "Управлять персоналом в организации: осуществлять отбор, помогать адаптироваться, обучать, мотивировать на эффективную работу",
"Анализировать рынок товаров и выбирать направления развития предприятия", "Обеспечивать мирную коммуникацию людей друг с другом, помогать договариваться, разрешать споры, защищать юридические интересы людей и организаций",
"Придумывать, изобретать новую технику и технологии (корабли, автомобили, космические корабли, энергостанции, компьютерную технику и программное обеспечение и др.)", "Доводить информацию о товарах до потребителя", "Защищать интересы людей находящихся в трудных жизненных ситуациях",
"Улучшать существующие технику и технологии", "Работать на сложном химическом оборудовании, проводить опыты с химическими веществами", "Изготовлять по чертежам (проектам) детали, изделия, здания и сооружения"]

directs = ["Электроэнергетика и электротехника", "Авиастроение", "Конструирование и технология электронных средств", "Автоматизация технологических процессов и производств", "Информационные системы и технологии", "Системный анализ и управление", "Лингвистика", "Психология", "Клиническая психология", 
           "Юриспруденция", "Химия", "Ядерная физика и технологии", "Химия, физика и механика материалов", "Физика", "Химия", "Юриспруденция", "Социология", "Государственное и муниципальное управление", "Фундаментальная информатика и информационные технологии", 
           "Бизнес-информатика", "Автоматизация технологических процессов и производств", "Информатика и вычислительная техника", "Программная инженерия", "Авиастроение", "Прикладная математика и информатика", "Химия, физика и механика материалов", "Электроэнергетика и электротехника", 
           "Экология и природопользование", "Химия", "Технология геологической разведки", "Государственное и муниципальное управление", "Прикладная информатика", "Государственное и муниципальное управление", "Юриспруденция", "Экономика"]

@bot.message_handler(commands = ['start'])
def welcome(message):
    mrkp = types.ReplyKeyboardMarkup()
    btn3 = types.KeyboardButton('Да')
    btn4 = types.KeyboardButton('Нет (да)')
    mrkp.row(btn3, btn4)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Да", callback_data = 'yes')
    btn2 = types.InlineKeyboardButton("Нет", callback_data = 'no')
    markup.row(btn1, btn2)
    
    bot.send_message(message.chat.id, f"Здравствуй, добрый путник! \n Перед тобой открыта ГУД Вселенная! Эта Вселенная зародилась давным-давно, ещё в прошлом столетии. В этой Вселенной есть место каждому: здесь дружно живут представители разных гильдий, которые вместе строят и развивают ее. Чтобы всем в ней жилось хорошо предлагаем тебе найти и занять место в этой уникальной Вселенной! Для начала расскажи немного о себе.", reply_markup= mrkp)
    bot.send_message(message.chat.id, f"Твое имя {message.from_user.first_name}?", reply_markup= markup)

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()
def db_table_val(user_id: int, user_name: str, user_surname: str, email: str, city: str, school: str, phone: str):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, email, city, school, phone) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, user_name, user_surname, email, city, school, phone))
	conn.commit()
        
def update_db_table(faculty: str, direction: str, user_id: int):
	cursor.execute('UPDATE test SET faculty = ?, direction = ? WHERE user_id = ?', (faculty, direction, user_id))
	conn.commit()

@bot.message_handler(commands=['deleteaccount'])
def delete_account(message):
    user_id = message.from_user.id
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM test WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

    bot.send_message(message.chat.id, 'Ваш аккаунт удален из базы данных.')
    bot.send_message(message.chat.id, message.from_user.id)


@bot.callback_query_handler(func = lambda callback: True)
def callback_name(callback):
    global name  
    global technozhr
    global technomag
    global keep_soul
    global alchemist
    global keep_civil
    global keep_world
    global oracle 
    global phone
    global faculty
    global school
    global surname
    global name
    global email
    global city
    #us_id = callback.message.from_user.id

    buttons=[('1','one'),('2','two'),('3','three'),('4','four'),('5','five')]
    markup=inline_keybord.create_keybord(buttons)

    buttons1=[('1','one1'),('2','two1'),('3','three1'),('4','four1'),('5','five1')]
    markup1=inline_keybord.create_keybord(buttons1)

    buttons2=[('1','one2'),('2','two2'),('3','three2'),('4','four2'),('5','five2')]
    markup2=inline_keybord.create_keybord(buttons2)

    buttons3=[('1','one3'),('2','two3'),('3','three3'),('4','four3'),('5','five3')]
    markup3=inline_keybord.create_keybord(buttons3)

    buttons4=[('1','one4'),('2','two4'),('3','three4'),('4','four4'),('5','five4')]
    markup4=inline_keybord.create_keybord(buttons4)

    buttons5=[('1','one5'),('2','two5'),('3','three5'),('4','four5'),('5','five5')]
    markup5=inline_keybord.create_keybord(buttons5)

    buttons6=[('1','one6'),('2','two6'),('3','three6'),('4','four6'),('5','five6')]
    markup6=inline_keybord.create_keybord(buttons6)

    buttons7=[('1','one7'),('2','two7'),('3','three7'),('4','four7'),('5','five7')]
    markup7=inline_keybord.create_keybord(buttons7) 

    buttons8=[('1','one8'),('2','two8'),('3','three8'),('4','four8'),('5','five8')]
    markup8=inline_keybord.create_keybord(buttons8)

    buttons9=[('1','one9'),('2','two9'),('3','three9'),('4','four9'),('5','five9')]
    markup9=inline_keybord.create_keybord(buttons9)

    buttons10=[('1','one10'),('2','two10'),('3','three10'),('4','four10'),('5','five10')]
    markup10=inline_keybord.create_keybord(buttons10)
    
    buttons11=[('1','one11'),('2','two11'),('3','three11'),('4','four11'),('5','five11')]
    markup11=inline_keybord.create_keybord(buttons11)

    buttons12=[('1','one12'),('2','two12'),('3','three12'),('4','four12'),('5','five12')]
    markup12=inline_keybord.create_keybord(buttons12)

    buttons13=[('1','one13'),('2','two13'),('3','three13'),('4','four13'),('5','five13')]
    markup13=inline_keybord.create_keybord(buttons13)

    buttons14=[('1','one14'),('2','two14'),('3','three14'),('4','four14'),('5','five14')]
    markup14=inline_keybord.create_keybord(buttons14)

    buttons15=[('1','one15'),('2','two15'),('3','three15'),('4','four15'),('5','five15')]
    markup15=inline_keybord.create_keybord(buttons15)

    buttons16=[('1','one16'),('2','two16'),('3','three16'),('4','four16'),('5','five16')]
    markup16=inline_keybord.create_keybord(buttons16)

    buttons17=[('1','one17'),('2','two17'),('3','three17'),('4','four17'),('5','five17')]
    markup17=inline_keybord.create_keybord(buttons17)

    buttons18=[('1','one18'),('2','two18'),('3','three18'),('4','four18'),('5','five18')]
    markup18=inline_keybord.create_keybord(buttons18)

    buttons19=[('1','one19'),('2','two19'),('3','three19'),('4','four19'),('5','five19')]
    markup19=inline_keybord.create_keybord(buttons19)

    buttons20=[('1','one20'),('2','two20'),('3','three20'),('4','four20'),('5','five20')]
    markup20=inline_keybord.create_keybord(buttons20)

    buttons21=[('1','one21'),('2','two21'),('3','three21'),('4','four21'),('5','five21')]
    markup21=inline_keybord.create_keybord(buttons21)

    buttons22=[('1','one22'),('2','two22'),('3','three22'),('4','four22'),('5','five22')]
    markup22=inline_keybord.create_keybord(buttons22)

    buttons23=[('1','one23'),('2','two23'),('3','three23'),('4','four23'),('5','five23')]
    markup23=inline_keybord.create_keybord(buttons23)

    buttons24=[('1','one24'),('2','two24'),('3','three24'),('4','four24'),('5','five24')]
    markup24=inline_keybord.create_keybord(buttons24)

    buttons25=[('1','one25'),('2','two25'),('3','three25'),('4','four25'),('5','five25')]
    markup25=inline_keybord.create_keybord(buttons25)

    buttons26=[('1','one26'),('2','two26'),('3','three26'),('4','four26'),('5','five26')]
    markup26=inline_keybord.create_keybord(buttons26)

    buttons27=[('1','one27'),('2','two27'),('3','three27'),('4','four27'),('5','five27')]
    markup27=inline_keybord.create_keybord(buttons27)

    buttons28=[('1','one28'),('2','two28'),('3','three28'),('4','four28'),('5','five28')]
    markup28=inline_keybord.create_keybord(buttons28)

    buttons29=[('1','one29'),('2','two29'),('3','three29'),('4','four29'),('5','five29')]
    markup29=inline_keybord.create_keybord(buttons29)

    buttons30=[('1','one30'),('2','two30'),('3','three30'),('4','four30'),('5','five30')]
    markup30=inline_keybord.create_keybord(buttons30)

    buttons31=[('1','one31'),('2','two31'),('3','three31'),('4','four31'),('5','five31')]
    markup31=inline_keybord.create_keybord(buttons31)

    buttons32=[('1','one32'),('2','two32'),('3','three32'),('4','four32'),('5','five32')]
    markup32=inline_keybord.create_keybord(buttons32)

    buttons33=[('1','one33'),('2','two33'),('3','three33'),('4','four33'),('5','five33')]
    markup33=inline_keybord.create_keybord(buttons33)

    buttons34=[('1','one34'),('2','two34'),('3','three34'),('4','four34'),('5','five34')]
    markup34=inline_keybord.create_keybord(buttons34)

    if(callback.data == 'yes'):
        bot.send_message(callback.message.chat.id, f"Отлично!\n Напиши свою фамилию")
        name = callback.from_user.first_name
        bot.register_next_step_handler(callback.message, get_user_surname)
    elif (callback.data == 'no'):
        
        bot.send_message(callback.message.chat.id, f"Напиши свое имя")
        
        bot.register_next_step_handler(callback.message, get_user_name)
    elif callback.data=="ye":
                
        bot.edit_message_text(arr[0], callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    elif callback.data=="one" or callback.data=="two" or callback.data=="three" or callback.data=="four" or callback.data=="five":
                if callback.data=="one":
                    technozhr[0] += 1
                    technozhr[1] += 1
                elif callback.data=="two": 
                    technozhr[0] += 2
                    technozhr[1] += 2
                elif callback.data=="three": 
                    technozhr[0] += 3
                    technozhr[1] += 3
                elif callback.data=="four": 
                    technozhr[0] += 4
                    technozhr[1] += 4
                elif callback.data=="five": 
                    technozhr[0] += 5
                    technozhr[1] += 5
                          
                bot.edit_message_text(arr[1], callback.message.chat.id, callback.message.message_id, reply_markup=markup1)             
            
    elif callback.data=="one1" or callback.data=="two1" or callback.data=="three1" or callback.data=="four1" or callback.data=="five1":
                if callback.data=="one1":
                    technozhr[0] += 1
                    technozhr[2] += 1
                elif callback.data=="two1": 
                    technozhr[0] += 2
                    technozhr[2] += 2    
                elif callback.data=="three1":
                    technozhr[0] += 3
                    technozhr[2] += 3    
                elif callback.data=="four1":
                    technozhr[0] += 4
                    technozhr[2] += 4    
                elif callback.data=="five1": 
                    technozhr[0] += 5
                    technozhr[2] += 5    
                bot.edit_message_text(arr[2], callback.message.chat.id, callback.message.message_id, reply_markup=markup2)
                
    elif callback.data=="one2" or callback.data=="two2" or callback.data=="three2" or callback.data=="four2" or callback.data=="five2":
                if callback.data=="one2":
                    keep_soul[0] += 1
                    keep_soul[1] += 1
                elif callback.data=="two2": 
                    keep_soul[0] += 2
                    keep_soul[1] += 2  
                elif callback.data=="three2":
                    keep_soul[0] += 3
                    keep_soul[1] += 3    
                elif callback.data=="four2":
                    keep_soul[0] += 4
                    keep_soul[1] += 4   
                elif callback.data=="five2": 
                    keep_soul[0] += 5
                    keep_soul[1] += 5    
                bot.edit_message_text(arr[3], callback.message.chat.id, callback.message.message_id, reply_markup=markup3)

    elif callback.data=="one3" or callback.data=="two3" or callback.data=="three3" or callback.data=="four3" or callback.data=="five3":
                if callback.data=="one3":
                    alchemist[0] += 1
                    alchemist[1] += 1
                elif callback.data=="two3": 
                    alchemist[0] += 2
                    alchemist[1] += 2   
                elif callback.data=="three3":
                    alchemist[0] += 3
                    alchemist[1] += 3    
                elif callback.data=="four3":
                    alchemist[0] += 4
                    alchemist[1] += 4   
                elif callback.data=="five3": 
                    alchemist[0] += 5
                    alchemist[1] += 5    
                bot.edit_message_text(arr[4], callback.message.chat.id, callback.message.message_id, reply_markup=markup4)

    elif callback.data=="one4" or callback.data=="two4" or callback.data=="three4" or callback.data=="four4" or callback.data=="five4":
                if callback.data=="one4":
                    oracle[0] += 1
                    oracle[1] += 1
                elif callback.data=="two4": 
                    oracle[0] += 2
                    oracle[1] += 2
                elif callback.data=="three4":
                    oracle[0] += 3
                    oracle[1] += 3
                elif callback.data=="four4":
                    oracle[0] += 4
                    oracle[1] += 4   
                elif callback.data=="five4": 
                    oracle[0] += 5
                    oracle[1] += 5   
                bot.edit_message_text(arr[5], callback.message.chat.id, callback.message.message_id, reply_markup=markup5)

    elif callback.data=="one5" or callback.data=="two5" or callback.data=="three5" or callback.data=="four5" or callback.data=="five5":
                if callback.data=="one5":
                    technomag[0] += 1
                    technomag[1] += 1
                elif callback.data=="two5": 
                    technomag[0] += 2
                    technomag[1] += 2  
                elif callback.data=="three5":
                    technomag[0] += 3
                    technomag[1] += 3   
                elif callback.data=="four5":
                    technomag[0] += 4
                    technomag[1] += 4    
                elif callback.data=="five5": 
                    technomag[0] += 5
                    technomag[1] += 5  
                bot.edit_message_text(arr[6], callback.message.chat.id, callback.message.message_id, reply_markup=markup6)  

    elif callback.data=="one6" or callback.data=="two6" or callback.data=="three6" or callback.data=="four6" or callback.data=="five6":
                if callback.data=="one6":
                    keep_civil[0] += 1
                    keep_civil[1] += 1
                elif callback.data=="two6": 
                    keep_civil[0] += 2
                    keep_civil[1] += 2   
                elif callback.data=="three6":
                    keep_civil[0] += 3
                    keep_civil[1] += 3    
                elif callback.data=="four6":
                    keep_civil[0] += 4
                    keep_civil[1] += 4    
                elif callback.data=="five6": 
                    keep_civil[0] += 5
                    keep_civil[1] += 5    
                bot.edit_message_text(arr[7], callback.message.chat.id, callback.message.message_id, reply_markup=markup7)

    elif callback.data=="one7" or callback.data=="two7" or callback.data=="three7" or callback.data=="four7" or callback.data=="five7":
                if callback.data=="one7":
                    keep_civil[0] += 1
                    keep_civil[2] += 1
                elif callback.data=="two7": 
                    keep_civil[0] += 2
                    keep_civil[2] += 2   
                elif callback.data=="three7":
                    keep_civil[0] += 3
                    keep_civil[2] += 3    
                elif callback.data=="four7":
                    keep_civil[0] += 4
                    keep_civil[2] += 4    
                elif callback.data=="five7": 
                    keep_civil[0] += 5
                    keep_civil[2] += 5  
                bot.edit_message_text(arr[8], callback.message.chat.id, callback.message.message_id, reply_markup=markup8)  

    elif callback.data=="one8" or callback.data=="two8" or callback.data=="three8" or callback.data=="four8" or callback.data=="five8":
                if callback.data=="one8":
                    keep_soul[0] += 1
                    keep_soul[1] += 1
                elif callback.data=="two8": 
                    keep_soul[0] += 2
                    keep_soul[1] += 2   
                elif callback.data=="three8":
                    keep_soul[0] += 3
                    keep_soul[1] += 3    
                elif callback.data=="four8":
                    keep_soul[0] += 4
                    keep_soul[1] += 4    
                elif callback.data=="five8": 
                    keep_soul[0] += 5
                    keep_soul[1] += 5    
                bot.edit_message_text(arr[9], callback.message.chat.id, callback.message.message_id, reply_markup=markup9)

    elif callback.data=="one9" or callback.data=="two9" or callback.data=="three9" or callback.data=="four9" or callback.data=="five9":
                if callback.data=="one9":
                    keep_civil[0] += 1
                    keep_civil[3] += 1 
                elif callback.data=="two9": 
                    keep_civil[0] += 2
                    keep_civil[3] += 2 
                elif callback.data=="three9":
                    keep_civil[0] += 3
                    keep_civil[3] += 3    
                elif callback.data=="four9":
                    keep_civil[0] += 4
                    keep_civil[3] += 4     
                elif callback.data=="five9": 
                    keep_civil[0] += 5
                    keep_civil[3] += 5    
                bot.edit_message_text(arr[10], callback.message.chat.id, callback.message.message_id, reply_markup=markup10)

    elif callback.data=="one10" or callback.data=="two10" or callback.data=="three10" or callback.data=="four10" or callback.data=="five10":
                if callback.data=="one10":
                    keep_world[0] += 1
                    keep_world[1] += 1
                elif callback.data=="two10": 
                    keep_world[0] += 2
                    keep_world[1] += 2    
                elif callback.data=="three10":
                    keep_world[0] += 3
                    keep_world[1] += 3    
                elif callback.data=="four10":
                    keep_world[0] += 4
                    keep_world[1] += 4    
                elif callback.data=="five10": 
                    keep_world[0] += 5
                    keep_world[1] += 5   
                bot.edit_message_text(arr[11], callback.message.chat.id, callback.message.message_id, reply_markup=markup11)

    elif callback.data=="one11" or callback.data=="two11" or callback.data=="three11" or callback.data=="four11" or callback.data=="five11":
                if callback.data=="one11":
                    keep_world[0] += 1
                    keep_world[2] += 1
                elif callback.data=="two11": 
                    keep_world[0] += 2
                    keep_world[2] += 2  
                elif callback.data=="three11":
                    keep_world[0] += 3
                    keep_world[2] += 3   
                elif callback.data=="four11":
                    keep_world[0] += 4
                    keep_world[2] += 4    
                elif callback.data=="five11": 
                    keep_world[0] += 5
                    keep_world[2] += 5    
                bot.edit_message_text(arr[12], callback.message.chat.id, callback.message.message_id, reply_markup=markup12)

    elif callback.data=="one12" or callback.data=="two12" or callback.data=="three12" or callback.data=="four12" or callback.data=="five12":
                if callback.data=="one12":
                    oracle[0] += 1
                    oracle[2] += 1
                elif callback.data=="two12": 
                    oracle[0] += 2
                    oracle[2] += 2    
                elif callback.data=="three12":
                    oracle[0] += 3
                    oracle[2] += 3    
                elif callback.data=="four12":
                    oracle[0] += 4
                    oracle[2] += 4   
                elif callback.data=="five12": 
                    oracle[0] += 5
                    oracle[2] += 5
                bot.edit_message_text(arr[13], callback.message.chat.id, callback.message.message_id, reply_markup=markup13)

    elif callback.data=="one13" or callback.data=="two13" or callback.data=="three13" or callback.data=="four13" or callback.data=="five13":
                if callback.data=="one13":
                    oracle[0] += 1
                    oracle[3] += 1
                elif callback.data=="two13": 
                    oracle[0] += 2
                    oracle[3] += 2   
                elif callback.data=="three13":
                    oracle[0] += 3
                    oracle[3] += 3    
                elif callback.data=="four13":
                    oracle[0] += 4
                    oracle[3] += 4    
                elif callback.data=="five13": 
                    oracle[0] += 5
                    oracle[3] += 5    
                bot.edit_message_text(arr[14], callback.message.chat.id, callback.message.message_id, reply_markup=markup14)

    elif callback.data=="one14" or callback.data=="two14" or callback.data=="three14" or callback.data=="four14" or callback.data=="five14":
                if callback.data=="one14":
                    technozhr[0] += 1
                    technozhr[3] += 1
                elif callback.data=="two14": 
                    technozhr[0] += 2
                    technozhr[3] += 2   
                elif callback.data=="three14":
                    technozhr[0] += 3
                    technozhr[3] += 3    
                elif callback.data=="four14":
                    technozhr[0] += 4
                    technozhr[3] += 4    
                elif callback.data=="five14": 
                    technozhr[0] += 5
                    technozhr[3] += 5    
                bot.edit_message_text(arr[15], callback.message.chat.id, callback.message.message_id, reply_markup=markup15)

    elif callback.data=="one15" or callback.data=="two15" or callback.data=="three15" or callback.data=="four15" or callback.data=="five15":
                if callback.data=="one15":
                    alchemist[0] += 1
                    alchemist[2] += 1
                elif callback.data=="two15": 
                    alchemist[0] += 2
                    alchemist[2] += 2    
                elif callback.data=="three15":
                    alchemist[0] += 3
                    alchemist[2] += 3
                elif callback.data=="four15":
                    alchemist[0] += 4
                    alchemist[2] += 4
                elif callback.data=="five15": 
                    alchemist[0] += 5
                    alchemist[2] += 5
                bot.edit_message_text(arr[16], callback.message.chat.id, callback.message.message_id, reply_markup=markup16)

    elif callback.data=="one16" or callback.data=="two16" or callback.data=="three16" or callback.data=="four16" or callback.data=="five16":
                if callback.data=="one16":
                    alchemist[0] += 1
                    alchemist[3] += 1
                elif callback.data=="two16": 
                    alchemist[0] += 2
                    alchemist[3] += 2
                elif callback.data=="three16":
                    alchemist[0] += 3
                    alchemist[3] += 3
                elif callback.data=="four16":
                    alchemist[0] += 4
                    alchemist[3] += 4
                elif callback.data=="five16": 
                    alchemist[0] += 5
                    alchemist[3] += 5
                bot.edit_message_text(arr[17], callback.message.chat.id, callback.message.message_id, reply_markup=markup17)

    elif callback.data=="one17" or callback.data=="two17" or callback.data=="three17" or callback.data=="four17" or callback.data=="five17":
                if callback.data=="one17":
                    alchemist[0] += 1
                    alchemist[4] += 1
                elif callback.data=="two17": 
                    alchemist[0] += 2
                    alchemist[4] += 2   
                elif callback.data=="three17":
                    alchemist[0] += 3
                    alchemist[4] += 3   
                elif callback.data=="four17":
                    alchemist[0] += 4
                    alchemist[4] += 4    
                elif callback.data=="five17": 
                    alchemist[0] += 5
                    alchemist[4] += 5   
                bot.edit_message_text(arr[18], callback.message.chat.id, callback.message.message_id, reply_markup=markup18)

    elif callback.data=="one18" or callback.data=="two18" or callback.data=="three18" or callback.data=="four18" or callback.data=="five18":
                if callback.data=="one18":
                    technozhr[0] += 1
                    technozhr[4] += 1
                elif callback.data=="two18": 
                    technozhr[0] += 2
                    technozhr[4] += 2   
                elif callback.data=="three18":
                    technozhr[0] += 3
                    technozhr[4] += 3    
                elif callback.data=="four18":
                    technozhr[0] += 4
                    technozhr[4] += 4   
                elif callback.data=="five18": 
                    technozhr[0] += 5
                    technozhr[4] += 5    
                bot.edit_message_text(arr[19], callback.message.chat.id, callback.message.message_id, reply_markup=markup19)

    elif callback.data=="one19" or callback.data=="two19" or callback.data=="three19" or callback.data=="four19" or callback.data=="five19":
                if callback.data=="one19":
                    keep_soul[0] += 1
                    keep_soul[3] += 1
                elif callback.data=="two19": 
                    keep_soul[0] += 2
                    keep_soul[3] += 2    
                elif callback.data=="three19":
                    keep_soul[0] += 3
                    keep_soul[3] += 3    
                elif callback.data=="four19":
                    keep_soul[0] += 4
                    keep_soul[3] += 4   
                elif callback.data=="five19": 
                    keep_soul[0] += 5
                    keep_soul[3] += 5    
                bot.edit_message_text(arr[20], callback.message.chat.id, callback.message.message_id, reply_markup=markup20)

    elif callback.data=="one20" or callback.data=="two20" or callback.data=="three20" or callback.data=="four20" or callback.data=="five20":
                if callback.data=="one20":
                    technomag[0] += 1
                    technomag[2] += 1
                elif callback.data=="two20": 
                    technomag[0] += 2
                    technomag[2] += 2   
                elif callback.data=="three20":
                    technomag[0] += 3
                    technomag[2] += 3    
                elif callback.data=="four20":
                    technomag[0] += 4
                    technomag[2] += 4    
                elif callback.data=="five20": 
                    technomag[0] += 5
                    technomag[2] += 5    
                bot.edit_message_text(arr[21], callback.message.chat.id, callback.message.message_id, reply_markup=markup21)

    elif callback.data=="one21" or callback.data=="two21" or callback.data=="three21" or callback.data=="four21" or callback.data=="five21":
                if callback.data=="one21":
                    technomag[0] += 1
                    technomag[3] += 1
                elif callback.data=="two21": 
                    technomag[0] += 2
                    technomag[3] += 2    
                elif callback.data=="three21":
                    technomag[0] += 3
                    technomag[3] += 3    
                elif callback.data=="four21":
                    technomag[0] += 4
                    technomag[3] += 4    
                elif callback.data=="five21": 
                    technomag[0] += 5
                    technomag[3] += 5    
                bot.edit_message_text(arr[22], callback.message.chat.id, callback.message.message_id, reply_markup=markup22)

    elif callback.data=="one22" or callback.data=="two22" or callback.data=="three22" or callback.data=="four22" or callback.data=="five22":
                if callback.data=="one22":
                    oracle[0] += 1
                    oracle[4] += 1
                elif callback.data=="two22": 
                    oracle[0] += 2
                    oracle[4] += 2
                elif callback.data=="three22":
                    oracle[0] += 3
                    oracle[4] += 3    
                elif callback.data=="four22":
                    oracle[0] += 4
                    oracle[4] += 4    
                elif callback.data=="five22": 
                    oracle[0] += 5
                    oracle[4] += 5    
                bot.edit_message_text(arr[23], callback.message.chat.id, callback.message.message_id, reply_markup=markup23) 

    elif callback.data=="one23" or callback.data=="two23" or callback.data=="three23" or callback.data=="four23" or callback.data=="five23":
                if callback.data=="one23":
                    keep_civil[0] += 1
                    keep_civil[4] += 1
                elif callback.data=="two23": 
                    keep_civil[0] += 2
                    keep_civil[4] += 2    
                elif callback.data=="three23":
                    keep_civil[0] += 3
                    keep_civil[4] += 3    
                elif callback.data=="four23":
                    keep_civil[0] += 4
                    keep_civil[4] += 4    
                elif callback.data=="five23": 
                    keep_civil[0] += 5
                    keep_civil[4] += 5    
                bot.edit_message_text(arr[24], callback.message.chat.id, callback.message.message_id, reply_markup=markup24)

    elif callback.data=="one24" or callback.data=="two24" or callback.data=="three24" or callback.data=="four24" or callback.data=="five24":
                if callback.data=="one24":
                    keep_civil[0] += 1
                    keep_civil[5] += 1
                elif callback.data=="two24": 
                    keep_civil[0] += 2
                    keep_civil[5] += 2    
                elif callback.data=="three24":
                    keep_civil[0] += 3
                    keep_civil[5] += 3    
                elif callback.data=="four24":
                    keep_civil[0] += 4
                    keep_civil[5] += 4    
                elif callback.data=="five24": 
                    keep_civil[0] += 5
                    keep_civil[5] += 5    
                bot.edit_message_text(arr[25], callback.message.chat.id, callback.message.message_id, reply_markup=markup25)

    elif callback.data=="one25" or callback.data=="two25" or callback.data=="three25" or callback.data=="four25" or callback.data=="five25":
                if callback.data=="one25":
                    keep_soul[0] += 1
                    keep_soul[4] += 1
                elif callback.data=="two25": 
                    keep_soul[0] += 2
                    keep_soul[4] += 2    
                elif callback.data=="three25":
                    keep_soul[0] += 3
                    keep_soul[4] += 3    
                elif callback.data=="four25":
                    keep_soul[0] += 4
                    keep_soul[4] += 4    
                elif callback.data=="five25": 
                    keep_soul[0] += 5
                    keep_soul[4] += 5    
                bot.edit_message_text(arr[26], callback.message.chat.id, callback.message.message_id, reply_markup=markup26)

    elif callback.data=="one26" or callback.data=="two26" or callback.data=="three26" or callback.data=="four26" or callback.data=="five26":
                if callback.data=="one26":
                    keep_world[0] += 1
                    keep_world[3] += 1
                elif callback.data=="two26": 
                    keep_world[0] += 2
                    keep_world[3] += 2    
                elif callback.data=="three26":
                    keep_world[0] += 3
                    keep_world[3] += 3    
                elif callback.data=="four26":
                    keep_world[0] += 4
                    keep_world[3] += 4    
                elif callback.data=="five26": 
                    keep_world[0] += 5
                    keep_world[3] += 5    
                bot.edit_message_text(arr[27], callback.message.chat.id, callback.message.message_id, reply_markup=markup27)

    elif callback.data=="one27" or callback.data=="two27" or callback.data=="three27" or callback.data=="four27" or callback.data=="five27":
                if callback.data=="one27":
                    oracle[0] += 1
                    oracle[5] += 1
                elif callback.data=="two27": 
                    oracle[0] += 2
                    oracle[5] += 2    
                elif callback.data=="three27":
                    oracle[0] += 3
                    oracle[5] += 3    
                elif callback.data=="four27":
                    oracle[0] += 4
                    oracle[5] += 4    
                elif callback.data=="five27": 
                    oracle[0] += 5
                    oracle[5] += 5   
                bot.edit_message_text(arr[28], callback.message.chat.id, callback.message.message_id, reply_markup=markup28) 

    elif callback.data=="one28" or callback.data=="two28" or callback.data=="three28" or callback.data=="four28" or callback.data=="five28":
                if callback.data=="one28":
                    keep_world[0] += 1
                    keep_world[4] += 1
                elif callback.data=="two28": 
                    keep_world[0] += 2
                    keep_world[4] += 2    
                elif callback.data=="three28":
                    keep_world[0] += 3
                    keep_world[4] += 3       
                elif callback.data=="four28":
                    keep_world[0] += 4
                    keep_world[4] += 4       
                elif callback.data=="five28": 
                    keep_world[0] += 5
                    keep_world[4] += 5    
                bot.edit_message_text(arr[29], callback.message.chat.id, callback.message.message_id, reply_markup=markup29)   

    elif callback.data=="one29" or callback.data=="two29" or callback.data=="three29" or callback.data=="four29" or callback.data=="five29":
                if callback.data=="one29":
                    technomag[0] += 1
                    technomag[4] += 1
                elif callback.data=="two29": 
                    technomag[0] += 2
                    technomag[4] += 2    
                elif callback.data=="three29":
                    technomag[0] += 3
                    technomag[4] += 3    
                elif callback.data=="four29":
                    technomag[0] += 4
                    technomag[4] += 4    
                elif callback.data=="five29": 
                    technomag[0] += 5
                    technomag[4] += 5   
                bot.edit_message_text(arr[30], callback.message.chat.id, callback.message.message_id, reply_markup=markup30) 

    elif callback.data=="one30" or callback.data=="two30" or callback.data=="three30" or callback.data=="four30" or callback.data=="five30":
                if callback.data=="one30":
                    keep_world[0] += 1
                    keep_world[5] += 1
                elif callback.data=="two30": 
                    keep_world[0] += 2
                    keep_world[5] += 2    
                elif callback.data=="three30":
                    keep_world[0] += 3
                    keep_world[5] += 3    
                elif callback.data=="four30":
                    keep_world[0] += 4
                    keep_world[5] += 4    
                elif callback.data=="five30": 
                    keep_world[0] += 5
                    keep_world[5] += 5   
                bot.edit_message_text(arr[31], callback.message.chat.id, callback.message.message_id, reply_markup=markup31)  

    elif callback.data=="one31" or callback.data=="two31" or callback.data=="three31" or callback.data=="four31" or callback.data=="five31":
                if callback.data=="one31":
                    keep_soul[0] += 1
                    keep_soul[5] += 1
                elif callback.data=="two31": 
                    keep_soul[0] += 2
                    keep_soul[5] += 2    
                elif callback.data=="three31":
                    keep_soul[0] += 3
                    keep_soul[5] += 3    
                elif callback.data=="four31":
                    keep_soul[0] += 4
                    keep_soul[5] += 4    
                elif callback.data=="five31": 
                    keep_soul[0] += 5
                    keep_soul[5] += 5    
                bot.edit_message_text(arr[32], callback.message.chat.id, callback.message.message_id, reply_markup=markup32)

    elif callback.data=="one32" or callback.data=="two32" or callback.data=="three32" or callback.data=="four32" or callback.data=="five32":
                if callback.data=="one32":
                    technomag[0] += 1
                    technomag[5] += 1
                elif callback.data=="two32": 
                    technomag[0] += 2
                    technomag[5] += 2    
                elif callback.data=="three32":
                    technomag[0] += 3
                    technomag[5] += 3    
                elif callback.data=="four32":
                    technomag[0] += 4
                    technomag[5] += 4    
                elif callback.data=="five32": 
                    technomag[0] += 5
                    technomag[5] += 5    
                bot.edit_message_text(arr[33], callback.message.chat.id, callback.message.message_id, reply_markup=markup33)
        
    elif callback.data=="one33" or callback.data=="two33" or callback.data=="three33" or callback.data=="four33" or callback.data=="five33":
                if callback.data=="one33":
                    alchemist[0] += 1
                    alchemist[5] += 1
                elif callback.data=="two33": 
                    alchemist[0] += 2
                    alchemist[5] += 2   
                elif callback.data=="three33":
                    alchemist[0] += 3
                    alchemist[5] += 3    
                elif callback.data=="four33":
                    alchemist[0] += 4
                    alchemist[5] += 4    
                elif callback.data=="five33": 
                    alchemist[0] += 5
                    alchemist[5] += 5  
                bot.edit_message_text(arr[34], callback.message.chat.id, callback.message.message_id, reply_markup=markup34)

    elif callback.data=="one34" or callback.data=="two34" or callback.data=="three34" or callback.data=="four34" or callback.data=="five34":
                if callback.data=="one34":
                    technozhr[0] += 1
                    technozhr[5] += 1
                elif callback.data=="two34": 
                    technozhr[0] += 2
                    technozhr[5] += 2    
                elif callback.data=="three34":
                    technozhr[0] += 3
                    technozhr[5] += 3    
                elif callback.data=="four34":
                    technozhr[0] += 4
                    technozhr[5] += 4    
                elif callback.data=="five34": 
                    technozhr[0] += 5
                    technozhr[5] += 5    

                result = ["", "", ""]
                arr2 = [technozhr[0], keep_soul[0], alchemist[0], oracle[0], technomag[0], keep_civil[0], keep_world[0]]
                f = arr2.index(max(arr2)) 
                
                technozhr[0] = -1
                keep_soul[0] = -1
                alchemist[0] = -1
                oracle[0] = -1
                technomag[0] = -1
                keep_civil[0] = -1
                keep_world[0] = -1
                
                direct = 0
                     
                if f == 0:
                    result[0] = "Техножрец"
                    direct = technozhr.index(max(technozhr))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Техномаги и техножрецы живут среди машин. Они создают внутри Вселенной отдельный мир машин и механизмов. Техножрецы - настоящие заклинатели и хранители машин. Они делают реальным то, что техномаги придумали и нарисовали, но только техножрецы знают, на какие кнопки нажать, чтобы машина заработала как надо. Техножрецы живут в кузницах и мастерских, в которых собирают машины и механизмы, чинят их, совершенствуют и управляют ими. Машины для них как дети, они заботятся о них, учат их говорить, общаться друг с другом и с жителями Вселенной. Техножрецы могут говорить с машинами на одном языке и создавать заклинания, которые позволяют жителям Вселенной отдавать им команды."
                elif f == 1:
                    result[0] = "Хранитель души" 
                    direct = keep_soul.index(max(keep_soul))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Хранители души и тела живут в уютных домиках на окраинах селений. К ним приходят жители Вселенной, когда им нужна помощь в излечении или укреплении их духа и тела. Только они знают, как устроен человек и его внутренний мир, могут помочь разобраться в себе и других, сохранить любовь и взаимопонимание в семьях, гармонично развить личность ребенка. Иногда хранители души выходят из своих домиков, идут на ярмарочную площадь, где рассказывают и обучают жителей Вселенной тому, как и детям, и взрослым быть здоровыми, активными и счастливыми."
                elif f == 2:
                    result[0] = "Алхимик" 
                    direct = alchemist.index(max(alchemist))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Алхимики живут в лабораториях на окраине Вселенной, наполненных аккуратно расставленными пробирками, колбами, реактивами и измерительными приборами (которые иногда представляют собой целое здание). Их влечет к познанию основ мироздания. Они исследуют, как и из чего создан этот мир от самых маленьких частиц до звезд и устройства Вселенной, по каким законам он работает, а потом разбирают его “по кирпичикам”, чтобы сделать из найденных веществ разные интересные материалы, которые пригодятся жителям Вселенной."
                elif f == 3:
                    result[0] = "Оракул" 
                    direct = oracle.index(max(oracle))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Оракулы - повелители чисел, они живут в небесных башнях на пересечении потоков информации, порождаемой жителями Вселенной, где черпают данные для своих предсказаний, которые очень нужны жителям Вселенной."
                elif f == 4:
                    result[0] = "Техномаг" 
                    direct = technomag.index(max(technomag))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Техномаги и техножрецы живут среди машин. Они создают внутри Вселенной отдельный мир машин и механизмов. Техномаги находят себе тихий уголок, где можно день и ночь в одиночестве мечтать о новых машинах и механизмах, придумывать и рисовать их "
                elif f == 5:
                    result[0] = "Хранитель цивилизации" 
                    direct = keep_civil.index(max(keep_civil))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Хранители цивилизации живут среди людей, наблюдают за тем, чего им не хватает, а потом идут в далекие земли, где живут в палатках и добывают ресурсы для развития цивилизации. Они возводят города, охраняют и оберегают природу, следят за разумным использованием добытых ресурсов для того, чтобы всем жителям Вселенной хватило тепла, энергии, еды и чистой воды, миру машин - топлива, а человеческая цивилизация продолжала существовать и не погибла из-за того, что во Вселенной закончились ресурсы и её переполнило отходами."
                elif f == 6:
                    result[0] = "Хранитель мира"
                    direct = keep_world.index(max(keep_world))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Жители Вселенной, представители разных гильдий живут бок о бок, обмениваются полезной информацией и произведенными товарами, а иногда конкурируют и спорят друг с другом из-за территории и ресурсов. Часто им бывает сложно договориться между собой, потому что у них противоположные интересы или говорят они на разных языках. Жители Вселенной для того, чтобы сохранить мир и понять друг друга, зовут на помощь хранителей мира, которые живут среди людей и стараются быть как можно ближе к ним. Только они могут найти общий язык с любым человеком, понять его, помочь людям договориться, обойти острые углы, совершить выгодные сделки и защитить интересы каждого."


                bot.send_message(callback.message.chat.id, f"Ты {result[0]}! {result[2]} \n\n Твоё направление: {result[1]}")
                faculty = result[0]
                direction = result[1]
                #db_table_val(user_id=us_id, user_name=name, user_surname=surname, email=email, city=city, school=school, faculty=faculty, phone=phone, direction=direction)
                update_db_table(faculty=faculty, direction=direction, user_id=callback.message.chat.id)
                
                
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton("Да", callback_data = 'ye')
                markup.row(btn1)
                bot.send_message(callback.message.chat.id, 'Хочешь пройти заново?',  reply_markup= markup)
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                
                

    elif callback.data=="n":
                bot.send_message(callback.message.chat.id, "Зачем ты тогда пришел?")



@bot.message_handler(content_types=['text'])
def get_user_name(message):
    global name 
    bot.send_message(message.chat.id, "Пожалуйста, введи свою фамилию", parse_mode = 'html')
    bot.register_next_step_handler(message, get_user_surname)

def get_user_surname(message):
    bot.send_message(message.chat.id, "Пожалуйста, введи свою почту", parse_mode = 'html')
    global surname
    surname = message.text
    surname = surname
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    bot.send_message(message.chat.id, "Пожалуйста, напиши название твоего населённого пункта", parse_mode = 'html')    
    global email  
    email = message.text
    email=email
    bot.register_next_step_handler(message, get_city)

def get_city(message):
    bot.send_message(message.chat.id, "Пожалуйста, введи номер твоей школы", parse_mode = 'html')
    global city
    city = message.text
    city=city
    bot.register_next_step_handler(message, get_school)

def get_school(message):
    bot.send_message(message.chat.id, "И напоследок, напиши номер своего телефона", parse_mode = 'html')
    global school 
    school = message.text
    school=school
    bot.register_next_step_handler(message, get_number)
    
def get_number(message):
    global phone
    global us_id
    global name
    global school
    global email
    global city
    us_id = message.from_user.id
    us_id = us_id
    phone = message.text
    phone = phone
    db_table_val(user_id= message.chat.id, user_name=name, user_surname=surname, email=email, city=city, school=school, phone=phone)
    markup0=types.InlineKeyboardMarkup(row_width=2)
    item1=types.InlineKeyboardButton("Да", callback_data="ye")
    item2=types.InlineKeyboardButton("Нет", callback_data="n")
    markup0.add(item1, item2)
    bot.send_message(message.chat.id, "Ты готов ответить на несколько вопросов".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup0)

bot.polling(non_stop=True)

