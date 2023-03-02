import json
import re
import requests


def get_news():
    pack = list()

    res = requests.get("https://newsapi.org/v2/top-headlines?",
                       params={'language': 'ru', 'country': 'ru', 'apiKey': 'YOU APIKEY'}).text

    info = json.loads(res)
    for key, val in list(info.items()):
        if key == 'articles':
            for news in val:
                if not re.search('^https://news.liga.net/', news['url']) and \
                        not re.search('^https://www.unian.net/', news['url'])and \
                        not re.search('^https://meduza.io/', news['url']):
                    pack.append(f'Заголовок:\n\r {news["title"]}\n\r\n\rИнформация:\n\r {news["description"]}\n\r\n\rПодробнее:\n\r {news["url"]}')

    return pack
