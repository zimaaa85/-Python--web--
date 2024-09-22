# Registered email address: 165129@mail.ru
# Access token: fAbKA_03gpLTb88YxOac (Include this in your API calls!)
# Not sure how to do this? Please refer to the documentation's auth part!

# /character - персонаж
# List of characters including metadata like name, gender, realm, race and more
# Список персонажей, включающий метаданные, такие как имя, пол, царство, раса и многое другое

# /character/{id}
# Request one specific character - Запросить одного конкретного персонажа

# /character/{id}/quote
# Request all movie quotes of one specific character - 
# Запрашивать все цитаты из фильмов об одном конкретном персонаже

# /quote - цитата, Список всех цитат из фильмов
# List of all movie quotes - Запросить цитату из одного конкретного фильма

# /quote/{id} Request one specific movie quote - Запросить цитату из одного конкретного фильма

# /chapter - глава, List of all book chapters - Список всех глав книги

# /chapter/{id} Request one specific book chapter
# Запросите одну конкретную главу книги

from requests import *
import random

key='Bearer fAbKA_03gpLTb88YxOac'

headers = {'Accept': 'application/json', 'Authorization': key}

# resp= get(url='https://the-one-api.dev/v2/book', headers=headers ) # запрос по книгам
# dict_keys(['docs', 'total', 'limit', 'offset', 'page', 'pages'])
# все ключи docs:
# [{'_id': '5cf5805fb53e011a64671582', 'name': 'The Fellowship Of The Ring'}, 
#  {'_id': '5cf58077b53e011a64671583', 'name': 'The Two Towers'}, 
#  {'_id': '5cf58080b53e011a64671584', 'name': 'The Return Of The King'}]

# resp= get(url='https://the-one-api.dev/v2/movie', headers=headers ) # запрос по фильмам
# dict_keys(['docs', 'total', 'limit', 'offset', 'page', 'pages'])
# все ключи docs:
# dict_keys(['_id', 'name', 'runtimeInMinutes', 'budgetInMillions', 'boxOfficeRevenueInMillions', 'academyAwardNominations', 'academyAwardWins', 'rottenTomatoesScore'])
# [{'_id': '5cd95395de30eff6ebccde56', 'name': 'The Lord of the Rings Series', 'runtimeInMinutes': 558, 'budgetInMillions': 281, 'boxOfficeRevenueInMillions': 2917, 'academyAwardNominations': 30, 'academyAwardWins': 17, 'rottenTomatoesScore': 94}, 
#  {'_id': '5cd95395de30eff6ebccde57', 'name': 'The Hobbit Series', 'runtimeInMinutes': 462, 'budgetInMillions': 675, 'boxOfficeRevenueInMillions': 2932, 'academyAwardNominations': 7, 'academyAwardWins': 1, 'rottenTomatoesScore': 66.33333333}, 
#  {'_id': '5cd95395de30eff6ebccde58', 'name': 'The Unexpected Journey', 'runtimeInMinutes': 169, 'budgetInMillions': 200, 'boxOfficeRevenueInMillions': 1021, 'academyAwardNominations': 3, 'academyAwardWins': 1, 'rottenTomatoesScore': 64}, 
#  {'_id': '5cd95395de30eff6ebccde59', 'name': 'The Desolation of Smaug', 'runtimeInMinutes': 161, 'budgetInMillions': 217, 'boxOfficeRevenueInMillions': 958.4, 'academyAwardNominations': 3, 'academyAwardWins': 0, 'rottenTomatoesScore': 75}, 
#  {'_id': '5cd95395de30eff6ebccde5a', 'name': 'The Battle of the Five Armies', 'runtimeInMinutes': 144, 'budgetInMillions': 250, 'boxOfficeRevenueInMillions': 956, 'academyAwardNominations': 1, 'academyAwardWins': 0, 'rottenTomatoesScore': 60}, 
#  {'_id': '5cd95395de30eff6ebccde5b', 'name': 'The Two Towers', 'runtimeInMinutes': 179, 'budgetInMillions': 94, 'boxOfficeRevenueInMillions': 926, 'academyAwardNominations': 6, 'academyAwardWins': 2, 'rottenTomatoesScore': 96}, 
#  {'_id': '5cd95395de30eff6ebccde5c', 'name': 'The Fellowship of the Ring', 'runtimeInMinutes': 178, 'budgetInMillions': 93, 'boxOfficeRevenueInMillions': 871.5, 'academyAwardNominations': 13, 'academyAwardWins': 4, 'rottenTomatoesScore': 91}, 
#  {'_id': '5cd95395de30eff6ebccde5d', 'name': 'The Return of the King', 'runtimeInMinutes': 201, 'budgetInMillions': 94, 'boxOfficeRevenueInMillions': 1120, 'academyAwardNominations': 11, 'academyAwardWins': 11, 'rottenTomatoesScore': 95}]



