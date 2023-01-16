from flask import Flask, request, render_template
from flask_restful import Resource, Api
from copy import deepcopy
from uuid import uuid4

from pathlib import Path
import sys
from flask import json

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Card
from culqi.resources import Customer
from culqi.resources import Charge


app = Flask(__name__)
api = Api(app)
public_key = "pk_test_90667d0a57d45c48"
private_key = "sk_test_1573b0e8079863ff"
port = 5100


if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

@app.route('/',  methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/card')
def card():
    return render_template('index-card.html')

@app.route('/culqi/generateCards',  methods=['POST'])
def generatecard():
    body = request.json
    version = __version__

    culqi = Culqi(public_key, private_key)
    card = Card(client=culqi)


    card = card.create(body)
    response = app.response_class(
        response=json.dumps(card["data"]),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/culqi/generateCustomer',  methods=['POST'])
def generatecutomer():
    body = request.json
    version = __version__

    culqi = Culqi(public_key, private_key)
    customer = Customer(client=culqi)
    data = {
        "first_name": body["first_name"],
        "last_name": body["last_name"],
        "email": body["email"],
        "address": body["address"],
        "address_city": body["address_city"],
        "country_code": body["country_code"],
        "phone_number": body["phone_number"],
    }
    card = customer.create(data)
    response = app.response_class(
        response=json.dumps(card["data"]),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/culqi/generateCharge',  methods=['POST'])
def generatecharge():
    body = request.json
    version = __version__

    culqi = Culqi(public_key, private_key)
    charge = Charge(client=culqi)
    card = charge.create(body)
    print(card)
    response = app.response_class(
        response=json.dumps(card["data"]),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

