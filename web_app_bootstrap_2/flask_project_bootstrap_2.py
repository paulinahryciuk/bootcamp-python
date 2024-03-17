import sqlite3
from datetime import date

from flask import Flask, render_template, request, flash, g, redirect, url_for, session

import binascii
import hashlib
import random
import string

app_info = {
    'db_file': 'data/cantor.db'
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KluczTrudnyDoZlamania123!!!'


def get_db():
    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        print(error)


class UserPass:
    def __init__(self,user='', password=''):
        self.user = user
        self.password = password

    def hash_password(self):
        os_urandom_static = b'\xe2sG}\xfd\xc0\xd0\xbb\xda\xad\x84\xc30-\xc2\x1c\x860\x1c\x1a\x91\xf3\xe7kr\xf1AM$x\xc4\x08\x89\xaa"L\xe7R\'"\xf1\xc5\x805\xdez[%\x05\xd2j\x1f\x0c\\\xdfX\xa5$$\xe2'
        salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', self.password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return(salt+ pwdhash).decode('ascii')

    def verify_password(self,stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('utf-8'),
                                      10000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
    def get_random_user_password(self):
        random_user = ''.join(random.choice(string.ascii_lowercase) for i in range(3))
        self.user = random_user

        password_characters = string.ascii_letters
        random_password = ''.join(random.choice(password_characters) for i in range(3))
        self.password = random_password

    def login_user(self):
        db = get_db()
        sql_statement = 'SELECT id, name, email, password, is_active, is_admin FROM users WHERE name=?'
        cur = db.execute(sql_statement, [self.user])
        user_record = cur.fetchone()

        if user_record!=None and self.verify_password(user_record['password'], self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', active_menu='login')
    else:
        user_name = '' if "user_name" not in request.form else request.form['user_name']
        user_pass = '' if "user_pass" not in request.form else request.form['user_pass']

    login = UserPass(user_name, user_pass)
    login_record = login.login_user()

    if login_record !=None:
        session['user'] = user_name
        flash(f"Login succesfull, welcome {user_name}")
        return redirect(url_for('index'))
    else:
        flash("login failed, try again!")
        return render_template('login.html', active_menu= 'login')

@app.route('/')

@app.route('/init_app')
def init_app():
    db = get_db()
    sql_statement = 'SELECT COUNT (*) AS cnt FROM users WHERE is_active AND is_admin;'
    cur = db.execute(sql_statement)
    active_admins = cur.fetchone()

    if active_admins !=None and active_admins['cnt'] >0:
        flash('Application is already set-up. Nothing to do')
        return redirect(url_for('index'))
    user_pass = UserPass()
    user_pass.get_random_user_password()
    db.execute('''
    INSERT INTO users(name, email, password, is_active, is_admin)
    VALUES(?,?,?,True,True);
    ''', [user_pass.user, 'none@no.no', user_pass.hash_password()])
    db.commit()
    flash('User {} with password {} has been added'.format(user_pass.user, user_pass.password))
    return redirect(url_for('index'))


class Currency:
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return f'<Currency {self.code}>'


class CantorOffer:
    def __init__(self):
        self.currencies = []
        self.danied_codes = []

    def load_offer(self):
        """
        laduje dane do systemu
        :return:
        """
        self.currencies.append(Currency('USD', "Dollar", 'currencies/1.jpg'))
        self.currencies.append(Currency('EUR', "Euro", 'currencies/2.jpg'))
        self.currencies.append(Currency('PLN', "Zloty", 'kantor.png'))
        self.currencies.append(Currency('GBP', "Funt", 'currencies/3.jpg'))
        self.currencies.append(Currency('RUB', "Rubel", 'kantor.png'))
        self.danied_codes.append('RUB')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'kantor.png')


@app.route("/")
def index():
    # return 'This is index'
    return render_template('index.html', active_menu='home')


@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer, active_menu='exchange')
    else:
        flash("Debug: starting exchange in POST mode")
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = "100"
        if 'amount' in request.form:
            amount = request.form['amount']

        if currency in offer.danied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The selected currency is unknown and cannot be actepted')
        else:
            db = get_db()
            sql_command = "INSERT INTO transactions(currency, amount, user) values(?,?,?);"
            db.execute(sql_command, [currency, amount, 'admin'])
            db.commit()
            flash('Request to exchange {} was accepted'.format(currency))

        return render_template('exchange_results.html', currency=currency, amount=amount,
                               active_menu='exchange', currency_info=offer.get_by_code(currency))


@app.route('/history')
def history():
    db = get_db()
    sgl_command = 'SELECT id, currency, amount, trans_date FROM transactions;'
    cur = db.execute(sgl_command)
    transactions = cur.fetchall()

    return render_template('history.html', transactions=transactions, active_menu='history')

@app.route("/delete_tarnsaction/<int:transaction_id>")
def delete_transaction(transaction_id):
    db = get_db()
    sql_statement = 'delete from transactions where id = ?;'
    db.execute(sql_statement, [transaction_id])
    db.commit()

    return redirect(url_for('history'))

@app.route("/edit_transaction/<int:transaction_id>", methods=['GET', 'POST'])
def edit_transaction(transaction_id):

    offer = CantorOffer()
    offer.load_offer()
    db=get_db()

    if request.method == 'GET':
        sql_statement = 'SELECT id, currency, amount from transactions WHERE id =?;'
        cur = db.execute(sql_statement, [transaction_id])
        transaction = cur.fetchone()

        if transaction == None:
            flash("no such transaction!")
            return redirect(url_for('history'))
        else:
            return render_template('edit_transaction.html', transaction = transaction,
                                   offer=offer, active_menu='history')
    else:
        flash("Debug: starting exchange in POST mode")
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = "100"
        if 'amount' in request.form:
            amount = request.form['amount']

        if currency in offer.danied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The selected currency is unknown and cannot be actepted')
        else:
            db = get_db()
            sql_command = '''UPDATE transactions SET
            currency=?,
            amount=?,
            user=?,
            trans_date=?
            WHERE id=?;'''
            db.execute(sql_command, [currency, amount, 'admin', date.today(), transaction_id])
            db.commit()
            flash('Transaction was updated')

        return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(debug=True)
