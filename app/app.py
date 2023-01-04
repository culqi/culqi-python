from flask import Flask, request
from flask_restful import Resource, Api
import sys
from copy import deepcopy
from uuid import uuid4
from data import Data
from culqi.client import Culqi


app = Flask(__name__)
api = Api(app)
port = 5100

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

class topic_tags(Resource):
    def get(self):
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.TOKEN)
        token_data["email"] = email
        token = Culqi.token.create(data=token_data)
        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = Culqi.customer.create(data=customer_data)

        return {
            "token_id": token["data"]["id"],
            "customer_id": customer["data"]["id"],
        }


api.add_resource(topic_tags, '/culqi/generateCards')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)