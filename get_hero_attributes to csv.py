import json
import csv

with open(r'C:\Users\91879\OneDrive\Desktop\Python\dota_heroes728.json', 'r') as file:
    data = json.load(file)

l = []
headers = [
        "Hero",
        "Strength",
        "Agility",
        "Intelligence",
		"Health_base",
        "Health_lvl1",
        "Health_lvl15",
        "Health_lvl25",
        "Health_lvl30",
        "Health regen_base",
        "Health regen_lvl1",
        "Health regen_lvl15",
        "Health regen_lvl25",
        "Health regen_lvl30",
        "Mana_base",
        "Mana_lvl1",
        "Mana_lvl15",
        "Mana_lvl25",
        "Mana_lvl30",
        "Mana regen_base",
        "Mana regen_lvl1",
        "Mana regen_lvl15",
        "Mana regen_lvl25",
        "Mana regen_lvl30",
        "Armor_base",
        "Armor_lvl1",
        "Armor_lvl15",
        "Armor_lvl25",
        "Armor_lvl30",
        "Att/sec_base",
        "Att/sec_lvl1",
        "Att/sec_lvl15",
        "Att/sec_lvl25",
        "Att/sec_lvl30",
        "Damage_base",
        "Damage_lvl1",
        "Damage_lvl15",
        "Damage_lvl25",
        "Damage_lvl30",
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

with open(r'C:\Users\91879\OneDrive\Desktop\Python\out.csv', 'w+', encoding='utf-8') as file:
    json_to_csv = csv.writer(file, delimiter=',', lineterminator='\n')
    json_to_csv.writerow(headers)

    for i in data:
        if i != 'Index':
            l.append(i)
            for _ in data[i]:
                if type(_) is list:
                    for k in _:
                        l.append(int(k) if type(k) is int else k.replace('â€’', '-').strip('á¹¢'))
                else:
                    l.append(int(_) if type(_) is int else _.replace('â€’', '-').strip('á¹¢'))
        json_to_csv.writerow(l)
        l.clear()