from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/Przemek')
def hello_przemek():
    return 'Hello, Przemku!'

@app.route('/imag')
def imag():
    return '<img src = "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg">'


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET. '
    

@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'   

@app.route('/<number>')
def number(number):
        number = int(number)
        answer = ""
        if(number % 2 == 0):
            answer = answer + "Liczba jest podzielna przez 2 \n"
        if(number % 3 == 0):
            answer = answer + "Liczba jest podzielna przez 3 \n"
        if(number % 5 == 0):
            answer = answer + "Liczba jest podzielna przez 5 \n"
        return answer  

@app.route('/about/<name>/<age>/<job>')
def about_name(name, age, job):
    return render_template("about.html", name = name, age = age, job = job)   
   


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
