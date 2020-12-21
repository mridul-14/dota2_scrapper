import requests
from bs4 import BeautifulSoup
import json

urls = ['https://dota2.gamepedia.com/Category:Carries', 'https://dota2.gamepedia.com/Category:Supports', 'https://dota2.gamepedia.com/Category:Nukers', 'https://dota2.gamepedia.com/Category:Disablers', 'https://dota2.gamepedia.com/Category:Junglers', 'https://dota2.gamepedia.com/Category:Durable', 'https://dota2.gamepedia.com/Category:Escape', 'https://dota2.gamepedia.com/Category:Pushers', 'https://dota2.gamepedia.com/Category:Initiators']
roles = {}
heroes = []

for index, url in enumerate(urls):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    tag = soup.find('div', class_='mw-content-ltr', lang='en')
    for i in tag.find_all('div', class_='mw-category-group'):
        for _ in i.find_all('li'):
            if _.text != 'User:Kroocsiogsi/Hero role matrix':
                heroes.append(_.text)
    category = url.split(':')[2]
    roles.update({category: heroes.copy()})
    heroes.clear()

with open(r'hero_roles.json', 'w+') as file:
    json.dump(roles, file)
