from flask import Flask, url_for, request, redirect, abort, render_template, session
from flask_sqlalchemy import SQLAlchemy
from db import db
import datetime
import os
from os import path
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from rgz import rgz

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET-KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'alex_ryazantsev_orm'
    db_user = 'alex_ryazantsev_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = '5432'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'

else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "alex_ryazantsev_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(rgz)

@app.route("/index")
def index():
    css = url_for('static', filename='lab1/main.css')

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
    css = url_for('static', filename='lab1/main.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                    <div class='spisoklab'><a href="/lab1">Лабораторная работа №1</a></div>
                    <div class='spisoklab'><a href="/lab2">Лабораторная работа №2</a></div>
                    <div class='spisoklab'><a href="/lab3">Лабораторная работа №3</a></div>
                    <div class='spisoklab'><a href="/lab4">Лабораторная работа №4</a></div>
                    <div class='spisoklab'><a href="/lab5">Лабораторная работа №5</a></div>
                    <div class='spisoklab'><a href="/lab6">Лабораторная работа №6</a></div>
                    <div class='spisoklab'><a href="/lab7">Лабораторная работа №7</a></div>
                    <div class='spisoklab'><a href="/lab8">Лабораторная работа №8</a></div>
                    <div class='spisoklab'><a href="/rgz">Расчётно-графическое задание</a></div>
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