import json
import re
import requests
import colorama as color


color.init(autoreset=True)

def get_news():
    pack = list()

    res = requests.get("https://newsapi.org/v2/top-headlines?",
                       params={'language': 'ru', 'country': 'ru', 'apiKey': '7248b8a39f3d471581e5397cfd3f3459'}).text

    info = json.loads(res)
    for key, val in list(info.items()):
        if key == 'articles':
            for news in val:
                if not re.search('^https://news.liga.net/', news['url']) and \
                        not re.search('^https://www.unian.net/', news['url'])and \
                        not re.search('^https://meduza.io/', news['url']):
                    pack.append(f'Заголовок:\n\r {news["title"]}\n\r\n\rИнформация:\n\r {news["description"]}\n\r\n\rПодробнее:\n\r {news["url"]}')

    return pack
