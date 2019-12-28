import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Card

from .data import Data


class CardTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CardTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.client = Client(self.api_key, self.api_secret)
        self.card = Card(client=self.client)

        self.metadata = {"order_id": "0001"}

    @property
    def card_data(self):
        # pylint: disable=no-member
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.TOKEN)
        token_data["email"] = email
        token = self.client.token.create(data=token_data)

        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = self.client.customer.create(data=customer_data)

        return {
            "token_id": token["data"]["id"],
            "customer_id": customer["data"]["id"],
        }

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.card._get_url() == "https://api.culqi.com/v2/cards"
        assert self.card._get_url(id_) == "https://api.culqi.com/v2/cards/{0}".format(
            id_
        )

    @pytest.mark.vcr()
    def test_card_create(self):
        card = self.card.create(data=self.card_data)
        assert card["data"]["object"] == "card"

    @pytest.mark.vcr()
    def test_card_retrieve(self):
        created_card = self.card.create(data=self.card_data)
        retrieved_card = self.card.read(created_card["data"]["id"])
        assert created_card["data"]["id"] == retrieved_card["data"]["id"]

    @pytest.mark.vcr()
    def test_card_list(self):
        retrieved_card_list = self.card.list()
        assert "items" in retrieved_card_list["data"]

    @pytest.mark.vcr()
    def test_card_update(self):
        created_card = self.card.create(data=self.card_data)

        metadatada = {"metadata": self.metadata}
        updated_card = self.card.update(id_=created_card["data"]["id"], data=metadatada)

        assert created_card["data"]["id"] == created_card["data"]["id"]
        assert updated_card["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_card_delete(self):
        created_card = self.card.create(data=self.card_data)
        deleted_card = self.card.delete(id_=created_card["data"]["id"])

        assert deleted_card["data"]["deleted"]
        assert deleted_card["data"]["id"] == created_card["data"]["id"]
        assert deleted_card["status"] == 200


if __name__ == "__main__":
    unittest.main()
