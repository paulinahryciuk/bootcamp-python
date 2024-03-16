from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route("/")
def wyswietlenie():
    return "hello"

@app.route("/imie/<imie>")
def wyswietlenie_imie (imie):
    return f"hello {imie}"


lista = ["posprzatc", "zrobic zakupy"]

# @app.route('/todo', method = ["GET", "POST"])
# def zadania():
#     if request.method == "POST":
#         request.form['taski']
#     return render_template("todo.html", taski = lista)

@app.route("/menu")
def start():
    return render_template("main.html")



if __name__ == '__main__':
    app.run(debug = True)

