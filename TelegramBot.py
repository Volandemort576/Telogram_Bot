import telebot
from telebot import types
import news_api
import weather_api

bot = telebot.TeleBot('5549730577:AAHHRHzq0Y6E4Dt9Q8pAg2E7VuxuA5zIENs')

commands = ['/start', '/help']

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
    btn7 = types.KeyboardButton(text='Установи город для погоды')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
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
    bot.send_message(message.chat.id, 'введите название города\r\nНапример "\S Moscow"\r\nОбратите внимание на язык')


@bot.message_handler(func=lambda message: message.text.split()[0] == '\S')
def wither_city(message):
    global city, mess

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn)
    bot.send_message(message.chat.id, 'Город принят', reply_markup=kb)

    mess = message.text.split()[1]
    try:
        city = mess
    except:
        bot.send_message(message.chat.id, 'Повторите еще раз')


@bot.message_handler(func=lambda message: message.text == 'Покажи новости')
def news(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Вперед')
    btn2 = types.KeyboardButton(text='В начало')
    btn3 = types.KeyboardButton(text='Показать прошлое меню')
    kb.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Нажмите на какую-нибудь кнопку.\n\rЕсли нашли новости украинcкой пропоганды, то напишите например:\n\r"/black_list https://site.com/"', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text.split()[0] == '/black_list')
def black_list(message):
    message = message.text.split()[1]
    lst = list()

    with open('proverka.txt') as file:
        for line in file:
            if len(line) != 0:
                lst.append(line)
            else:
                continue

    lst.append(message)
    index = len(lst) - 1

    count = 0
    with open('proverka.txt', 'w') as file:
        for word in lst:
            if count != index:
                file.write(word)
            else:
                file.write(f'\n{word}')
            count += 1


@bot.message_handler(func=lambda message: message.text == 'Вперед')
def cont(message):
    global index

    news = news_api.get_news()
    index += 1
    try:
        bot.send_message(message.chat.id, news[index])
    except:
        bot.send_message(message.chat.id, f'Кажется новости закончились')


@bot.message_handler(func=lambda message: message.text == 'В начало')
def reset(message):
    global index

    news = news_api.get_news()
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
    bot.polling()
except Exception as error:
    print(f'Ошибка. Подробности: {error}')