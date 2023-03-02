import json
import re
import requests


def get_news():
    pack = list()

    lst = list()
    with open('black_list.txt') as file:
        for line in file:
            lst.append(line[0:-1])
    res = requests.get("https://newsapi.org/v2/top-headlines?",
                       params={'language': 'ru', 'country': 'ru', 'apiKey': 'YOU APIKEY'}).text

    switch = list()
    info = json.loads(res)
    for key, val in list(info.items()):
        if key == 'articles':
            for news in val:
                for black in lst:
                    if not re.search(f'^{black}', news['url']):
                        switch.append('ok')
                    else:
                        switch.append('no')
                if 'no' not in switch:
                    pack.append(f'Заголовок:\n\r {news["title"]}\n\r\n\r'
                                f'Информация:\n\r {news["description"]}\n\r\n\r'
                                f'Подробнее:\n\r {news["url"]}')

    return pack
