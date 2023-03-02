import telebot
from telebot import types

from news_api import get_news
from weather_api import get_weather
from database_ADMIN import DataBase_a
from database_CLIENT import DataBase_c

bot = telebot.TeleBot('5549730577:AAHHRHzq0Y6E4Dt9Q8pAg2E7VuxuA5zIENs')

commands = ['/start', '/help', '/admin']

city = str()
index = -1


@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == 'Да, покажи мне их')
@bot.message_handler(func=lambda message: message.text == 'Покажи команды')
def help(message):
    count = 1
    s = 'Команды'
    for command in commands:
        s += f'\n\r{count}.{command}'
        count += 1
    bot.send_message(message.chat.id, s)


@bot.message_handler(func=lambda message: message.text == 'Нет, спасибо')
def cont(message):
    kb = kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='Нет')
    btn2 = types.KeyboardButton(text='ДА!')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Тогда показать следующее меню?', reply_markup=kb)


@bot.message_handler(commands=['start'])
def start(message):
    kb = kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='Да, покажи мне их')
    btn2 = types.KeyboardButton(text='Нет, спасибо')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, я тестовый бот, спасибо что ты пришел со мной поговорить!\n\rПоказать команды?', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'ДА!')
@bot.message_handler(func=lambda message: message.text == 'Привет')
@bot.message_handler(func=lambda message: message.text == 'Показать прошлое меню')
def hello(message):
    global index

    index = -1

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Что ты умеешь?')
    btn2 = types.KeyboardButton(text='Пока!')
    btn3 = types.KeyboardButton(text='Хочу халявные игры!')
    btn4 = types.KeyboardButton(text='Покажи команды')
    btn5 = types.KeyboardButton(text='Покажи новости')
    btn6 = types.KeyboardButton(text='Покажи погоду')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Привет! Чем я могу помочь?', reply_markup=kb) 


######################     CLIENT     ##########################
@bot.message_handler(func=lambda message: message.text == 'Показать прошлое меню')
@bot.message_handler(func=lambda message: message.text == 'Покажи погоду')
def iteam_db(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    db = DataBase_c()
    for button in db:
        kb.add(types.KeyboardButton(text=f'/city {button}'))

    bot.send_message(message.chat.id, '<Выберите город>\n\rДля добавления города обращайтесь на мой email:\n\rsanek1080p@gmail.com', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text.split()[0] == '/city')
def weather(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)

    try:
        city = message.text.split()[1]
        weather = get_weather(city)
        bot.send_message(message.chat.id, weather, reply_markup=kb)
    except:
        bot.send_message(message.chat.id, 'Ошибка', )
######################     CLIENT     ##########################


######################     ADMIN     ##########################
@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(message.chat.id, 'admin_1 - Посмотреть данные\n'
                                      'admin_2 - Добавить данные\n\r'
                                      'admin_3 - Удалить данные\n\r\n\r'
                                      'Как записывать:\n\r'
                                      'admin_1 - /admin_1 введите пароль \n\r\n\r'
                                      'admin_2 - /admin_2 пароль и название города (ENG) \n\r\n\r'
                                      'admin_3 - /admin_3 пароль и id города \n\r\n\r'
                                      'Будьте осторожны с командами!')


@bot.message_handler(func=lambda message: message.text.split()[0] == '/admin_1')
def admin_1(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    try: 
        password = message.text.split()[1]
        db = DataBase_a(password, 1)
        bot.send_message(message.chat.id, db, reply_markup=kb)
    except:
        bot.send_message(message.chat.id, 'Ошибка')


@bot.message_handler(func=lambda message: message.text.split()[0] == '/admin_2')
def admin_2(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    try:
        password = message.text.split()[1]
        data = message.text.split()[2]
        db = DataBase_a(password, 2, data)
        bot.send_message(message.chat.id, db, reply_markup=kb)
    except:
        bot.send_message(message.chat.id, 'Ошибка')


@bot.message_handler(func=lambda message: message.text.split()[0] == '/admin_3')
def admin_3(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    try:
        password = message.text.split()[1]
        id = message.text.split()[2]
        db = DataBase_a(password, 3, id=id)
        bot.send_message(message.chat.id, db, reply_markup=kb)
    except:
        bot.send_message(message.chat.id, 'Ошибка')
######################     ADMIN     ##########################


@bot.message_handler(func=lambda message: message.text == 'Покажи новости')
def news(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Вперед')
    btn2 = types.KeyboardButton(text='В начало')
    btn3 = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Нажмите на какую-нибудь кнопку."', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Вперед')
def cont(message):
    global index

    news = get_news()
    index += 1
    try:
        bot.send_message(message.chat.id, news[index])
    except:
        bot.send_message(message.chat.id, f'Кажется новости закончились')


@bot.message_handler(func=lambda message: message.text == 'В начало')
def reset(message):
    global index

    news = get_news()
    index = 0
    bot.send_message(message.chat.id, news[index])


@bot.message_handler(func=lambda message: message.text == 'Что ты умеешь?')
def help(message):
    bot.send_message(message.chat.id, 'Я умею тратить ресурсы сервера ;)')


@bot.message_handler(func=lambda message: message.text == 'Пока!')
def good_bye(message):
    bot.send_message(message.chat.id, message.text)
    exit()


@bot.message_handler(func=lambda message: message.text == 'Хочу халявные игры!')
def site(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton(text='Сайт', url='https://s5.torrent-repack.club/')
    kb.add(btn)

    bot.send_message(message.chat.id, 'Лови', reply_markup=kb)


try:
    bot.polling(none_stop=True)
except Exception as error:
    print(f'Ошибка. Подробности: {error}')