from app import app

# jsonify converts the same way that JSON.stringify does, converts Python
# dictionary into a JS object, which is then stringified and sent.
# request allows us to take parameters in the API call
from flask import render_template, jsonify, request

# Don't confuse with request method above -- this requests is a Python module for calling APIs in Python where the method above is specific to Flask
import requests

# index is going to call weather API and show information on front
@app.route('/')
@app.route('/index')
def index():
    API_KEY = app.config['WEATHER_API_KEY']

    city = 'boston'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial'
    print(API_KEY)
    return render_template('index.html')
