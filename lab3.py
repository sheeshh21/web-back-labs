from flask import Blueprint, url_for, request, redirect, abort, render_template, make_response
import datetime
lab3 = Blueprint('lab3', __name__)

@lab3.route("/lab3/")
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)


@lab3.route("/lab3/cookie")
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'red')
    return resp

@lab3.route("/lab3/del_cookie")
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name')
    resp.set_cookie('age')
    resp.set_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    errors1 = {}
    age = request.args.get('age')
    if age == '':
        errors1['age'] = 'Вы забыли указать возраст!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors, errors1=errors1)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')



@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('/lab3/pay.html', price=price)



@lab3.route('/lab3/end')
def end():
    price = request.args.get('price')
    return render_template('/lab3/end.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    backgroundColor = request.args.get('backgroundColor')
    fontSize = request.args.get('fontSize')
    textshadow = request.args.get('textshadow')
    
    if color or backgroundColor or fontSize or textshadow:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if backgroundColor:
            resp.set_cookie('backgroundColor', backgroundColor)
        if fontSize:
            resp.set_cookie('fontSize', fontSize)
        if textshadow:
            resp.set_cookie('textshadow', textshadow)
        return resp

    color = request.cookies.get('color')
    backgroundColor = request.cookies.get('backgroundColor')
    fontSize = request.cookies.get('fontSize')
    textshadow = request.cookies.get('textshadow')
    return render_template('lab3/settings.html', color=color, backgroundColor=backgroundColor, fontSize=fontSize, textshadow=textshadow)