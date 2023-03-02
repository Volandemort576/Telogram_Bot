import requests


def get_weather(city):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOU APPID',
                       params={'units': 'metric', 'lang': 'ru'})
    data = res.json()
    try:
        cond = "Осадки: ", str(data['weather'][0]['description'])
        cond = ' '.join(cond)

        temp = "Температура:", str(data['main']['temp'])
        temp = ' '.join(temp)

        temp_min = "Минимальная температура:", str(data['main']['temp_min'])
        temp_min = ' '.join(temp_min)

        temp_max = "Максимальная температура:", str(data['main']['temp_max'])
        temp_max = ' '.join(temp_max)
    except Exception as error:
        return f'Что-то пошло не так :( ({error})'
    return f'Погода в {city}:\n\r{cond}\n\r{temp}\n\r{temp_min}\n\r{temp_max}'
