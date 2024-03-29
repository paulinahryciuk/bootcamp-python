from flask import Flask,render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def start():
    return "Hello"

@app.route('/<imie>')
def start_imie(imie):
    return f"Hello {imie}"

@app.route('/str')
def strona():
    return render_template('strona.html')

@app.route('/formularz', methods = ['GET','POST'])
def formularz():
    # print(request.method)
    if request.method == 'GET':
        return render_template('formularz.html')
    else:
        zmienna = request.form['wartosc']
        # return redirect(url_for('strona'))
        return redirect('str')


if __name__ == '__main__':
    app.run(debug=True)

# {request.form['wartosc']