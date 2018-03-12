#!/usr/bin/env python3

# hello-world-web-2.py
# 
# This example uses add_url_rule() instead of decorator 
# to bind URL to view function
#

from flask import Flask

app = Flask(__name__)

def index():
  return '<h1>Hello World!</h1>'

app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
  app.run()
