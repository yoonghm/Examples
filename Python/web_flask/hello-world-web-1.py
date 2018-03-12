#!/usr/bin/env python3

# hello-world-web-1.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return '<h1>Hello World!</h1>'

'''
To run the script,
  FLASK_APP=hello-world-web-1.py flask run
'''
