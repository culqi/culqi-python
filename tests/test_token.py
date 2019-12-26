import os
import unittest

from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Token


class TokenTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.client = Client(self.api_key, self.api_secret)
        self.token = Token(client=self.client)

        self.data = {
            "cvv": "123",
            "card_number": "4111111111111111",
            "expiration_year": "2020",
            "expiration_month": "09",
            "email": "richard@piedpiper.com",
        }

        self.metadata = {
            "order_id":"0001"
        }

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.token._get_url() == "https://api.culqi.com/v2/tokens"
        assert self.token._get_url(id_) == "https://api.culqi.com/v2/tokens/{0}".format(id_)

    def test_token_create(self):
        token = self.token.create(data=self.data)
        assert token["data"]["object"] == "token"

    def test_token_retrieve(self):
        created_token = self.token.create(data=self.data)
        retrieved_token = self.token.read(created_token["data"]["id"])
        assert created_token["data"]["id"] == retrieved_token["data"]["id"]

    def test_token_list(self):
        retrieved_token_list = self.token.list()
        assert "items" in retrieved_token_list["data"]

    def test_token_update(self):
        metadatada = {
            "metadata": self.metadata
        }
        created_token = self.token.create(data=self.data)
        updated_token = self.token.update(id_=created_token["data"]["id"], data=metadatada)

        assert created_token["data"]["id"] == created_token["data"]["id"]
        assert updated_token["data"]["metadata"] == self.metadata

if __name__ == "__main__":
    unittest.main()
