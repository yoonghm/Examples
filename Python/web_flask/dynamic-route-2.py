#!/usr/bin/env python3

# dynamic-route-2.py
#
# URL is matched using pattern matching ,
# variable and converter
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/user/id/<int:user_id>')
def id(name):
  # Get user name from database va user_id
  return '<h1>Hello, user with id: {}!</h1>'.format(name)

if __name__ == '__main__':
  app.run()
