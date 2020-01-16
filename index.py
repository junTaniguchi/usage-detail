# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:45:40 2020

@author: tie305403
"""

from flask import Flask, render_template, jsonify
#from flask_restplus import Api, Resource, fields

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login/', methods=['POST'])
def login():
    message = "Hello World"
    return jsonify({'message': message})

@app.route('/api/get/point', methods=['GET'])
def get_point():
    message = "Hello World"
    return jsonify({'message': message})

@app.route('/api/get/balance', methods=['GET'])
def get_balance():
    message = "Hello World"
    return jsonify({'message': message})

@app.route('/api/get/details', methods=['GET'])
def get_details():
    message = "Hello World"
    return jsonify({'message': message})

@app.route('/api/post/point', methods=['GET'])
def post_point():
    message = "Hello World"
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)