from flask import Flask, url_for, request, redirect, abort, render_template
import datetime
app = Flask(__name__)

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
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1")
def lab1():
    css = url_for('static', filename='main.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>Лабораторная работа 1</title>
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
                    <h2>Список роутов:</h2>
                    <div class=spisoklab>
                        <ol class='text'>
                            <li><a href="/">Корень сайта</a><br>
                            <li><a href="/index">Главная страница</a><br>
                            <li><a href="/lab1/web">Веб-сервер</a><br>
                            <li><a href="/lab1/author">Автор</a><br>
                            <li><a href="/lab1/image">Изображение</a><br>
                            <li><a href="/lab1/counter">Счетчик</a><br>
                            <li><a href="/lab1/clearcounter">Сбор счетчика</a><br>
                            <li><a href="/lab1/info">Информация</a><br>
                            <li><a href="/lab1/created">Что-то создано</a><br>
                            <li><a href="/lab1/400">Код ответа 400</a><br>
                            <li><a href="/lab1/401">Код ответа 401</a><br>
                            <li><a href="/lab1/402">Код ответа 402</a><br>
                            <li><a href="/lab1/403">Код ответа 403</a><br>
                            <li><a href="/lab1/404">Код ответа 404</a><br>
                            <li><a href="/lab1/405">Код ответа 405</a><br>
                            <li><a href="/lab1/418">Код ответа 418</a><br>
                            <li><a href="/lab1/obrabot">Обработчик</a><br>
                        </ol>
                    </div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1/web")
def web():
    css = url_for('static', filename='lab1.css')

    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">Автор</a><br>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 200, { 
            'X-Server': 'sample', 
            'Content-Type': 'text/plain; charset=utf-8' 
        }

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
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <hr class='hr'>
                <p>Студент: ''' + name + '''</p>
                <hr class='hr'>
                <p>Группа: ''' + group + '''</p>
                <hr class='hr'>
                <p>Факультет: ''' + faculty + '''</p>
                <hr class='hr'>
                <a href="/lab1/web">web</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
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
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div class="block">
                    <h1>🌳Дуб🌳</h1>
                    <img src="''' + path + '''">
                </div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
            </body>
        </html>''', {
            "X-Server": "sample",
            "Content-Language": "en, ase, ru",
            "Web-Prog": "FBI-31",
            "Author": "Alexander Ryazantsev"
        }

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
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
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
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
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
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <hr class='hr'>
                <div class='clearcounter'>Обновите страницу чтобы сбросить счетчик<br>и вернитесь назад</div><br>
                <hr class='hr'>
                <div class='link'>
                    <a href="/lab1/counter">counter</a>
                </div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
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
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <h1>Создано успешно</h1>
                <div><i>что-то создано...</i></div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 201

@app.route("/lab1/400")
def code400():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>Код состояния ответа "HTTP 400 Bad Request" указывает, что сервер не смог понять запрос из-за недействительного синтаксиса. Клиент не должен повторять этот запрос без изменений.</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 400

@app.route("/lab1/401")
def code401():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>Код ответа на статус ошибки HTTP 401 Unauthorized клиента указывает, что запрос не был применён, поскольку ему не хватает действительных учётных данных для целевого ресурса.</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 401

@app.route("/lab1/402")
def code402():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>HTTP-ответ 402 Payment Required это нестандартная ошибка клиента, зарезервированная для использования в будущем. Иногда этот код означает, что запрос не может быть выполнен до тех пор, пока клиент не совершит оплату. Изначально создан для активации цифровых средств или (микро) платёжных систем и изображает, что запрошенный контент недоступен пока клиент не совершит оплату. Так или иначе, стандартизованного использования для кода нет, и он может использоваться разными элементами в разном контексте.</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 402

@app.route("/lab1/403")
def code403():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>Код ответа на статус ошибки "HTTP 403 Forbidden" указывает, что сервер понял запрос, но отказывается его авторизовать. Этот статус похож на 401, но в этом случае повторная аутентификация не будет иметь никакого значения. Доступ запрещён и привязан к логике приложения (например, у пользователя не хватает прав доступа к запрашиваемому ресурсу).</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 403

@app.route("/lab1/405")
def code405():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>Код состояния протокола HTTP 405 Method Not Allowed, указывает, что метод запроса известен серверу, но был отключён и не может быть использован. Два обязательных метода GET и HEAD никогда не должны быть отключены и не должны возвращать этот код ошибки. Сервер ОБЯЗАН сгенерировать поле заголовка Allow в ответе с кодом 405, которое содержит список текущих доступных методов ресурса.</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 405

@app.route("/lab1/418")
def code418():
    css = url_for('static', filename='lab1.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>HTTP код ошибки 418 I'm a teapot сообщает о том, что сервер не может приготовить кофе, потому что он чайник. Эта ошибка ссылается на Hyper Text Coffee Pot Control Protocol (гипертекстовый протокол кофейников) который был первоапрельской шуткой в 1998 году.</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>''', 418

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


