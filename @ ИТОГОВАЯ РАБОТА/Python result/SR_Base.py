from sqlite3 import connect, Connection, Cursor, Row

con =connect('static/db/houses.db')
cursor=Cursor(con)

# создаем запрос на создание базы данных
# sql= '''Create Table houses
#         (
#             id Integer Primary Key AUTOINCREMENT, 
#             name Text NOT NULL, 
#             floors Text NOT NULL,
#             square INTEGER NOT NULL, 
#             img TEXT NOT NULL,
#             img_plans TEXT NOT NULL,
#             img_facades TEXT NOT NULL,
#             price TEXT NOT NULL,
#             description TEXT NOT NULL     
#         )'''

#  создаем запись БД в проект
# cursor.execute(sql)

# записываем данные в БД
# sql = '''Insert into houses (name, floors, square, img, img_plans, img_facades, price, description) Values (?,?,?,?,?,?,?,?)'''
# cursor.executemany(sql,
#                     [('Дом 1', '1 этаж', 68, '1.jpg', '/1/план_1.jpg', '/1/1.jpg', '3 880 000 руб', '''Площадь застройки = 72 м2, Площадь дома = 68 м2, 
#                         Количество надземных этажей = 1, Высота дома = 5 м, Высота потолков = 2.7 м, Круглогодичное проживание = Да,
#                         Архитектурный стиль = Европейский''' ),
                     
#                     ('Дом 2', '2а этажа', 163, '2.jpg', '/2/план_2.png', '/2/1.jpg', '10 318 000 руб', '''Площадь застройки = 125 м2, 
#                         Площадь дома = 163 м2, Количество надземных этажей = 2, Высота дома = 9.55 м, Высота потолков = 3 м, Круглогодичное проживание = Да,
#                         Архитектурный стиль = Классический''' ),


#                     ('Дом 3', '2а этажа', 163, '3.jpg', '/3/план_3.jpg', '/3/1.jpg', '10 109 549 руб', '''Площадь застройки = 162 м2, 
#                         Площадь дома = 196 м2, Количество надземных этажей = 2, Высота дома = 8.13 м, Высота потолков = 3 м, Круглогодичное проживание = Да,
#                         Архитектурный стиль = Классический''' ),
                    
#                     ('Дом 4', '1 этаж', 165, '4.png', '/4/план_4.jpg', '/4/1.png', '9 842 500 руб', '''Площадь застройки = 215 м2, Площадь дома = 165 м2, 
#                         Количество надземных этажей = 1, Высота дома = 6.7 м, Высота потолков = 3 м, Круглогодичное проживание = Да,
#                         Архитектурный стиль = Классический''' ),

#                     ('Дом 5', '2а этажа', 155, '5.jpg', '/5/план_5.jpg', '/5/1.jpg', '15 438 047 руб', '''Площадь застройки = 97 м2, 
#                         Площадь дома = 155 м2, Количество надземных этажей = 2, Высота дома = 7.2 м, Высота потолков = 2.6 м, Круглогодичное проживание = Да,
#                         Архитектурный стиль = Европейский''' ),

#                     ('Дом 6', '1 этаж', 200, '6.jpg', '/6/план_6.jpg', '/6/1.jpg', '15 407 663 руб', '''Площадь застройки = 246 м2, Площадь дома = 200 м2, 
#                         Количество надземных этажей = 1, Высота дома = 5.47 м, Высота потолков = 3.2 м, Круглогодичное проживание = Да,
#                         Архитектурный стиль = Классический''' ),
#                         ])
# con.commit()

# sql = "Select * From houses"
# cursor.execute(sql)
# print(cursor.fetchall())

class HouseDB:
    def __init__(self, connection: Connection) -> None:
        self.__connect = connection
        self.__cursor = Cursor(connection)
        self.__cursor.row_factory = Row # возвращаем словари
    def getALLHouses(self):
        sql= 'Select id, name, floors, square, price, img FROM houses' #добавили еще id, чтобы потом сделать ссылку на страницу по id
        try:    # это исключения для поиска ошибок, не приводит к остановке программы
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except: # если ошибка произвошла то выйдет сообщение и пустой список
            print('Ошибка чтения из БД')
            return []
    
    # функция возвращает дом по id
    def getHouseFromId(self, id: int) -> dict | None:
        sql = "Select name, floors, square, img_plans, img_facades, price, description From houses Where id=?"
        try:   # это исключения для поиска ошибок, не приводит к остановке программы
            self.__cursor.execute(sql, (id,))
            return self.__cursor.fetchone() 
        except: # если ошибка произвошла то выйдет сообщение 
            print('Такой дом не существует')
            return None