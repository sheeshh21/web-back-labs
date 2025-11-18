from flask import Blueprint, url_for, request, redirect, abort, render_template, make_response, session, current_app
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
rgz = Blueprint('rgz', __name__)

@rgz.route('/rgz/')
def rgzz():
    return render_template('rgz/rgz.html', login=session.get('login'))


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'alex_ryazantsev_rgz',
            user = 'alex_ryazantsev_rgz',
            password = '123'
        )
        cur = conn.cursor(cursor_factory = RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@rgz.route("/rgz/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('rgz/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    real_name = request.form.get('real_name')

    if not (login and password):
        return render_template('rgz/register.html', error='Заполните все обязательные поля')
    
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=%s;", (login, ))
    else:
        cur.execute("SELECT login FROM users WHERE login=?;", (login, ))

    if cur.fetchone():
        db_close(conn, cur)
        return render_template('rgz/register.html', error='Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password)
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login, password, real_name) VALUES (%s, %s, %s);", 
                   (login, password_hash, real_name))
    else:
        cur.execute("INSERT INTO users (login, password, real_name) VALUES (?, ?, ?);", 
                   (login, password_hash, real_name))
    
    db_close(conn, cur)
    return render_template('rgz/success.html', login=login)



@rgz.route("/rgz/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('rgz/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('rgz/login.html', error='Заполните поля')
    
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login, ))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('rgz/login.html', error='Логин и/или пароль неверны')
    
    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('rgz/login.html', error='Логин и/или пароль неверны')
    
    session['login'] = login
    db_close(conn, cur)
    return render_template('rgz/success_login.html', login=login)


@rgz.route('/rgz/logout')
def logout():
    session.pop('login', None)
    session.pop('user_id', None)
    return redirect('/rgz')


@rgz.route("/rgz/delete_account", methods=['GET', 'POST'])
def delete_account():
    if not session.get('login'):
        return redirect(url_for('rgz.login'))
    
    if request.method == 'GET':
        return render_template('rgz/delete_account.html')
    
    password = request.form.get('password')
    if not password:
        return render_template('rgz/delete_account.html', error='Введите пароль для подтверждения')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (session['login'],))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (session['login'],))
    user = cur.fetchone()
    
    if not user or not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('rgz/delete_account.html', error='Неверный пароль')
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM users WHERE login=%s;", (session['login'],))
    else:
        cur.execute("DELETE FROM users WHERE login=?;", (session['login'],))
    
    db_close(conn, cur)
    
    session.pop('login', None)
    session.pop('user_id', None)
    
    return render_template('rgz/account_deleted.html')


@rgz.route('/rgz/init_storage')
def init_storage():
    conn, cur = db_connect()
    
    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('''
                CREATE TABLE IF NOT EXISTS storage_cells (
                    id SERIAL PRIMARY KEY,
                    number INTEGER NOT NULL UNIQUE,
                    tenant VARCHAR(100),
                    is_occupied BOOLEAN DEFAULT FALSE
                )
            ''')
            
            for i in range(1, 101):
                cur.execute(
                    "INSERT INTO storage_cells (number, is_occupied) VALUES (%s, %s) ON CONFLICT (number) DO NOTHING",
                    (i, False)
                )
        else:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS storage_cells (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number INTEGER NOT NULL UNIQUE,
                    tenant TEXT,
                    is_occupied BOOLEAN DEFAULT FALSE
                )
            ''')
            
            for i in range(1, 101):
                cur.execute(
                    "INSERT OR IGNORE INTO storage_cells (number, is_occupied) VALUES (?, ?)",
                    (i, False)
                )
        
        db_close(conn, cur)
        return "Ячейки инициализированы успешно!"
    
    except Exception as e:
        db_close(conn, cur)
        return f"Ошибка: {e}"

@rgz.route('/rgz/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    
    if data['method'] == 'info':
        conn, cur = db_connect()
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('SELECT * FROM storage_cells ORDER BY number')
        else:
            cur.execute('SELECT * FROM storage_cells ORDER BY number')
            
        cells = cur.fetchall()
        
        total_cells = len(cells)
        occupied_cells = len([cell for cell in cells if cell['is_occupied']])
        free_cells = total_cells - occupied_cells
        
        db_close(conn, cur)
        
        return {
            'jsonrpc': '2.0',
            'result': {
                'cells': cells,
                'stats': {
                    'total': total_cells,
                    'occupied': occupied_cells,
                    'free': free_cells
                }
            },
            'id': id
        }
    
    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }
    
    elif data['method'] == 'booking':
        cell_number = data['params']
        
        conn, cur = db_connect()
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('SELECT COUNT(*) as count FROM storage_cells WHERE tenant = %s', (login,))
        else:
            cur.execute('SELECT COUNT(*) as count FROM storage_cells WHERE tenant = ?', (login,))
            
        user_cells_count = cur.fetchone()['count']
        
        if user_cells_count >= 5:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 6,
                    'message': 'Cannot book more than 5 cells'
                },
                'id': id
            }
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('SELECT * FROM storage_cells WHERE number = %s', (cell_number,))
        else:
            cur.execute('SELECT * FROM storage_cells WHERE number = ?', (cell_number,))
            
        cell = cur.fetchone()
        
        if not cell:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Cell not found'
                },
                'id': id
            }
        
        if cell['is_occupied']:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 2,
                    'message': 'Already booked'
                },
                'id': id
            }
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('UPDATE storage_cells SET tenant = %s, is_occupied = %s WHERE number = %s', 
                       (login, True, cell_number))
        else:
            cur.execute('UPDATE storage_cells SET tenant = ?, is_occupied = ? WHERE number = ?', 
                       (login, True, cell_number))
            
        db_close(conn, cur)
        
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }
    
    elif data['method'] == 'cancellation':
        cell_number = data['params']
        
        conn, cur = db_connect()
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('SELECT * FROM storage_cells WHERE number = %s', (cell_number,))
        else:
            cur.execute('SELECT * FROM storage_cells WHERE number = ?', (cell_number,))
            
        cell = cur.fetchone()
        
        if not cell:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Cell not found'
                },
                'id': id
            }
        
        if not cell['is_occupied']:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 4,
                    'message': 'Cell is not booked'
                },
                'id': id
            }
        
        if cell['tenant'] != login:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 5,
                    'message': 'You can only cancel your own booking'
                },
                'id': id
            }
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute('UPDATE storage_cells SET tenant = %s, is_occupied = %s WHERE number = %s', 
                       ('', False, cell_number))
        else:
            cur.execute('UPDATE storage_cells SET tenant = ?, is_occupied = ? WHERE number = ?', 
                       ('', False, cell_number))
            
        db_close(conn, cur)
        
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }
    

@rgz.route('/rgz/storage')
def storage_cells():
    return render_template('rgz/storage_cells.html', login=session.get('login'))