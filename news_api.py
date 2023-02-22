import requests
import json


def get_news():
    pack = list()

    response = requests.get('https://newsapi.org/v2/top-headlines?'
       'country=ru&'
       'apiKey=7248b8a39f3d471581e5397cfd3f3459')
    news = json.loads(response.text)
    for key, val in list(news.items()):
        if key == 'articles':
            lst = val

    cash = dict()

    for inform in lst:
        for key, val in list(inform.items()):
            if key == 'autor' or key == 'title' or key == 'description' or key == 'url':
                cash[key] = val
                pack.append(cash)
    return pack[0]