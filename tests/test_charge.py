import os
import unittest
from copy import deepcopy

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Charge
from culqi.utils.errors import ErrorMessage, NotAllowedError

from .data import Data


class ChargeTest(unittest.TestCase):
    # pylint: disable = too-many-public-methods
    def __init__(self, *args, **kwargs):
        super(ChargeTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.charge = Charge(client=self.culqi)
        self.metadata = {"order_id": "0001"}

    def get_charge_data(self, code, provider):
        token_data = deepcopy(Data.CARD[code][provider])
        token = self.culqi.token.create(data=token_data)

        charge_data = deepcopy(Data.CHARGE)
        charge_data["source_id"] = token["data"]["id"]

        return charge_data

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.charge._get_url() == "https://api.culqi.com/v2/charges"
        assert self.charge._get_url(
            id_
        ) == "https://api.culqi.com/v2/charges/{0}".format(id_)
        assert self.charge._get_url(
            id_, "capture"
        ) == "https://api.culqi.com/v2/charges/{0}/capture".format(id_)

    @pytest.mark.vcr()
    def test_charge_create(self):
        charge_data = self.get_charge_data("successful", "visa")
        charge = self.charge.create(data=charge_data)

        assert charge["data"]["object"] == "charge"

    @pytest.mark.vcr()
    def test_charge_capture(self):
        charge_data = self.get_charge_data("successful", "visa")
        created_charge = self.charge.create(data=charge_data)
        captured_charge = self.charge.capture(id_=created_charge["data"]["id"])

        assert captured_charge["data"]["id"] == created_charge["data"]["id"]

    @pytest.mark.vcr()
    def test_charge_retrieve(self):
        charge_data = self.get_charge_data("successful", "visa")
        created_charge = self.charge.create(data=charge_data)
        retrieved_charge = self.charge.read(created_charge["data"]["id"])

        assert created_charge["data"]["id"] == retrieved_charge["data"]["id"]

    @pytest.mark.vcr()
    def test_charge_list(self):
        retrieved_charge_list = self.charge.list()
        assert "items" in retrieved_charge_list["data"]

    @pytest.mark.vcr()
    def test_charge_update(self):
        charge_data = self.get_charge_data("successful", "visa")
        created_charge = self.charge.create(data=charge_data)

        metadatada = {"metadata": self.metadata}
        updated_charge = self.charge.update(
            id_=created_charge["data"]["id"], data=metadatada
        )

        assert updated_charge["data"]["id"] == created_charge["data"]["id"]
        assert updated_charge["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_charge_delete(self):
        with pytest.raises(NotAllowedError) as excinfo:
            charge_data = self.get_charge_data("successful", "visa")
            charge = self.charge.create(data=charge_data)
            self.charge.delete(charge["data"]["id"])

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)

    @pytest.mark.vcr()
    def test_charge_create__successful__visa(self):
        charge_data = self.get_charge_data("successful", "visa")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "charge"

    @pytest.mark.vcr()
    def test_charge_create__successful__master_card(self):
        charge_data = self.get_charge_data("successful", "master_card")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "charge"

    @pytest.mark.vcr()
    def test_charge_create__successful__american_express(self):
        charge_data = self.get_charge_data("successful", "american_express")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "charge"

    @pytest.mark.vcr()
    def test_charge_create__successful__diners_club(self):
        charge_data = self.get_charge_data("successful", "diners_club")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "charge"

    @pytest.mark.vcr()
    def test_charge_create__stolen_card__visa(self):
        charge_data = self.get_charge_data("stolen_card", "visa")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "stolen_card"

    @pytest.mark.vcr()
    def test_charge_create__lost_card__visa(self):
        charge_data = self.get_charge_data("lost_card", "visa")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "lost_card"

    @pytest.mark.vcr()
    def test_charge_create__insufficient_funds__visa(self):
        charge_data = self.get_charge_data("insufficient_funds", "visa")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "insufficient_funds"

    @pytest.mark.vcr()
    def test_charge_create__contact_issuer__master_card(self):
        charge_data = self.get_charge_data("contact_issuer", "master_card")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "contact_issuer"

    @pytest.mark.vcr()
    def test_charge_create__incorrect_cvv__master_card(self):
        charge_data = self.get_charge_data("incorrect_cvv", "master_card")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "incorrect_cvv"

    @pytest.mark.vcr()
    def test_charge_create__issuer_not_available__american_express(self):
        charge_data = self.get_charge_data("issuer_not_available", "american_express")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "issuer_not_available"

    @pytest.mark.vcr()
    def test_charge_create__issuer_decline_operation__american_express(self):
        charge_data = self.get_charge_data(
            "issuer_decline_operation", "american_express"
        )
        charge = self.charge.create(data=charge_data)

        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "issuer_decline_operation"

    @pytest.mark.vcr()
    def test_charge_create__invalid_card__diners_club(self):
        charge_data = self.get_charge_data("invalid_card", "diners_club")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "invalid_card"

    @pytest.mark.vcr()
    def test_charge_create__processing_error__diners_club(self):
        charge_data = self.get_charge_data("processing_error", "diners_club")
        charge = self.charge.create(data=charge_data)
        assert charge["data"]["object"] == "error"
        assert charge["data"]["code"] == "card_declined"
        assert charge["data"]["decline_code"] == "processing_error"

    # This fail due to Internal server error in Culqi
    # @pytest.mark.vcr()
    # def test_charge_create__fraudulent__diners_club(self):
    #     charge_data = self.get_charge_data(# "fraudulent", "diners_club")
    #     charge = self.charge.create(data=charge_data)
    #     assert charge["data"]["object"] == "error"
    #     assert charge["data"]["code"] == "card_declined"
    #     assert charge["data"]["decline_code"] == "fraudulent"


if __name__ == "__main__":
    unittest.main()
