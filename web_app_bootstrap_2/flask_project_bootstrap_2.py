from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'KluczTrudnyDoZlamania123!!!'

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
        self.currencies.append(Currency('USD',"Dollar", 'currencies/1.jpg'))
        self.currencies.append(Currency('EUR',"Euro", 'currencies/2.jpg'))
        self.currencies.append(Currency('PLN',"Zloty", 'kantor.png'))
        self.currencies.append(Currency('GBP',"Funt", 'currencies/3.jpg'))
        self.currencies.append(Currency('RUB',"Rubel", 'kantor.png'))
        self.danied_codes.append('RUB')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'kantor.png')

@app.route("/")
def index():
    # return 'This is index'
    return render_template(('index.html'))

@app.route("/exchange", methods=['GET','POST'])
def exchange():

    offer = CantorOffer()
    offer.load_offer()


    if request.method=='GET':
        return render_template('exchange.html', offer=offer)
    else:
        flash("Debug: starting exchange in POST mode")
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form['currency']

        if currency in offer.danied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The selected currency is unknown and cannot be actepted')
        else:
            flash('Request to exchange {} was accepted'.format(currency))

        amount = "EUR"
        if 'amount' in request.form:
            amount = request.form['amount']

        return render_template('exchange_results.html', currency = currency, amount= amount,
                               currency_info=offer.get_by_code(currency))

if __name__ == '__main__':
    app.run(debug=True)