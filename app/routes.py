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

    # .json() converts string response into Python dictionary
    response = requests.get(url).json()

    print(response)
    return render_template('index.html', response=response)


@app.route('/api/customers/', methods=['GET', 'POST'])
def apiCustomers():
    name = request.args.get('name')

    customers = [
        {
            'name': 'John',
            'age': 22
        },
        {
            'name': 'Alex',
            'age': 12
        },
        {
            'name': 'Annie',
            'age': 67
        },
        {
            'name': 'Jake',
            'age': 45
        },
        {
            'name': 'Bill',
            'age': 32
        },
    ]

    try:
        for customer in customers:
            if customer['name'] == name:
                return jsonify(customer)
    except:
        return jsonify({'Error 5000': 'Something went wrong'})

    return jsonify({'Error 304': 'No customer found'})


@app.route('/api/customers/age/', methods=['GET', 'POST'])
def apiCustomersAge():
    min = request.args.get('min')
    max = request.args.get('max')

    # print(request.args)

    # name is optional
    name = request.args.get('name')

    customers = [
        {
            'name': 'John',
            'age': 22
        },
        {
            'name': 'Alex',
            'age': 12
        },
        {
            'name': 'Annie',
            'age': 67
        },
        {
            'name': 'Jake',
            'age': 45
        },
        {
            'name': 'Bill',
            'age': 32
        },
    ]

    try:
        results = []

        for customer in customers:
            if int(min) < customer['age'] and customer['age'] < int(max):
                results.append(customer)

        if name:
            customers = []
            for customer in results:
                if customer['name'] == name:
                    return jsonify(customer)

        return jsonify(results)
    except:
        return jsonify({'Error': 'Incompatible parameter values'})

    return jsonify({'error': 'Something went wrong'})


@app.route('/api/coords/', methods=['GET', 'POST'])
def coords():
    city = request.headers.get('city')

    API_KEY = app.config['WEATHER_API_KEY']

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial'

    try:
        # json() method converts string response into python dictionary
        response = requests.get(url).json()

        return jsonify({'city': response['name']})
    except:
        return jsonify({'error': 'City does not exist'})
