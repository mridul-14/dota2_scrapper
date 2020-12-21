import requests
from bs4 import BeautifulSoup
import json

l, temp, hero_data = [], [], {
	"Index": [
        "Strength",
        "Agility",
        "Intelligence",
		"Health",
		"Health regen",
		"Mana",
		"Mana regen",
		"Armor",
		"Att/sec",
		"Damage",
        "Magic resistance",
		"Movement speed",
		"Attack speed",
		"Turn rate",
		"Vision range",
		"Attack range",
		"Projectile speed",
		"Attack animation",
		"Base attack time",
		"Damage block",
		"Collision size",
		"Legs",
		"Gib type"
	]
}

url = 'https://dota2.gamepedia.com/Heroes'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

for index, _ in enumerate(soup.find_all('a')):
    if index in (53, 54, 93, 94):
        continue
    if index >= 14 and index <= 137:
        hero = _.attrs.get('href')[1:].replace('%27', "'")

        url = 'https://dota2.gamepedia.com'+_.attrs.get('href')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        
        tag = soup.find('div', style='width: 100%; padding: 4px 0; display: grid; grid-template-columns: auto auto auto; color: white; text-align: center;')
        for index, _ in enumerate(tag.find_all('b')):
            l.append(_.parent.text)

        tag = soup.find('table', class_='evenrowsgray')
        for _ in tag.tbody.find_all('tr')[1:]:
            for i in _.text.split('\n'):
                if(isinstance(i, str) and len(i)):
                    temp.append(i)
            l.append(temp.copy()[1:])
            temp.clear()

        tag = soup.find('table', class_='oddrowsgray')
        for _ in tag.tbody.find_all('tr'):
            for i in _.text.split('\n'):
                if(len(i)):
                    temp.append(i.replace('Link▶️ ', '').strip('\xa0'))
            l.append(temp.copy()[1])
            temp.clear()
        hero_data.update({hero: l.copy()})
        l.clear()

with open(r'dota_heroes.json', 'w+') as file:
    json.dump(hero_data, file)
