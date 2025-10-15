from flask import Blueprint, url_for, request, redirect, abort, render_template, make_response
import datetime
lab3 = Blueprint('lab3', __name__)

@lab3.route("/lab3/")
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


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
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
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


products = [
    {"name": "Смартфон Samsung Galaxy S21", "price": 59999, "brand": "Samsung", "color": "черный", "storage": "128GB"},
    {"name": "Смартфон Apple iPhone 13", "price": 79999, "brand": "Apple", "color": "белый", "storage": "128GB"},
    {"name": "Смартфон Xiaomi Redmi Note 11", "price": 19999, "brand": "Xiaomi", "color": "синий", "storage": "64GB"},
    {"name": "Смартфон Google Pixel 6", "price": 54999, "brand": "Google", "color": "зеленый", "storage": "128GB"},
    {"name": "Смартфон OnePlus 9", "price": 45999, "brand": "OnePlus", "color": "фиолетовый", "storage": "128GB"},
    {"name": "Смартфон Samsung Galaxy A52", "price": 24999, "brand": "Samsung", "color": "голубой", "storage": "128GB"},
    {"name": "Смартфон Apple iPhone 12", "price": 64999, "brand": "Apple", "color": "красный", "storage": "64GB"},
    {"name": "Смартфон Realme 8", "price": 15999, "brand": "Realme", "color": "черный", "storage": "128GB"},
    {"name": "Смартфон Huawei P50", "price": 49999, "brand": "Huawei", "color": "золотой", "storage": "256GB"},
    {"name": "Смартфон Sony Xperia 5 III", "price": 69999, "brand": "Sony", "color": "черный", "storage": "128GB"},
    {"name": "Смартфон Oppo Find X3", "price": 44999, "brand": "Oppo", "color": "синий", "storage": "256GB"},
    {"name": "Смартфон Vivo X70", "price": 39999, "brand": "Vivo", "color": "черный", "storage": "128GB"},
    {"name": "Смартфон Motorola Edge 20", "price": 29999, "brand": "Motorola", "color": "белый", "storage": "128GB"},
    {"name": "Смартфон Nokia G50", "price": 18999, "brand": "Nokia", "color": "синий", "storage": "128GB"},
    {"name": "Смартфон Apple iPhone SE", "price": 39999, "brand": "Apple", "color": "красный", "storage": "64GB"},
    {"name": "Смартфон Samsung Galaxy Z Flip3", "price": 89999, "brand": "Samsung", "color": "фиолетовый", "storage": "256GB"},
    {"name": "Смартфон Xiaomi Mi 11 Lite", "price": 27999, "brand": "Xiaomi", "color": "розовый", "storage": "128GB"},
    {"name": "Смартфон Google Pixel 5a", "price": 34999, "brand": "Google", "color": "черный", "storage": "128GB"},
    {"name": "Смартфон OnePlus Nord 2", "price": 31999, "brand": "OnePlus", "color": "синий", "storage": "128GB"},
    {"name": "Смартфон Asus Zenfone 8", "price": 42999, "brand": "Asus", "color": "черный", "storage": "128GB"}
]


@lab3.route('/lab3/products')
def products_search():
    prices = [p['price'] for p in products]
    min_all = min(prices)
    max_all = max(prices)

    if request.args.get('reset'):
        resp = make_response(redirect('/lab3/products'))
        resp.delete_cookie('min_price')
        resp.delete_cookie('max_price')
        return resp
    
    min_price = request.args.get('min_price') or request.cookies.get('min_price', '')
    max_price = request.args.get('max_price') or request.cookies.get('max_price', '')

    if request.args.get('min_price') is not None:
        resp = make_response(redirect('/lab3/products'))
        resp.set_cookie('min_price', min_price)
        resp.set_cookie('max_price', max_price)
        return resp

    filtered_products = products
    
    if min_price or max_price:
        min_val = float(min_price) if min_price else min_all
        max_val = float(max_price) if max_price else max_all
        
        if min_val > max_val:
            min_val, max_val = max_val, min_val
        
        filtered_products = [p for p in products if min_val <= p['price'] <= max_val]
    
    return render_template('lab3/products.html', 
                         products=filtered_products,
                         min_price=min_price,
                         max_price=max_price,
                         min_all=min_all,
                         max_all=max_all)