@app.route("/lab1/obrabot")
def obrabot():
    css = url_for('static', filename='lab1.css')
    a = 100
    b = 0
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 1</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 1</header>
                <div>''' + str(a/b) + '''</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''

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

@app.route("/lab2/a")
def a1():
    return 'без слеша'

@app.route("/lab2/a/")
def a2():
    css = url_for('static', filename='main.css')
    return '''<!doctype html>
        <html> 
        <link rel="stylesheet" href="''' + css + '''">
           <body>
                <title>НГТУ, ФБ, Лабораторная работа 2</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 2</header>
                <div>со слешем</div>
                <a href="/" class="koren">🏠</a>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route("/lab2/flowers/<int:flower_id>")
def flowers(flower_id):
    css = url_for('static', filename='main.css')
    fav1 = url_for('static', filename='favicon1.png')
    fav = url_for('static', filename='favicon.png') 
    if flower_id >= len(flower_list):
        abort(404)
    else:    
        return '''<!doctype html>
            <html>
            <link rel="stylesheet" href="''' + css + '''">
            <link rel="icon" href="''' + fav + '''">
            <link rel="icon" href="''' + fav1 + '''">
            <body>
                <title>НГТУ, ФБ, Лабораторная работа 2</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 2</header>
                <div>цветок:''' + flower_list[flower_id] + '''</div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
                <a href='/lab2/spisok_flower'>spisok</a>
                <a href="/" class="koren">🏠</a>
            </body>
            </html>'''
    
@app.route("/lab2/add_flower/<name>")
def add_flower(name):
    css = url_for('static', filename='main.css')
    fav1 = url_for('static', filename='favicon1.png')
    fav = url_for('static', filename='favicon.png') 
    flower_list.append(name)
    return f'''<!doctype html>
        <html>
        <link rel="stylesheet" href="{css}">
        <link rel="icon" href="{fav}">
        <link rel="icon" href="{fav1}">
        <body>
                <title>НГТУ, ФБ, Лабораторная работа 2</title>
                <header>НГТУ, ФБ, WEB-программирование, Лабораторная 2</header>
                <h1>Добавлен новый цветок</h1>
                <div>Название нового цветка: {name}</div>
                <p>Всего цветов: {len(flower_list)}</p> 
                <p>Полный список: {flower_list}</p>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
        </body>
        </html>'''

@app.route("/lab2/add_flower/")
def none_flower():
    return render_template('none_flower.html')

@app.route('/lab2/spisok_flower/')
def all_flowers():
    return render_template('spisok_flower.html', flowers=flower_list)

@app.route("/lab2/clear_flower")
def clear_flower():
    css = url_for('static', filename='main.css') 
    fav1 = url_for('static', filename='favicon1.png')
    fav = url_for('static', filename='favicon.png')
    flower_list.clear()
    return f'''<!doctype html>
            <html>
            <link rel="stylesheet" href="{css}">
            <link rel="icon" href="{fav}">
            <link rel="icon" href="{fav1}">
            <body>
                    <title>НГТУ, ФБ, Лабораторная работа 2</title>
                    <header>НГТУ, ФБ, WEB-программирование, Лабораторная 2</header>
                    <div>Список очищен</div>
                    <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
                    <a href='/lab2/spisok_flower'>spisok</a>
                    <a href="/" class="koren">🏠</a>
            </body>
            </html>'''

@app.route('/lab2/example')
def example():
    name = 'Рязанцев Александр Алексеевич'
    number_lab = '2'
    group = 'ФБИ-31'
    course = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},    
        {'name': 'апельсины', 'price': 80},    
        {'name': 'мандарины', 'price': 95},    
        {'name': 'манго', 'price': 321}        
    ]
    return render_template('example.html', number_lab=number_lab, name=name, group=group, course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>отркытий</i> чудных...'
    return render_template('filter.html', phrase=phrase)

@app.route("/lab2/calc/<int:a>/<int:b>")
def calc(a, b):
    css = url_for('static', filename='main.css')
    fav1 = url_for('static', filename='favicon1.png')
    fav = url_for('static', filename='favicon.png')
    
    sum = a + b
    minus = a - b
    umn = a * b
    stepen = a ** b
    stepen_str = f"{a}<sup>{b}</sup> = {stepen}"
    
    if b != 0:
        delenie = a / b
        delenie_str = f"{a} / {b} = {delenie}"
    else:
        delenie_str = f"{a} / {b} = деление на 0 запрещено!"
    
    
    return f'''<!doctype html>
        <html>
        <link rel="stylesheet" href="{css}">
        <link rel="icon" href="{fav}">
        <link rel="icon" href="{fav1}">
        <body>
            <title>НГТУ, ФБ, Лабораторная работа 2</title>
            <header>НГТУ, ФБ, WEB-программирование, Лабораторная 2</header>
            <h2>Калькулятор</h2>
            <div>Число a: {a}</div>
            <div>Число b: {b}</div>
            <hr>
            <div>Сумма: {a} + {b} = {sum}</div>
            <div>Вычитание: {a} - {b} = {minus}</div>
            <div>Умножение: {a} * {b} = {umn}</div>
            <div>Деление: {delenie_str}</div>
            <div>Возведение в степень: {stepen_str}</div>
            <hr>
            <a href="/" class="koren">🏠</a>
            <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
        </body>
        </html>'''

@app.route("/lab2/calc/")
def defcalc():
    return redirect('/lab2/calc/1/1')

@app.route("/lab2/calc/<int:a>")
def newcalc(a):
    return redirect(f'/lab2/calc/{a}/1')

@app.route('/lab2/books')
def books():
    books = [
    {'author': 'Фёдор Достоевский', 'name': 'Преступление и наказание', 'genre': 'Роман', 'str': 671},
    {'author': 'Лев Толстой', 'name': 'Война и мир', 'genre': 'Эпопея', 'str': 1274},
    {'author': 'Михаил Булгаков', 'name': 'Мастер и Маргарита', 'genre': 'Роман', 'str': 384},
    {'author': 'Антон Чехов', 'name': 'Рассказы', 'genre': 'Рассказы', 'str': 256},
    {'author': 'Александр Пушкин', 'name': 'Евгений Онегин', 'genre': 'Роман в стихах', 'str': 224},
    {'author': 'Николай Гоголь', 'name': 'Мёртвые души', 'genre': 'Поэма', 'str': 352},
    {'author': 'Иван Тургенев', 'name': 'Отцы и дети', 'genre': 'Роман', 'str': 288},
    {'author': 'Александр Солженицын', 'name': 'Архипелаг ГУЛАГ', 'genre': 'Историческая проза', 'str': 1424},
    {'author': 'Владимир Набоков', 'name': 'Лолита', 'genre': 'Роман', 'str': 336},
    {'author': 'Михаил Шолохов', 'name': 'Тихий Дон', 'genre': 'Роман-эпопея', 'str': 1504},
    {'author': 'Джордж Оруэлл', 'name': '1984', 'genre': 'Антиутопия', 'str': 328},
    {'author': 'Рэй Брэдбери', 'name': '451° по Фаренгейту', 'genre': 'Научная фантастика', 'str': 256}
]
    return render_template('books.html', books=books)

@app.route('/lab2/berry')
def berry():
    berry = [
    {
        'name': 'Клубника',
        'image': 'klub.png',
        'description': 'Сладкая красная ягода, богатая витамином C и антиоксидантами.'
    },
    {
        'name': 'Малина',
        'image': 'malina.png',
        'description': 'Ароматная ягода с нежным вкусом, содержит эллаговую кислоту.'
    },
    {
        'name': 'Черника',
        'image': 'chernika.png',
        'description': 'Маленькая синяя ягода, улучшает зрение и память.'
    },
    {
        'name': 'Ежевика',
        'image': 'ezhevika.png',
        'description': 'Тёмная ягода с кисло-сладким вкусом, богата клетчаткой.'
    },
    {
        'name': 'Смородина чёрная',
        'image': 'chernsmor.png',
        'description': 'Ароматная ягода с высоким содержанием витамина C.'
    },
    {
        'name': 'Смородина красная',
        'image': 'krasncmor.png',
        'description': 'Кислая прозрачная ягода, отлично подходит для желе.'
    },
    {
        'name': 'Крыжовник',
        'image': 'krizh.png',
        'description': 'Зелёная или красная ягода с освежающим кисло-сладким вкусом.'
    },
    {
        'name': 'Голубика',
        'image': 'golubika.png',
        'description': 'Дикая родственница черники, растёт в хвойных лесах.'
    },
    {
        'name': 'Брусника',
        'image': 'brusnika.png',
        'description': 'Красная кислая ягода, часто используется в медицине.'
    },
    {
        'name': 'Клюква',
        'image': 'klukva.png',
        'description': 'Кислая красная ягода, растёт на болотах, полезна для почек.'
    },
    {
        'name': 'Облепиха',
        'image': 'oblepiha.png',
        'description': 'Оранжевая ягода с высоким содержанием витаминов A и E.'
    },
    {
        'name': 'Шиповник',
        'image': 'shipovnik.png',
        'description': 'Плод розы, рекордсмен по содержанию витамина C.'
    },
    {
        'name': 'Боярышник',
        'image': 'boyarishnik.png',
        'description': 'Красные ягоды, полезные для сердечно-сосудистой системы.'
    },
    {
        'name': 'Калина',
        'image': 'kalina.png',
        'description': 'Красные горьковатые ягоды, традиционное лекарственное растение.'
    },
    {
        'name': 'Рябина',
        'image': 'ryabina.png',
        'description': 'Оранжево-красные ягоды, становятся сладкими после заморозков.'
    },
    {
        'name': 'Черёмуха',
        'image': 'cheremuha.png',
        'description': 'Чёрные ароматные ягоды с вяжущим вкусом.'
    },
    {
        'name': 'Ирга',
        'image': 'irga.png',
        'description': 'Сладкие сине-чёрные ягоды, богатые антиоксидантами.'
    },
    {
        'name': 'Жимолость',
        'image': 'jimolost.png',
        'description': 'Синие продолговатые ягоды с уникальным вкусом.'
    },
    {
        'name': 'Бузина',
        'image': 'buzina.png',
        'description': 'Тёмно-фиолетовые ягоды, используются в народной медицине.'
    },
    {
        'name': 'Годжи',
        'image': 'godji.png',
        'description': 'Красные ягоды, известные как суперфуд с антиоксидантами.'
    },
    {
        'name': 'Морошка',
        'image': 'moroshka.png',
        'description': 'Желто-оранжевая ягода, растущая в северных регионах.'
    },
]
    return render_template('berry.html', berry=berry)

flowers_with_prices = [
    {'name': 'роза', 'price': 300},
    {'name': 'тюльпан', 'price': 310},
    {'name': 'незабудка', 'price': 320},
    {'name': 'ромашка', 'price': 330}
]

@app.route('/lab2/flowers_advanced/', methods=['GET', 'POST'])
def flowers_advanced():
   
    if request.method == 'POST':
        flower_name = request.form.get('flower_name')
        flower_price = request.form.get('flower_price')
        if flower_name and flower_price:
            flowers_with_prices.append({'name': flower_name, 'price': int(flower_price)})

    return render_template('flowers_advanced.html', flowers=flowers_with_prices)

@app.route('/lab2/add_flower_advanced/<name>/<int:price>')
def add_flower_advanced(name, price):

    flowers_with_prices.append({'name': name, 'price': price})
    return redirect('/lab2/flowers_advanced/')

@app.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    
    if flower_id >= len(flowers_with_prices):
        abort(404)
    flowers_with_prices.pop(flower_id)
    return redirect('/lab2/flowers_advanced/')

@app.route('/lab2/del_all_flowers')
def del_all_flowers():
    flowers_with_prices.clear()
    return redirect('/lab2/flowers_advanced/')