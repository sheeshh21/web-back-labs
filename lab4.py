from flask import Blueprint, url_for, request, redirect, abort, render_template, make_response, session
import datetime
lab4 = Blueprint('lab4', __name__)

@lab4.route("/lab4/")
def lab():
    return render_template('lab4/lab4.html')


@lab4.route("/lab4/div-form")
def divform():
    return render_template('lab4/div-form.html')


@lab4.route("/lab4/div", methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    if x2 == '0':
        return render_template('lab4/div.html', error2='На ноль делить нельзя!')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 / x2

    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route("/lab4/summ", methods = ['POST'])
def summ():
    x1 = request.form.get('x1') or '0'
    x2 = request.form.get('x2') or '0'

    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2

    return render_template('lab4/summ.html', x1=x1, x2=x2, result=result)


@lab4.route("/lab4/umn", methods = ['POST'])
def umn():
    x1 = request.form.get('x1') or '1'
    x2 = request.form.get('x2') or '1'

    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2

    return render_template('lab4/umn.html', x1=x1, x2=x2, result=result)


@lab4.route("/lab4/vichit", methods = ['POST'])
def vichit():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/vichit.html', error='Оба значения должны быть заполнены')


    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2

    return render_template('lab4/vichit.html', x1=x1, x2=x2, result=result)


@lab4.route("/lab4/stepen", methods = ['POST'])
def stepen():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/stepen.html', error='Оба значения должны быть заполнены')

    if x1 == '0' and x2 == '0':
        return render_template('lab4/stepen.html', error2='Оба поля не должны равняться 0')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 ** x2

    return render_template('lab4/stepen.html', x1=x1, x2=x2, result=result)

tree_count = 0
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    if request.method == 'POST':
        operation = request.form.get('operation')

    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    if tree_count <= -1:
        return render_template('lab4/tree.html', error='Нельзя срубить отрицательное количество деревьев!')
    
    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Алексеевич'},
    {'login': 'bob', 'password': '555', 'name': 'Боб Бобович'},
    {'login': 'artem', 'password': '456', 'name': 'Артем Артемович'},
    {'login': 'vlad', 'password': '789', 'name': 'Владислав Владиславович'},
    {'login': 'matvey', 'password': '000', 'name': 'Матвей Матвеевич'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = ''
            for user in users:
                if user['login'] == login:
                    name = user['name']
        else:
            authorized = False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if login == '':
        errorlog = 'Не введён логин!'
        return render_template('lab4/login.html', errorlog=errorlog, authorized=False)
    
    if password == '':
        errorpass = 'Не введён пароль!'
        return render_template('lab4/login.html', errorpass=errorpass, authorized=False)
    
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False)


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/xolodilnik', methods=['GET', 'POST'])
def xolodilnik():
    temp1 = request.form.get('temp')
    
    if temp1 is None or temp1 == '':
        error = 'Ошибка: не задана температура'
        return render_template('lab4/xolodilnik.html', error=error)
    
    temp = float(temp1)
    
    if temp < -12:
        error = 'Не удалось установить температуру — слишком низкое значение'
        return render_template('lab4/xolodilnik.html', error=error)
    elif temp > -1:
        error = 'Не удалось установить температуру — слишком высокое значение'
        return render_template('lab4/xolodilnik.html', error=error)
    elif -12 <= temp <= -9:
        snowflakes = 3
        return render_template('lab4/xolodilnik.html', temp=temp, snowflakes=snowflakes)
    elif -8 <= temp <= -5:
        snowflakes = 2
        return render_template('lab4/xolodilnik.html', temp=temp, snowflakes=snowflakes)
    elif -4 <= temp <= -1:
        snowflakes = 1
        return render_template('lab4/xolodilnik.html', temp=temp, snowflakes=snowflakes)
    else:
        return render_template('lab4/xolodilnik.html', temp=temp)