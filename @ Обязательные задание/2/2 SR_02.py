# 1 задача (сделал 3и реализации)
# Пользователь - словарь : Дата рождения, имена
# Функция принимает список пользователей - возвращает количество пользователей по возрасту
# сортировка возраста до 10 лет, от 10-20 лет, от 20-30 лет, 30-40, 40-50

import datetime
from datetime import date

# Получаем объект класса date, представляющий текущую дату
today = date.today()
# Выводим текущую дату в формате "YYYY, MM, DD"
print('Текущая дата:', today.strftime("%Y, %m, %d"))

users = [
            {'Имя':'Вася', 'Дата рождения':datetime.date(2015, 5, 6)},
            {'Имя':'Вася', 'Дата рождения':datetime.date(2015, 5, 6)},
            {'Имя':'Вася', 'Дата рождения':datetime.date(2015, 5, 6)},
            {'Имя':'Иван', 'Дата рождения':datetime.date(1991, 6, 7)},
            {'Имя':'Влад', 'Дата рождения':datetime.date(1976, 8, 7)},
            {'Имя':'Витя', 'Дата рождения':datetime.date(1981, 5, 6)},
            {'Имя':'Петя', 'Дата рождения':datetime.date(1981, 5, 16)},
            {'Имя':'Коля', 'Дата рождения':datetime.date(1945, 3, 2)},
            {'Имя':'Дима', 'Дата рождения':datetime.date(1995, 2, 26)}
       ]
all={'Имя':'Вася', 'Дата рождения':datetime.date(2015, 5, 6)}
print(all.items())

def userDataToConsole(user: dict):
    
# Реализация 1 варианта - вывод на консоль без словарей    
    countAge0=0
    countAge1=0
    countAge2=0
    countAge3=0
    countAge4=0
    countAge5=0    
    newList={}

    for user in users:
        birth_date = user['Дата рождения']
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        # для проверки возраста вывожу на консоль возраст каждого user/словаря моего списка
        print(f"{user['Имя']} is {age} years old")  
        
        if age >= 0 and age <= 10:
            countAge0 +=1
        elif age >= 11 and age <= 20:
            countAge1 +=1
        elif age >= 21 and age <= 30:
            countAge2 +=1
        elif age >= 31 and age <= 40:
            countAge3 +=1
        elif age >= 41 and age <= 50:
            countAge4 +=1
        elif age > 50:
            countAge5 +=1 
           
    print(countAge0, ' возраст до 10 лет')
    print(countAge1, ' возраст от 11 до 20 лет')
    print(countAge2, ' возраст от 21 до 30 лет')
    print(countAge3, ' возраст от 31 до 40 лет')
    print(countAge4, ' возраст от 41 до 50 лет')
    print(countAge5, ' возраст за пределами диапазонов')

userDataToConsole(users)

#  # Реализация 2 варианта - вывод в словарь     
#     newList = {
#                 'возраст до 10 лет': 0,  
#                 'возраст от 11 до 20 лет': 0, 
#                 'возраст от 21 до 30 лет': 0, 
#                 'возраст от 31 до 40 лет': 0, 
#                 'возраст от 41 до 50 лет': 0, 
#                 'возраст за пределами диапазонов': 0  
#             }

#     for user in users:
#         birth_date = user['Дата рождения']
#         age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#         # для проверки возраста вывожу на консоль возраст каждого user/словаря моего списка
#         print(f"{user['Имя']} is {age} years old")  
        
#         if age >= 0 and age <= 10:
#                 newList['возраст до 10 лет'] += 1
#         elif age >= 11 and age <= 20:
#             newList['возраст от 11 до 20 лет'] += 1
#         elif age >= 21 and age <= 30:
#             newList['возраст от 21 до 30 лет'] += 1
#         elif age >= 31 and age <= 40:
#             newList['возраст от 31 до 40 лет'] += 1
#         elif age >= 41 and age <= 50:
#             newList['возраст от 41 до 50 лет'] += 1
#         elif age > 50:
#             newList['возраст за пределами диапазонов'] += 1

#     return newList

# print(userDataToConsole(users))


# # Реализация 3 варианта - вывод результата из словаря, используя цикл для печати: ключ-значение    
#     age_counts = {}  #пустой словарь для подсчета количества пользователей каждого возраста
 
#     for user in users:
#         birth_date = user['Дата рождения']
#         age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#         if age in age_counts:
#             age_counts[age] += 1  # Увеличиваем счетчик, если возраст уже есть в словаре
#         else:
#             age_counts[age] = 1  # Инициализируем счетчик, если возраст встречается впервые
#     return age_counts  # Возвращаем словарь с количеством пользователей каждого возраста

# result = userDataToConsole(users)
# for age, count in result.items():
#     print(f"{age} лет: {count}")





# 2 задача
# Список из трех словарей
# Словарь - координаты вершин (точки) треугольника, ключи: х, у
# Функция принимает список из 3х словарей - возвращает площадь треугольника построенного через вершины (точки)

koordinats = [
                {'x' : -2, 'y' : 10},
                {'x' : 10, 'y' : -5},
                {'x' : 5, 'y' : -10}
            ]

def triangleArea(koordinats: dict):
    #вытаскиваю из словарей координаты вершин в переменные
    x1=koordinats[0]['x']
    y1=koordinats[0]['y']

    x2=koordinats[1]['x']
    y2=koordinats[1]['y']

    x3=koordinats[2]['x']
    y3=koordinats[2]['y']

    #высчитываю площадь треугольника по трем координатам вершин
    area=abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
    return area   

print(triangleArea(koordinats))




# 3 задача
# Список с назнанием книг (словари)
# Функция принимает список с названием книг - возвращает список словарей.
# Каждый словарь - содержит 2а ключа: буква алфавита, количество книг на эту букву, делает подсчет без учета регистра
# (а и А в качестве первой буквы должны расцениваться как одна и та же буква)

books = [
            {'Название книги':'Азбука'},
            {'Название книги':'Алфавит'},
            {'Название книги':'автобус'},
            {'Название книги':'Кино'},
            {'Название книги':'киотеатр'},
            {'Название книги':'Фото'},
            {'Название книги':'зоопарк Казань'},
            {'Название книги':'Село зеленое'}
        ]

def booksSortCount(book:dict):
    sortCount={}
    for book in books:
        title = book['Название книги']
        letter = (title[0]).lower()  #первую букву привели к нижнему регистру
        if letter in sortCount:
            sortCount[letter]  += 1  #увеличиваем счетчик, если буква уже есть в словаре
        else:
            sortCount[letter]  = 1  #инициализируем счетчик, если буква встречается впервые
    
    return sortCount

# print(booksSortCount(books))
result = (booksSortCount(books))
for буква, count in result.items():
    print(f"буква '{буква}' : {count} шт.")