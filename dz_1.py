import requests

def get_superheroes_data():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка")
        return None


def find_smartest_hero(superheroes_data, hero_names):
    smartest_hero = None
    max_intelligence = -1
    
    for hero in superheroes_data:
        name = hero['name']
        intelligence = int(hero['powerstats']['intelligence'])
        
        if name in hero_names and intelligence > max_intelligence:
            max_intelligence = intelligence
            smartest_hero = name
    
    return smartest_hero, max_intelligence


hero_names = ["Hulk", "Captain America", "Thanos"]

superheroes_data = get_superheroes_data()

if superheroes_data:
    smartest_hero, intelligence = find_smartest_hero(superheroes_data, hero_names)
    
    if smartest_hero:
        print(f"Самый умный супергерой: {smartest_hero}, уровень интеллекта: {intelligence}")
    else:
        print("Не удалось найти самого умного супергероя")







