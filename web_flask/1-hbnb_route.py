#!/usr/bin/python3
"""
This is a simple module that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

app.config['RESTFUL_URL_PREFIX'] = False


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
