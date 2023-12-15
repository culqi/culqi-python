import os
import unittest
from copy import deepcopy

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Token

from .data import Data


class TokenTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TokenTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"
        self.culqi = Culqi(self.public_key, self.private_key)
        self.token = Token(client=self.culqi)

        self.token_data = deepcopy(Data.TOKEN)
        self.yape_data = deepcopy(Data.YAPE)
        self.metadata = {"order_id": "0001"}

        #ecnrypt variables
        self.rsa_public_key = "-----BEGIN PUBLIC KEY-----\n"+\
        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgd5UbyW6+DysTvwvS6fKzXK7j\n"+\
        "smjKWPSHcjw8sSTr3rARRYMmOKgDI2ZbfsfcBedHp0ZjsrL/2owXV4N+GYTjheuj\n"+\
        "VQl2g0rdu9JpYbxe5zSXNptjIPYjwFOzIt5ODotcwgcurA6XlU63zZZuCcUQSgka\n"+\
        "2B7gmga5bxUZA6dAHwIDAQAB\n"+\
        "-----END PUBLIC KEY-----"
        self.rsa_id = "82d2e538-9b07-4f0b-b615-9d7f028c825b"

    @pytest.mark.vcr()
    def test_token_create(self):
        token = self.token.create(data=self.token_data)
        print(token)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create_encrypt(self):
        options = {}
        options["rsa_public_key"] = self.rsa_public_key
        options["rsa_id"] = self.rsa_id
        token = self.token.create(data=self.token_data, **options)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_yape_create(self):
        token = self.token.createyape(data=self.yape_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_yape_create_encrypt(self):
        options = {}
        options["rsa_public_key"] = self.rsa_public_key
        options["rsa_id"] = self.rsa_id
        token = self.token.createyape(data=self.yape_data, **options)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_retrieve(self):
        created_token = self.token.create(data=self.token_data)
        retrieved_token = self.token.read(created_token["data"]["id"])
        assert created_token["data"]["id"] == retrieved_token["data"]["id"]

    @pytest.mark.vcr()
    def test_token_list(self):
        querystring = {
            "creation_date": "1476132639",
            "creation_date_from": "1476132639",
            "creation_date_to": "1476132639",
            "card_brand": "Visa",
            "card_type": "credito",
            "device_type": "mobile",
            "bin": "411111",
            "country_code": "PE",
            "limit": "10",
        }
        retrieved_token_list = self.token.list(querystring)
        assert "items" in retrieved_token_list["data"]

    @pytest.mark.vcr()
    def test_token_update(self):
        metadatada = {"metadata": self.metadata}
        created_token = self.token.create(data=self.token_data)
        updated_token = self.token.update(
            id_=created_token["data"]["id"], data=metadatada
        )

        assert created_token["data"]["id"] == created_token["data"]["id"]
        assert updated_token["data"]["metadata"] == self.metadata


if __name__ == "__main__":
    unittest.main()
