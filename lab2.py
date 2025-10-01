from flask import Blueprint, url_for, request, redirect, abort, render_template
import datetime
lab2 = Blueprint('lab2', __name__)

@lab2.route("/lab2/a")
def a1():
    return 'без слеша'


@lab2.route("/lab2/a/")
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


@lab2.route("/lab2/flowers/<int:flower_id>")
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


@lab2.route("/lab2/add_flower/<name>")
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


@lab2.route("/lab2/add_flower/")
def none_flower():
    return render_template('none_flower.html')


@lab2.route('/lab2/spisok_flower/')
def all_flowers():
    return render_template('spisok_flower.html', flowers=flower_list)


@lab2.route("/lab2/clear_flower")
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


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html', phrase=phrase)


@lab2.route("/lab2/calc/<int:a>/<int:b>")
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


@lab2.route("/lab2/calc/")
def defcalc():
    return redirect('/lab2/calc/1/1')


@lab2.route("/lab2/calc/<int:a>")
def newcalc(a):
    return redirect(f'/lab2/calc/{a}/1')


@lab2.route('/lab2/books')
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


@lab2.route('/lab2/berry')
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


@lab2.route('/lab2/flowers_advanced/', methods=['GET', 'POST'])
def flowers_advanced():
   
    if request.method == 'POST':
        flower_name = request.form.get('flower_name')
        flower_price = request.form.get('flower_price')
        if flower_name and flower_price:
            flowers_with_prices.append({'name': flower_name, 'price': int(flower_price)})

    return render_template('flowers_advanced.html', flowers=flowers_with_prices)


@lab2.route('/lab2/add_flower_advanced/<name>/<int:price>')
def add_flower_advanced(name, price):

    flowers_with_prices.append({'name': name, 'price': price})
    return redirect('/lab2/flowers_advanced/')


@lab2.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    
    if flower_id >= len(flowers_with_prices):
        abort(404)
    flowers_with_prices.pop(flower_id)
    return redirect('/lab2/flowers_advanced/')


@lab2.route('/lab2/del_all_flowers')
def del_all_flowers():
    flowers_with_prices.clear()
    return redirect('/lab2/flowers_advanced/')