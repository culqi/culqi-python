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
        self.public_key = "pk_test_da33560a681ff246"
        self.private_key = "sk_test_93fd5e4babc0f7a6"
        self.culqi = Culqi(self.public_key, self.private_key)
        self.token = Token(client=self.culqi)

        self.token_data = deepcopy(Data.TOKEN)
        self.yape_data = deepcopy(Data.YAPE)
        self.metadata = {"order_id": "0001"}

        #ecnrypt variables
        self.rsa_public_key = "-----BEGIN PUBLIC KEY-----\n"+\
        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDuCmwMoEzvBk++m4rZUlZL4pDD\n"+\
        "W++NV1tSjAOJsRv5Ermg3/ygjINNhi1gfMbfSiWloc85tJBZhXzD7JpOd7JxOOg7\n"+\
        "CicgbZKGF/sq2geoVw4+n4j4vUZx0+a1PgStwR+BeZn2I+eAn9xOrHJD6/baJqIO\n"+\
        "/ifGJ1e5jHeQXIR4IwIDAQAB\n"+\
        "-----END PUBLIC KEY-----"
        self.rsa_id = "30b83fd0-8709-4fe4-86c1-fef042c3c2c3"

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
        print(retrieved_token)
        assert created_token["data"]["id"] == retrieved_token["data"]["id"]

    @pytest.mark.vcr()
    def test_token_list(self):
        retrieved_token_list = self.token.list()
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
