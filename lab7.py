from flask import Blueprint, url_for, request, redirect, abort, render_template, make_response, session, jsonify
import datetime
lab7 = Blueprint('lab7', __name__)

@lab7.route("/lab7/")
def main():
    return render_template('lab7/index.html')


films = [
    {
        "title": "comeback",
        "title_ru": "Камбек",
        "year": 2025,
        "description": "Нижний Новгород, начало 2000-х. В телефонах — только звонки и \
            «змейка», во дворах качают под Дельфина и Hi-Fi, а богатые чаще всего связаны \
            с криминалом. Трое школьных друзей — Юра, Птаха и Олег — решают выручить\
            одноклассницу Дашу, но вместо этого вляпываются в серьёзные неприятности.\
            И неожиданно их спасает бездомный по прозвищу Компот. Он скитается в\
            поисках заработка, его подкармливают в школьной столовой, а сам он ничего\
            не помнит о своём прошлом — однажды он просто очнулся после тяжелых травм.\
            Ребята понимают: этот человек спас им жизнь, и теперь они хотят раскопать\
            тайну Компота и помочь ему вернуть себя настоящего."
    },
    {
        "title": "Brotherly",
        "title_ru": "По-братски",
        "year": 2025,
        "description": "Антон и Света Лебедевы приняли ответственное решение:\
            они хотят развестись. Из-за бюрократических проблем им необходимо\
            отправиться в путешествие в далекий северный городок Нежногорье,\
            где их когда-то поженили. К ним на выручку приходит безумная\
            соседская семейка — Валентин и Варвара Бублики, а также\
            их озорной сын Платон Валентинович, которые случайно отправляются\
            по тому же маршруту. Антон и Света вынуждены согласиться поехать \
            с ними, не предполагая, какие безумные приключения ждут их на этом пути."
    },
    {
        "title": "The Shawshank Redemption",
        "title_ru": "Побег из Шоушенка",
        "year": 1994,
        "description": "Бухгалтер Энди Дюфрейн обвинён в убийстве собственной\
            жены и её любовника. Оказавшись в тюрьме под названием Шоушенк,\
            он сталкивается с жестокостью и беззаконием, царящими по обе\
            стороны решётки. Каждый, кто попадает в эти стены, становится\
            их рабом до конца жизни. Но Энди, обладающий живым умом и доброй душой,\
            находит подход как к заключённым, так и к охранникам, добиваясь их особого к себе расположения."
    }
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)

    return films[id]


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404)

    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404)

    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    films[id] = film
    return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    
    films.append(film)
    new_id = len(films) -1
    return str(new_id), 201