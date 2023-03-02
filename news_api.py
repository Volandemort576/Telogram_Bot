import json
import requests


def get_news():
    pack = list()

    res = requests.get("https://newsapi.org/v2/top-headlines?",
                       params={'language': 'ru', 'country': 'ru', 'apiKey': 'YOU APIKEY'}).text

    info = json.loads(res)
    for key, val in list(info.items()):
        if key == 'articles':
            for news in val:
                pack.append(f'Заголовок:\n\r {news["title"]}\n\r\n\r'
                            f'Информация:\n\r {news["description"]}\n\r\n\r'
                            f'Подробнее:\n\r {news["url"]}')

    return pack
