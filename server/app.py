#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route: Index
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

# Route: /print/<parameter>
@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  # Console output
    return f'{parameter}', 200

# Route: /count/<int:num>
@app.route('/count/<int:num>')
def count(num):
    output = ""
    for i in range(num):
        output += f"{i}\n"
    return output, 200

# Route: /math/<int:num1>/<op>/<int:num2>
@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result), 200
