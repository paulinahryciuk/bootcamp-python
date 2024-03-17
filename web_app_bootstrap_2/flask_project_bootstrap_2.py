import sqlite3
from datetime import date

from flask import Flask, render_template, request, flash, g, redirect, url_for

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
