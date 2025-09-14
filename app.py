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
                    <div class='spisoklab'><a href="/lab1">Лабораторная работа №1</a></div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
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
                    <div class='spisoklab'><a href="/lab1">Лабораторная работа №1</a></div>
                <footer>Рязанцев Александр Алексеевич, ФБИ-31, 3 курс, 2025</footer>
          </body>
        </html>'''

@app.route("/lab1")
def lab1():
    css = url_for('static', filename='lab1.css')

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
        </html>''', 201, {
            "X-Server": "sample",
            "Content-Type": "text/plain; charset=utf-8"
        }

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
    css = url_for('static', filename='lab1.css')
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



