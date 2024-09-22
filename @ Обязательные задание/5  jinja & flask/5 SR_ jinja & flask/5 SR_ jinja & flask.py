from flask import Flask, render_template, g

app = Flask(__name__)

navMenu = [
            {'link':'/index/', 'name': 'Главная'},
            {'link':'/product1/', 'name': 'Горный'},
            {'link':'/product2/', 'name': 'Городской'},
            {'link':'/product3/', 'name': 'Детский'},
            {'link':'/product4/', 'name': 'Трековый'}
         ]

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', menu=navMenu)

@app.route('/product1/')
def product1():
    return render_template('product1.html', menu=navMenu)

@app.route('/product2/')
def product2():
    return render_template('product2.html', menu=navMenu)

@app.route('/product3/')
def product3():
    return render_template('product3.html', menu=navMenu)

@app.route('/product4/')
def product4():
    return render_template('product4.html', menu=navMenu)

if __name__ == '__main__':
    app.run()