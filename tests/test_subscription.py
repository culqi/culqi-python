import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Subscription
from culqi.utils.urls import URL

from .data import Data


class SubscriptionTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SubscriptionTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"
        self.culqi = Culqi(self.public_key, self.private_key)
        self.subscription = Subscription(client=self.culqi)

        self.metadata = {"order_id": "0001"}

    @property
    def subscription_data(self):
        # pylint: disable=no-member
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.TOKEN)
        token_data["email"] = email
        token = self.culqi.token.create(data=token_data)

        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = self.culqi.customer.create(data=customer_data)

        card_data = {
            "token_id": token["data"]["id"],
            "customer_id": customer["data"]["id"],
        }
        card = self.culqi.card.create(data=card_data)

        plan_data = deepcopy(Data.PLAN)
        plan_data["name"] = "plan-{0}".format(uuid4().hex[:4])
        plan = self.culqi.plan.create(data=plan_data)

        return {
            "card_id": card["data"]["id"],
            "plan_id": plan["data"]["id"],
            "tyc": True
        }
    
    @property
    def subscription_data_update(self):
        # pylint: disable=no-member
        email = "richard{0}@piedpiper.com".format(uuid4().hex[:4])

        token_data = deepcopy(Data.TOKEN)
        token_data["email"] = email
        token = self.culqi.token.create(data=token_data)

        customer_data = deepcopy(Data.CUSTOMER)
        customer_data["email"] = email
        customer = self.culqi.customer.create(data=customer_data)

        card_data = {
            "token_id": token["data"]["id"],
            "customer_id": customer["data"]["id"],
        }
        card = self.culqi.card.create(data=card_data)

        return {
            "card_id": card["data"]["id"],
            "metadata": self.metadata
        }

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.subscription._get_url() == f"{URL.BASE}/v2/recurrent/subscriptions"
        assert self.subscription._get_url(
            id_
        ) ==f"{URL.BASE}/v2/recurrent/subscriptions/{id_}"

    #python3 -m pytest -k test_subscription_create -p no:warnings
    @pytest.mark.vcr()
    def test_subscription_create(self):
        subscription = self.subscription.create(data=self.subscription_data)
        assert "id" in subscription["data"] and isinstance(subscription["data"]["id"], str)

    #python3 -m pytest -k test_subscription_create -p no:warnings
    @pytest.mark.vcr()
    def test_subscription_retrieve(self):
        created_subscription = self.subscription.create(data=self.subscription_data)
        retrieved_subscription = self.subscription.read(created_subscription["data"]["id"])
        assert (created_subscription["data"]["id"] == retrieved_subscription["data"]["id"])

    #python3 -m pytest -k test_subscription_list -p no:warnings
    @pytest.mark.vcr()
    def test_subscription_list(self):
         data_filter = {
            #"before": "1712692203",
            #"after": "1712692203",
            "limit": 1
            #"creation_date_from": "2023-12-30T00:00:00.000Z",
            #"creation_date_to": "2023-12-20T00:00:00.000Z",
        }
         retrieved_subscription_list = self.subscription.list(data=data_filter)
         assert "items" in retrieved_subscription_list["data"]

    #python3 -m pytest -k test_subscription_update -p no:warnings
    @pytest.mark.vcr()
    def test_subscription_update(self):
        created_subscription = self.subscription.create(data=self.subscription_data)
        data_update = self.subscription_data_update

        updated_subscription = self.subscription.update(
            id_=created_subscription["data"]["id"], data=data_update
        )
        assert updated_subscription["data"]["id"] == created_subscription["data"]["id"]

    #python3 -m pytest -k test_subscription_delete -p no:warnings
    @pytest.mark.vcr()
    def test_subscription_delete(self):
        created_subscription = self.subscription.create(data=self.subscription_data)
        deleted_subscription = self.subscription.delete(id_=created_subscription["data"]["id"])

        assert deleted_subscription["data"]["deleted"]
        assert deleted_subscription["data"]["id"] == created_subscription["data"]["id"]
        assert deleted_subscription["status"] == 200


if __name__ == "__main__":
    unittest.main()
