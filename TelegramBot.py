import telebot
from telebot import types
import news_api
import weather_api

bot = telebot.TeleBot('5549730577:AAHHRHzq0Y6E4Dt9Q8pAg2E7VuxuA5zIENs')

commands = ['/start', '/help']

city = str()


@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == 'Да, покажи мне их')
@bot.message_handler(func=lambda message: message.text == 'Покажи команды')
def help(message):
    bot.send_message(message.chat.id, 'Команды:')
    count = 1
    for command in commands:
        bot.send_message(message.chat.id, f'{count}.{command}')
        count += 1


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
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Что ты умеешь?')
    btn2 = types.KeyboardButton(text='Пока!')
    btn3 = types.KeyboardButton(text='Хочу халявные игры!')
    btn4 = types.KeyboardButton(text='Добавить меня в другой чат')
    btn5 = types.KeyboardButton(text='Покажи команды')
    btn6 = types.KeyboardButton(text='Покажи новости')
    btn7 = types.KeyboardButton(text='Покажи погоду')
    btn8 = types.KeyboardButton(text='Установи город для погоды')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id, 'Привет! Чем я могу помочь?', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Покажи погоду')
def get_with(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)

    weather = weather_api.get_weather(city)
    bot.send_message(message.chat.id, weather, reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Установи город для погоды')
def mess(message):
    bot.send_message(message.chat.id, 'введите название города\r\nНапример "Город Moscow"\r\nОбратите внимание на язык')


@bot.message_handler(func=lambda message: message.text.split()[0] == 'Город')
def wither_city(message):
    global city, mess

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    bot.send_message(message.chat.id, 'Город принят', reply_markup=kb)

    try:
        mess = message.text.split()[1]
    except: bot.send_message(message.caht.id, 'Ошибка')
    city = mess


@bot.message_handler(func=lambda message: message.text == 'Покажи новости')
def news(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    s = ''
    news = news_api.get_news()
    for key, val in news.items():
        s += f'{val}\r\n'
    bot.send_message(message.chat.id, s, reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Добавить меня в другой чат')
def switch(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Выберите чат', switch_inline_query='/Привет')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Выберите чат', reply_markup=markup)



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
    bot.polling()
except Exception as error:
    print(f'Ошибка. Подробности: {error}')
