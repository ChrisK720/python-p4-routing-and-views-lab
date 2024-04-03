#!/usr/bin/env python3

from flask import Flask
import operator

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<p>{param}</p>'

@app.route('/count/<int:max_num>')
def count(max_num):
    conv_max_num = int(max_num)

    to_display = f'''
                 <ul>
           
                 
                  '''
    return make_range(conv_max_num,to_display)
def make_range(conv_max_num,to_display):
    
    for num in range(conv_max_num):

        to_display = to_display + f'<li>{num}</li>'
        if num == conv_max_num - 1:
            to_display + '</ul>'
    return to_display

@app.route('/math/<float:num1>/<operation>/<float:num2>')

def math(num1,operation,num2):
    conv_num1 = float(num1)
    conv_num2 = float(num2)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        'div': operator.truediv,
        '%': operator.mod

    }
    result = operations.get(operation)(conv_num1,num2)
    return f'<h1>Answer: {result}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

