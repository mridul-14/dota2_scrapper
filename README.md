# dota2_scrapper

Here I've written a scrapper using bs4 & requests in Python.
The goal is to create a dataset on Kaggle available @ https://www.kaggle.com/prokid1911/dota-2-all-hero-data-727d
There are 4 file in the repo:
1. hero_category.py - This script is used to get the data about which category the hero belongs to (Strength, Agility, Intelligence)
2. hero_roles.py - This creates a file having details about hero roles (Carry, Support, Nuker, etc)
3. get_hero_attributes.py - This one is the main file, it captures details such as hp, mana regen, attack speed, move speed, collision size and other such details.
4. get_hero_attributes to csv.py - This was created to convert the JSON created by "get_hero_attributes.py" into csv.

The data is scraped from https://dota2.gamepedia.com/.
You can use these scripts however you like. Just remember to not bombard their website with too many requests.

I usually don't use comments in my code, so yeah. It might be hard to read the code.
I also haven't written a code that is heavily optimized or something like that, but it does the job in no time (simple scrapper!).
