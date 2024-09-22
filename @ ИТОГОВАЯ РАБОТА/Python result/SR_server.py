from flask import Flask, render_template, g
import sqlite3 # делаем импорт sqlite3
import SR_Base

app = Flask(__name__)
# создаем обращение к базе данных (путь к базе данных) через словарик
app.config['DATABASE'] = 'static/db/houses.db'  
# секретный ключ доступа к БД нужно задать обязательно
app.secret_key= 'qwerty12345'

# функция - создаем подлючение
def connect_db():
    con=sqlite3.connect(app.config['DATABASE'])     # когда функция завершит работу все объекты будут удаляться
    # con.row_factory = sqlite3.Row
    return con

# функция - для логики, когда надо делать новое подключение, а когда подключение не требуется
def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

# декоратор для ситуации, когда пользователь отключается от сайта
@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

navMenu = [
            {'link':'/main/', 'name': 'Главная'},
            {'link':'/houses/', 'name': 'Дома'},            
            {'link':'/info/', 'name': 'Контакты'}
         ]

@app.route('/')
@app.route('/main/')
def main():   
    return render_template('main.html', menu=navMenu)

@app.route('/houses/')
def houses():
    baseObject = SR_Base.HouseDB(get_connect())
    houses = baseObject.getALLHouses()
    return render_template('houses.html', menu=navMenu, houses=houses)

@app.route('/info/')
def info():
    return render_template('info.html', menu=navMenu)

# обработчик адреса дома url
@app.route('/house/<int:id>')
def showHouse(id: int):    
    base = SR_Base.HouseDB(get_connect())
    res = base.getHouseFromId(id)
    if res:
        return render_template('concretHouse.html', house=res, menu=navMenu)
    else:
        return f'Дом потерян, всё сломалось'
        # можно также вернуть render_template шаблон страницы с ошибкой

if __name__ == '__main__':
    app.run()