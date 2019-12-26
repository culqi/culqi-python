import os
import unittest
from copy import deepcopy

from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Token, Charge


class ChargeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.client = Client(self.api_key, self.api_secret)
        self.token = Token(client=self.client)
        self.charge = Charge(client=self.client)

        self.data = {
            "token": {
                "cvv": "123",
                "card_number": "4111111111111111",
                "expiration_year": "2020",
                "expiration_month": "09",
                "email": "richard@piedpiper.com",
            },
            "charge": {
                "amount": "1000",
                "capture": False,
                "currency_code": "PEN",
                "description": "Venta de prueba",
                "email": "richard@piedpiper.com",
                "installments": 0,
                "metadata": {
                    "test": "charge"
                },
                "source_id": None
            }
        }

        self.metadata = {
            "order_id": "0001"
        }

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.charge._get_url() == "https://api.culqi.com/v2/charges"
        assert self.charge._get_url(id_) == "https://api.culqi.com/v2/charges/{0}".format(id_)
        assert self.charge._get_url(id_, "capture") == "https://api.culqi.com/v2/charges/{0}/capture".format(id_)

    def test_charge_create(self):
        token_data = deepcopy(self.data["token"])
        token = self.token.create(data=token_data)

        charge_data = deepcopy(self.data["charge"])
        charge_data["source_id"] = token["data"]["id"]
        charge = self.charge.create(data=charge_data)

        assert charge["data"]["object"] == "charge"

    def test_charge_capture(self):
        token_data = deepcopy(self.data["token"])
        token = self.token.create(data=token_data)

        charge_data = deepcopy(self.data["charge"])
        charge_data["source_id"] = token["data"]["id"]
        created_charge = self.charge.create(data=charge_data)
        captured_charge = self.charge.capture(id_=created_charge['data']['id'])

        assert captured_charge["data"]["id"] == created_charge["data"]["id"]
        assert captured_charge['status'] == 201

    def test_charge_retrieve(self):
        token_data = deepcopy(self.data["token"])
        token = self.token.create(data=token_data)

        charge_data = deepcopy(self.data["charge"])
        charge_data["source_id"] = token["data"]["id"]
        created_charge = self.charge.create(data=charge_data)
        retrieved_charge = self.charge.read(created_charge["data"]["id"])

        assert created_charge["data"]["id"] == retrieved_charge["data"]["id"]

    def test_charge_list(self):
        retrieved_charge_list = self.charge.list()
        assert "items" in retrieved_charge_list["data"]

    def test_charge_update(self):
        token_data = deepcopy(self.data["token"])
        token = self.token.create(data=token_data)

        charge_data = deepcopy(self.data["charge"])
        charge_data["source_id"] = token["data"]["id"]
        created_charge = self.charge.create(data=charge_data)

        metadatada = {
            "metadata": self.metadata
        }
        updated_charge = self.charge.update(id_=created_charge["data"]["id"], data=metadatada)

        assert created_charge["data"]["id"] == created_charge["data"]["id"]
        assert updated_charge["data"]["metadata"]["order_id"] == self.metadata["order_id"]

if __name__ == "__main__":
    unittest.main()
