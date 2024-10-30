import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Order
from culqi.utils.urls import URL

from .data import Data


class OrderTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(OrderTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"
        self.culqi = Culqi(self.public_key, self.private_key)
        self.order = Order(client=self.culqi)

        self.metadata = {"order_id": "0001"}

        #ecnrypt variables
        self.rsa_public_key = "-----BEGIN PUBLIC KEY-----\n"+\
        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYp0451xITpczkBrl5Goxkh7m1\n"+\
        "oynj8eDHypIn7HmbyoNJd8cS4OsT850hIDBwYmFuwmxF1YAJS8Cd2nes7fjCHh+7\n"+\
        "oNqgNKxM2P2NLaeo4Uz6n9Lu4KKSxTiIT7BHiSryC0+Dic91XLH7ZTzrfryxigsc\n"+\
        "+ZNndv0fQLOW2i6OhwIDAQAB\n"+\
        "-----END PUBLIC KEY-----\n"
        self.rsa_id = "508fc232-0a9d-4fc0-a192-364a0b782b89"

    @property
    def order_data(self):
        order_data = deepcopy(Data.ORDER)
        order_data["order_number"] = "order-{0}".format(uuid4().hex[:4])

        return order_data

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.order._get_url() == f"{URL.BASE}/v2/orders"
        assert self.order._get_url(id_) == f"{URL.BASE}/v2/orders/{id_}"
        assert self.order._get_url(
            id_, "confirm"
        ) ==f"{URL.BASE}/v2/orders/{id_}/confirm"

    @pytest.mark.vcr()
    def test_order_create(self):
        order = self.order.create(data=self.order_data)

        assert order["data"]["object"] == "order"
    
    @pytest.mark.vcr()
    def test_order_create_encrypt(self):
        options = {}
        options["rsa_public_key"] = self.rsa_public_key
        options["rsa_id"] = self.rsa_id

        order = self.order.create(data=self.order_data, **options)

        assert order["data"]["object"] == "order"

    @pytest.mark.vcr()
    def test_order_confirm(self):
        created_order = self.order.create(data=self.order_data)
        confirmed_order = self.order.confirm(created_order["data"]["id"])

        assert confirmed_order["data"]["id"] == created_order["data"]["id"]
        assert confirmed_order["status"] == 201

    @pytest.mark.vcr()
    def test_order_retrieve(self):
        created_order = self.order.create(data=self.order_data)
        retrieved_order = self.order.read(created_order["data"]["id"])

        assert created_order["data"]["id"] == retrieved_order["data"]["id"]

    @pytest.mark.vcr()
    def test_order_list(self):
        retrieved_order_list = self.order.list()
        assert "items" in retrieved_order_list["data"]

    @pytest.mark.vcr()
    def test_order_update(self):
        created_order = self.order.create(data=self.order_data)

        metadatada = {"metadata": self.metadata}
        updated_order = self.order.update(
            id_=created_order["data"]["id"], data=metadatada
        )

        assert updated_order["data"]["id"] == created_order["data"]["id"]
        assert updated_order["data"]["metadata"] == self.metadata

    # Failing test: can't delete orders
    # @pytest.mark.vcr()
    # def test_order_delete(self):
    #     created_order = self.order.create(data=self.order_data)
    #     confirmed_order = self.order.confirm(id_=created_order['data']['id'])
    #     deleted_order = self.order.delete(id_=confirmed_order["data"]["id"])
    #     assert deleted_order["data"]["deleted"]
    #     assert deleted_order["data"]["id"] == created_order["data"]["id"]
    #     assert deleted_order["status"] == 200


if __name__ == "__main__":
    unittest.main()
