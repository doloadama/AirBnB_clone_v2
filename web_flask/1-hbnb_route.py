#!/usr/bin/python3
'''A simple flask application
'''
from flask import Flask


app = flask(__name__)
'''The flask application instance.'''
app.url_map.strict_slashes = False

@app.route('/')
def index():
    '''The homme page'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb page'''
    return 'HBNB'
