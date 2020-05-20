import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Card

from .data import Data


class CardTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CardTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__

        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")

        self.culqi = Culqi(self.public_key, self.private_key)
        self.card = Card(client=self.culqi)

        self.metadata = {"order_id": "0001"}

    def get_card_data(self, code, provider):
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.CARD[code][provider])
        token_data["email"] = email
        token = self.culqi.token.create(data=token_data)

        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = self.culqi.customer.create(data=customer_data)

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
        card_data = self.get_card_data("successful", "visa")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "card"

    @pytest.mark.vcr()
    def test_card_retrieve(self):
        card_data = self.get_card_data("successful", "visa")
        created_card = self.card.create(data=card_data)
        retrieved_card = self.card.read(created_card["data"]["id"])
        assert created_card["data"]["id"] == retrieved_card["data"]["id"]

    @pytest.mark.vcr()
    def test_card_list(self):
        retrieved_card_list = self.card.list()
        assert "items" in retrieved_card_list["data"]

    @pytest.mark.vcr()
    def test_card_update(self):
        card_data = self.get_card_data("successful", "visa")
        created_card = self.card.create(data=card_data)

        metadatada = {"metadata": self.metadata}
        updated_card = self.card.update(id_=created_card["data"]["id"], data=metadatada)

        assert created_card["data"]["id"] == created_card["data"]["id"]
        assert updated_card["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_card_delete(self):
        card_data = self.get_card_data("successful", "visa")
        created_card = self.card.create(data=card_data)
        deleted_card = self.card.delete(id_=created_card["data"]["id"])

        assert deleted_card["data"]["deleted"]
        assert deleted_card["data"]["id"] == created_card["data"]["id"]
        assert deleted_card["status"] == 200

    @pytest.mark.vcr()
    def test_card_create__successful__visa(self):
        card_data = self.get_card_data("successful", "visa")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "card"

    @pytest.mark.vcr()
    def test_card_create__successful__master_card(self):
        card_data = self.get_card_data("successful", "master_card")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "card"

    @pytest.mark.vcr()
    def test_card_create__successful__american_express(self):
        card_data = self.get_card_data("successful", "american_express")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "card"

    @pytest.mark.vcr()
    def test_card_create__successful__diners_club(self):
        card_data = self.get_card_data("successful", "diners_club")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "card"

    @pytest.mark.vcr()
    def test_card_create__stolen_card__visa(self):
        card_data = self.get_card_data("stolen_card", "visa")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "stolen_card"

    @pytest.mark.vcr()
    def test_card_create__lost_card__visa(self):
        card_data = self.get_card_data("lost_card", "visa")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "lost_card"

    @pytest.mark.vcr()
    def test_card_create__insufficient_funds__visa(self):
        card_data = self.get_card_data("insufficient_funds", "visa")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "insufficient_funds"

    @pytest.mark.vcr()
    def test_card_create__contact_issuer__master_card(self):
        card_data = self.get_card_data("contact_issuer", "master_card")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "contact_issuer"

    @pytest.mark.vcr()
    def test_card_create__incorrect_cvv__master_card(self):
        card_data = self.get_card_data("incorrect_cvv", "master_card")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "incorrect_cvv"

    @pytest.mark.vcr()
    def test_card_create__issuer_not_available__american_express(self):
        card_data = self.get_card_data("issuer_not_available", "american_express")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "issuer_not_available"

    @pytest.mark.vcr()
    def test_card_create__issuer_decline_operation__american_express(self):
        card_data = self.get_card_data("issuer_decline_operation", "american_express")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "issuer_decline_operation"

    @pytest.mark.vcr()
    def test_card_create__invalid_card__diners_club(self):
        card_data = self.get_card_data("invalid_card", "diners_club")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "invalid_card"

    @pytest.mark.vcr()
    def test_card_create__processing_error__diners_club(self):
        card_data = self.get_card_data("processing_error", "diners_club")
        card = self.card.create(data=card_data)
        assert card["data"]["object"] == "error"
        assert card["data"]["code"] == "card_declined"
        assert card["data"]["decline_code"] == "processing_error"

    # This fail due to Internal server error in Culqi
    # @pytest.mark.vcr()
    # def test_card_create__fraudulent__diners_club(self):
    #     card_data = self.get_card_data(# "fraudulent", "diners_club")
    #     card = self.card.create(data=card_data)
    #     assert card["data"]["object"] == "error"
    #     assert card["data"]["code"] == "card_declined"
    #     assert card["data"]["decline_code"] == "fraudulent"


if __name__ == "__main__":
    unittest.main()
