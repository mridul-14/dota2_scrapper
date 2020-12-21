import requests
from bs4 import BeautifulSoup
import json

urls = ['https://dota2.gamepedia.com/Category:Strength_heroes', 'https://dota2.gamepedia.com/Category:Intelligence_heroes', 'https://dota2.gamepedia.com/Category:Agility_heroes']
roles = {}
heroes = []

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    for i in soup.find_all('div', class_='mw-category-group'):
        for _ in i.find_all('li'):
            if _.text != 'User:Kroocsiogsi/Hero role matrix':
                heroes.append(_.text)
    category = url.split(':')[2]
    roles.update({category: heroes.copy()})
    heroes.clear()

with open(r'hero_category.json', 'w+') as file:
    json.dump(roles, file)
