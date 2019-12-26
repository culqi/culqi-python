import os
import unittest
from copy import deepcopy

import pytest
from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Token, Charge, Refund

from .utils import Data


class RefundTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.client = Client(self.api_key, self.api_secret)
        self.token = Token(client=self.client)
        self.charge = Charge(client=self.client)
        self.refund = Refund(client=self.client)

        self.token_data = deepcopy(Data.TOKEN)
        self.charge_data = deepcopy(Data.CHARGE)
        self.refund_data = deepcopy(Data.REFUND)
        self.metadata = {
            "order_id":"0001"
        }

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.refund._get_url() == "https://api.culqi.com/v2/refunds"
        assert self.refund._get_url(id_) == "https://api.culqi.com/v2/refunds/{0}".format(id_)

    @pytest.mark.vcr()
    def test_refund_create(self):
        token = self.token.create(data=self.token_data)

        self.charge_data["source_id"] = token["data"]["id"]
        charge = self.charge.create(data=self.charge_data)

        self.refund_data["charge_id"] = charge["data"]["id"]
        refund = self.refund.create(data=self.refund_data)
        assert refund["data"]["object"] == "refund"

    @pytest.mark.vcr()
    def test_refund_retrieve(self):
        token = self.token.create(data=self.token_data)

        self.charge_data["source_id"] = token["data"]["id"]
        charge = self.charge.create(data=self.charge_data)

        self.refund_data["charge_id"] = charge["data"]["id"]
        created_refund = self.refund.create(data=self.refund_data)
        retrieved_refund = self.refund.read(created_refund["data"]["id"])

        assert created_refund["data"]["id"] == retrieved_refund["data"]["id"]

    @pytest.mark.vcr()
    def test_refund_list(self):
        retrieved_refundharge_list = self.charge.list()
        assert "items" in retrieved_refundharge_list["data"]

    @pytest.mark.vcr()
    def test_refund_update(self):
        token = self.token.create(data=self.token_data)

        self.charge_data["source_id"] = token["data"]["id"]
        charge = self.charge.create(data=self.charge_data)

        self.refund_data["charge_id"] = charge["data"]["id"]
        created_refund = self.refund.create(data=self.refund_data)

        metadatada = {
            "metadata": self.metadata
        }
        updated_refund = self.refund.update(id_=created_refund["data"]["id"], data=metadatada)

        assert updated_refund["data"]["id"] == created_refund["data"]["id"]
        assert updated_refund["data"]["metadata"] == self.metadata


if __name__ == "__main__":
    unittest.main()
