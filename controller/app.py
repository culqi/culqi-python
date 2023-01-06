from flask import Flask, request
from flask_restful import Resource, Api
from copy import deepcopy
from uuid import uuid4
from data import Data
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
port = 5100

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))


class charge(Resource):
    @property
    def card_data(self):
        self.metadata = {"order_id": "0001"}
        # pylint: disable=no-member
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.TOKEN)
        token_data["email"] = email
        token = self.culqi.token.create(data=token_data)
        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = self.culqi.customer.create(data=customer_data)

        return {
            "token_id": token["data"]["id"],
            "customer_id": customer["data"]["id"],
        }
    def post(self):
        body = request.json
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"

        self.culqi = Culqi(self.public_key, self.private_key)
        self.charge = Charge(client=self.culqi)
        if len(body) > 2:
            data = {
                "amount": body["amount"],
                "currency_code": body["currency_code"],
                "email": body["email"],
                "source_id": body["source_id"],
                "authentication_3DS": body["authentication_3DS"]
            }
        else:
            data = {
                "amount": body["amount"],
                "currency_code": body["currency_code"],
                "email": body["email"],
                "source_id": body["source_id"],
            }
        card = self.charge.create(data)
        response = app.response_class(
            response=json.dumps(card["data"]),
            status=200,
            mimetype='application/json'
        )
        return response


api.add_resource(charge, '/culqi/generateCharge')
class topic_tags(Resource):
    @property
    def card_data(self):
        self.metadata = {"order_id": "0001"}
        # pylint: disable=no-member
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.TOKEN)
        token_data["email"] = email
        token = self.culqi.token.create(data=token_data)
        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = self.culqi.customer.create(data=customer_data)

        return {
            "token_id": token["data"]["id"],
            "customer_id": customer["data"]["id"],
        }
    def post(self):
        body = request.json
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"

        self.culqi = Culqi(self.public_key, self.private_key)
        self.card = Card(client=self.culqi)
        if len(body) > 2:
            data = {
                "token_id": body["token_id"],
                "customer_id": body["customer_id"],
                "authentication_3DS": body["authentication_3DS"]
            }
        else:
            data = {
                "token_id": body["token_id"],
                "customer_id": body["customer_id"]
            }
        card = self.card.create(data)
        response = app.response_class(
            response=json.dumps(card["data"]),
            status=200,
            mimetype='application/json'
        )
        return response


api.add_resource(topic_tags, '/culqi/generateCards')

class customers(Resource):
    def post(self):
        body = request.json
        self.version = __version__

        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"

        self.culqi = Culqi(self.public_key, self.private_key)
        self.customer = Customer(client=self.culqi)
        data = {
            "first_name": body["first_name"],
            "last_name": body["last_name"],
            "email": body["email"],
            "address": body["address"],
            "address_city": body["address_city"],
            "country_code": body["country_code"],
            "phone_number": body["phone_number"],
        }
        card = self.customer.create(data)
        response = app.response_class(
            response=json.dumps(card["data"]),
            status=200,
            mimetype='application/json'
        )
        return response


api.add_resource(customers, '/culqi/generateCustomer')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)