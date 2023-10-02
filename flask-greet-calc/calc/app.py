from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

def operate(operation, a, b):
    """Performs the operation and returns a result"""
    if operation == 'add':
        return add(a, b)
    elif operation == 'sub':
        return sub(a, b)
    elif operation == 'mult':
        return mult(a, b)
    elif operation == 'div':
        return div(a,b)
    else:
        return "Not a valid operation."
    
@app.route('/add')
def add_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(operate('add', a, b))

@app.route('/sub')
def sub_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(operate('sub', a, b))

@app.route('/mult')
def mult_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(operate('mult', a, b))

@app.route('/div')
def div_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(operate('div', a, b))

@app.route('/math/<operation>')
def math_route(operation):
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(operate(operation, a, b))