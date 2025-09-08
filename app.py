from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/index")
def index():
    css = url_for('static', filename='lab1.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                    <a href="/lab1/web">Лабораторная работа №1</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/")
def a():
    css = url_for('static', filename='lab1.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                    <a href="/lab1/web">Лабораторная работа №1</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1")
def lab1():
    css = url_for('static', filename='lab1.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>Лабораторная 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                    <div>
                        Flask — фреймворк для создания веб-приложений на языке
                        программирования Python, использующий набор инструментов
                        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                        называемых микрофреймворков — минималистичных каркасов
                        веб-приложений, сознательно предоставляющих лишь самые ба
                        зовые возможности.
                    </div>
                    <a href="/">Вернуться в начало</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1/web")
def web():
    css = url_for('static', filename='lab1.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">Автор</a><br>
                <a href="/lab1/image">Изображение</a><br>
                <a href="/lab1/counter">Счетчик</a><br>
                <a href="/lab1/info">Информация</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1/author")
def author():
    css = url_for('static', filename='lab1.css')
    name = 'Рязанцев Александр Алексеевич'
    group = 'ФБИ-31'
    faculty = 'ФБ'
    

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                <hr class='hr'>
                <p>Студент: ''' + name + '''</p>
                <hr class='hr'>
                <p>Группа: ''' + group + '''</p>
                <hr class='hr'>
                <p>Факультет: ''' + faculty + '''</p>
                <hr class='hr'>
                <a href="/lab1/web">web</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1/image")
def image():
    path = url_for('static', filename='oak.jpg')
    css = url_for('static', filename='lab1.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
            <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                <div class="block">
                    <h1>🌳Дуб🌳</h1>
                    <img src="''' + path + '''">
                </div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
            </body>
        </html>'''

count = 0
@app.route("/lab1/counter")
def counter():
    global count
    global time
    global url
    global client_ip
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                <hr class='hr'>
                <div class='clearcounter'>Сколько раз вы сюда заходили:</div> ''' + str(count) + '''
                <hr class='hr'>
                <div class='clearcounter'>Дата и время:</div> ''' + str(time) + '''<br>
                <hr class='hr'>
                <div class='clearcounter'>Запрошенный адрес:</div> ''' + url + '''<br>
                <hr class='hr'>
                <div class='clearcounter'>Ваш IP адрес:</div> ''' + client_ip + '''<br>
                <hr class='hr'>
                <a href="/lab1/clearcounter">clearcounter</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1/clearcounter")
def clearcounter():
    global count
    count = 0
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                <hr class='hr'>
                <div class='clearcounter'>Обновите страницу чтобы сбросить счетчик<br>и вернитесь назад</div><br>
                <hr class='hr'>
                <div class='link'>
                    <a href="/lab1/counter">counter</a>
                </div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")    

@app.route("/lab1/created")
def created():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                <h1>Создано успешно</h1>
                <div><i>что-то создано...</i></div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 2 курс, 2025</footer>
          </body>
        </html>''', 201, {
            "X-Server": "sample",
            "Content-Type": "text/plain; charset=utf-8"
        }

@app.errorhandler(404)
def not_found(err):
    return "нет такой станицы", 404
