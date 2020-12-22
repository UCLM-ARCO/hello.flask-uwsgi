#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
