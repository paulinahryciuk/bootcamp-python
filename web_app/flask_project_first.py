from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World!!!!!'

@app.route('/about')
def about():
    a=10
    b=1
    return '<h1>We are programrers</h1>'.format(a/b)

@app.route('/cantor/<currency>/<int:amount>')
def cabtor(currency, amount):
    message = f'<h1> You selected {currency} and {amount}</h1>'
    return message

if __name__ == '__main__':
    app.run(debug=True)