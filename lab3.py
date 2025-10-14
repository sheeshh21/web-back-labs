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
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    opacity = request.args.get('opacity')

    if color or bg_color or font_size or opacity:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if opacity:
            resp.set_cookie('opacity', opacity)
        return resp

    color = request.cookies.get('color')
    bg_color = request.cookies.get('bg_color')
    font_size = request.cookies.get('font_size')
    opacity = request.cookies.get('opacity')
    return render_template('lab3/settings.html', color=color, bg_color=bg_color, font_size=font_size, opacity=opacity)

@lab3.route('/lab3/clear')
def clear():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('opacity')
    return resp

@lab3.route('/lab3/ticket')
def ticket():
    return render_template('lab3/ticket.html')

@lab3.route('/lab3/itogticket')
def itogticket():
    price = 0

    age = int(request.args.get('age'))
    if age < 18:
        price = 700
        child = True
    else:
        price = 1000
        child = False

    position = request.args.get('position')
    if position == 'lower' or position == 'lowerside':
        price += 100

    belie = request.args.get('belie')
    if belie == 'on':
        price += 75

    bagaj = request.args.get('bagaj')
    if bagaj == 'on':
        price += 250

    strahovka = request.args.get('strahovka')
    if strahovka == 'on':
        price += 150

    return render_template('lab3/itogticket.html',price=price, child=child, strahovka=strahovka, bagaj=bagaj, 
                            belie=belie, position=position, age=age, fio=request.args.get('fio'),
                            viezd=request.args.get('viezd'),
                            naznach=request.args.get('naznach'),
                            data=request.args.get('data'))