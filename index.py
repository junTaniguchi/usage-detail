# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:45:40 2020

@author: tie305403
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login/?')
def login():
    return "Hello World"

@app.route('/api/get/point=?')
def get_point():
    return "Hello World"

@app.route('/api/get/balance=?')
def get_balance():
    return "Hello World"

@app.route('/api/get/details=?')
def get_details():
    return "Hello World"

@app.route('/api/post/point=?')
def post_point():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)