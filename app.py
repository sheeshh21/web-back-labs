from flask import Flask, url_for, request, redirect, abort, render_template
import datetime
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)

@app.route("/index")
def index():
    css = url_for('static', filename='main.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                    <div class='spisoklab'><a href="/lab1">Лабораторная работа №1</a></div>
                    <div class='spisoklab'><a href="/lab1">Лабораторная работа №1</a></div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''


@app.route("/")
def a():
    css = url_for('static', filename='main.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                    <div class='spisoklab'><a href="/lab1">Лабораторная работа №1</a></div>
                    <div class='spisoklab'><a href="/lab2">Лабораторная работа №2</a></div>
                    <div class='spisoklab'><a href="/lab3">Лабораторная работа №3</a></div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''


logs = ""
@app.errorhandler(404)
def not_found1(err):
    css = url_for('static', filename='main.css')
    error = url_for('static', filename='error.png')
    global client_ip
    global time
    global url
    global logs
    client_ip = request.remote_addr
    time = datetime.datetime.today()
    url = request.url
    logs += '''<div class='logs'><ul><li>[<i>''' + str(time) + '''</i>, пользователь <i>''' + client_ip + '''</i>] зашел на адрес: <i>''' + url + '''</i></li></ul></div>'''
    

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body class='bodyerror'>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <div class='error'>Упс, походу это ошибка 404...</div>
                <img class='imgerror' src=''' + error + '''>
                <hr class='hr1'>
                <div>Ваш IP адрес:</div> ''' + client_ip + '''<br>
                <hr class='hr1'>
                <div>Дата и время:</div> ''' + str(time) + '''<br>
                <hr class='hr1'>
                <a href="/">Корень сайта</a><br>
                <hr class='hr1'>
                <div class='hlogs'>Журнал посещений:''' + logs + '''</div>
          </body>
        </html>''', 404


@app.errorhandler(500)
def not_found2(err):
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body class='bodyerror'>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <div class='error1'>Внутренняя ошибка сервера!<br>Сервер столкнулся с внутренней ошибкой и не смог выполнить ваш запрос. Сервер перегружен, либо в приложении произошла ошибка.</div>
          </body>
        </html>''', 500