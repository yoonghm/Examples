#!/usr/bin/env python3

# hello-world-web-3.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

if __name__ == '__main__':
  app.run()