# resp= get(url='https://the-one-api.dev/v2/quote', headers=headers ) # запрос по цитатам
# dict_keys(['docs', 'total', 'limit', 'offset', 'page', 'pages'])
# всего 2384 цитаты 'total'
# print(resp.json()['docs'][0].keys()) # для получения ключей в docs для цитат
# dict_keys(['_id', 'dialog', 'movie', 'character', 'id'])

# resp= get(url='https://the-one-api.dev/v2/character', headers=headers ) # запрос по персонажам
# dict_keys(['docs', 'total', 'limit', 'offset', 'page', 'pages'])
# всего 933 персонажей'total'
# пример данных по одному из персонажей {'_id': '5cdbe73516d496d2c2940848', 'name': 'Éothain', 'wikiUrl': 'http://lotr.wikia.com//wiki/Éothain_(film_character)t', 'race': 'Human', 'birth': None, 'gender': 'Male', 'death': None, 'hair': None, 'height': None, 'realm': 'Rohan', 'spouse': None}]
# print(resp.json()['docs'][0].keys()) # для получения ключей в docs для персонажей
# dict_keys(['_id', 'name', 'wikiUrl', 'race', 'birth', 'gender', 'death', 'hair', 'height', 'realm', 'spouse'])   


# print(resp.url)
# print(resp.status_code)
# print(len(resp.json())) # получаем количество элементов json
# print(resp.json().keys())  # получаем ключи словаря json:

# print(resp.json()['docs']) # для получения списков docs
# print(resp.json()['docs'][0].keys()) # для получения ключей в docs на примере 1 словаря
# print(resp.json()['docs']['dialog'])

# response = resp.json()  # получаем текстов всех цитат 
# for doc in response['docs']:
#     print(doc['dialog'])

# response = resp.json()  # получаем все имена персонажей
# for doc in response['docs']:
#     print(doc['name'])
    # выписал часть имен персонажей:
        # для этой части персонажей НЕТ цитат:
# Adanel
# Aegnor
# Aerin
# Farin
# Fingon
# Finrod
# Horn
# Hundad
# Hundar
        # для этой части персонажей ЕСТЬ цитат:
# Denethor II
# Aragorn II Elessar
# Théoden
# Treebeard
# Samwise Gamgee
# Faramir
# Elrond

# функция - по имя персонажа выдает тексты его цитат
def quoteMovieCharacter():
    character_name = input("Введите имя персонажа: ").strip()

    characters_resp = get('https://the-one-api.dev/v2/character/' , headers=headers, params={'name': character_name})
    characters = characters_resp.json()

    if 'docs' in characters and len(characters['docs']) > 0:
        character_id = characters['docs'][0]['_id']
       
        quotes_resp = get('https://the-one-api.dev/v2/quote/', headers=headers, params={'character': character_id})
        quotes = quotes_resp.json()

        if 'docs' in quotes and len(quotes['docs']) > 0:
            print(f"Все найденные цитаты для персонажа '{character_name}':")
            for quote_data in quotes['docs']:
                print("Цитата:", quote_data['dialog'])
           
        else:
            print("Цитаты для данного персонажа не найдены.")
    else:
        print("Персонаж не найден.")

quoteMovieCharacter()


# функция - по произвольной цитате определяет имя персонажа
# def fetchData():
    
#     quotes_resp= get(url='https://the-one-api.dev/v2/quote', headers=headers )
#     quotes = quotes_resp.json()
#     random_index = random.randint(0, len(quotes['docs']) - 1)
#     quote = quotes['docs'][random_index]['dialog']
    
#     character_id = quotes['docs'][random_index]['character']
#     characters_resp = get('https://the-one-api.dev/v2/character/' + character_id, headers=headers)
#     characters = characters_resp.json()
#     character_name = characters['docs'][0]['name']

#     print(quotes_resp.status_code)
#     print(characters_resp.status_code)

#     return quote, character_name
   
# quote, character_name = fetchData()
# print("Цитата:", quote)
# print("Персонаж:", character_name)
