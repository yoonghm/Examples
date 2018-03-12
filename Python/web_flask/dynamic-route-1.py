#!/usr/bin/env python3

# dynamic-route-1.py
#
# URL is matched using pattern matching 
# and variables
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
  return '<h1>Hello, {}!</h1>', format(name)
