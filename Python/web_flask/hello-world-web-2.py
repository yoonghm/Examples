#!/usr/bin/env python3

# hello-world-web-2.py

from flask import Flask

app = Flask(__name__)

def index():
  return '<h1>Hello World!</h1>'

app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
  app.run()
