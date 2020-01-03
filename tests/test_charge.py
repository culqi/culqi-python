import os
import unittest
from copy import deepcopy

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Charge

from .data import Data


class ChargeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ChargeTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.charge = Charge(client=self.culqi)

        self.metadata = {"order_id": "0001"}

    @property
    def charge_data(self):
        # pylint: disable=no-member
        token_data = deepcopy(Data.TOKEN)
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
        charge = self.charge.create(data=self.charge_data)

        assert charge["data"]["object"] == "charge"

    @pytest.mark.vcr()
    def test_charge_capture(self):
        created_charge = self.charge.create(data=self.charge_data)
        captured_charge = self.charge.capture(id_=created_charge["data"]["id"])

        assert captured_charge["data"]["id"] == created_charge["data"]["id"]
        assert captured_charge["status"] == 201

    @pytest.mark.vcr()
    def test_charge_retrieve(self):
        created_charge = self.charge.create(data=self.charge_data)
        retrieved_charge = self.charge.read(created_charge["data"]["id"])

        assert created_charge["data"]["id"] == retrieved_charge["data"]["id"]

    @pytest.mark.vcr()
    def test_charge_list(self):
        retrieved_charge_list = self.charge.list()
        assert "items" in retrieved_charge_list["data"]

    @pytest.mark.vcr()
    def test_charge_update(self):
        created_charge = self.charge.create(data=self.charge_data)

        metadatada = {"metadata": self.metadata}
        updated_charge = self.charge.update(
            id_=created_charge["data"]["id"], data=metadatada
        )

        assert updated_charge["data"]["id"] == created_charge["data"]["id"]
        assert updated_charge["data"]["metadata"] == self.metadata


if __name__ == "__main__":
    unittest.main()
