from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return "Hello! Use add/1/2 subtract/1/2 multiply/1/2 or divide/1/2 to use the calculator"

@app.route('/add/<num1>/<num2>')
def add_nums(num1,num2):
    return str(int(int(num1) + int(num2)))

@app.route('/subtract/<num1>/<num2>')
def subtract_nums(num1,num2):
    return str(int(int(num1) - int(num2)))

@app.route('/multiply/<num1>/<num2>')
def multiply_nums(num1,num2):
    return str(int(int(num1) * int(num2)))

@app.route('/divide/<num1>/<num2>')
def divide_nums(num1,num2):
    if num2 == 0:
        return "Invalid operation, can't divide by zero"
    else:
        return str(round((int(num1) / int(num2)), 2))