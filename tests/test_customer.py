import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Customer

from .data import Data


class CustomerTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CustomerTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.customer = Customer(client=self.culqi)

        self.customer_data = deepcopy(Data.CUSTOMER)
        self.customer_data["email"] = "richard{0}@piedpiper.com".format(uuid4().hex[:4])
        self.metadata = {"order_id": "0001"}

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.customer._get_url() == "https://api.culqi.com/v2/customers"
        assert self.customer._get_url(
            id_
        ) == "https://api.culqi.com/v2/customers/{0}".format(id_)

    @pytest.mark.vcr()
    def test_customer_create(self):
        customer = self.customer.create(data=self.customer_data)
        assert customer["data"]["object"] == "customer"

    @pytest.mark.vcr()
    def test_customer_retrieve(self):
        created_customer = self.customer.create(data=self.customer_data)
        retrieved_customer = self.customer.read(created_customer["data"]["id"])
        assert created_customer["data"]["id"] == retrieved_customer["data"]["id"]

    @pytest.mark.vcr()
    def test_customer_list(self):
        retrieved_customer_list = self.customer.list()
        assert "items" in retrieved_customer_list["data"]

    @pytest.mark.vcr()
    def test_customer_update(self):
        created_customer = self.customer.create(data=self.customer_data)

        metadatada = {"metadata": self.metadata}
        updated_customer = self.customer.update(
            id_=created_customer["data"]["id"], data=metadatada
        )

        assert created_customer["data"]["id"] == created_customer["data"]["id"]
        assert updated_customer["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_customer_delete(self):
        created_customer = self.customer.create(data=self.customer_data)
        deleted_customer = self.customer.delete(id_=created_customer["data"]["id"])

        assert deleted_customer["data"]["deleted"]
        assert deleted_customer["data"]["id"] == created_customer["data"]["id"]
        assert deleted_customer["status"] == 200


if __name__ == "__main__":
    unittest.main()
