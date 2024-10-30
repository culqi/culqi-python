import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Plan
from culqi.utils.urls import URL

from .data import Data


class PlanTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PlanTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"
        self.culqi = Culqi(self.public_key, self.private_key)
        self.plan = Plan(client=self.culqi)

        self.metadata = {"order_id": "0001"}

    @property
    def plan_data(self):
        plan_data = deepcopy(Data.PLAN)
        plan_data["name"] = "plan-{0}".format(uuid4().hex[:4])

        return plan_data

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.plan._get_url() == f"{URL.BASE}/v2/recurrent/plans"
        assert self.plan._get_url(id_) == f"{URL.BASE}/v2/recurrent/plans/{id_}"

    #python3 -m pytest -k test_plan_create -p no:warnings
    @pytest.mark.vcr()
    def test_plan_create(self):
        plan = self.plan.create(data=self.plan_data)
        assert "id" in plan["data"] and isinstance(plan["data"]["id"], str)

    #python3 -m pytest -k test_plan_retrieve -p no:warnings
    @pytest.mark.vcr()
    def test_plan_retrieve(self):
        created_plan = self.plan.create(data=self.plan_data)
        retrieved_plan = self.plan.read(created_plan["data"]["id"])
        assert created_plan["data"]["id"] == retrieved_plan["data"]["id"]

    #python3 -m pytest -k test_plan_list -p no:warnings
    @pytest.mark.vcr()
    def test_plan_list(self):
        data_filter = {
            #"before": "pln_live_**********",
            #"after": "pln_live_**********",
            "limit": 1,
            #"min_amount": 300,
            #"max_amount": 500000,
            #"status": 1,
            #"creation_date_from": "1712692203",
            #"creation_date_to": "1712692203",
        }
        retrieved_plan_list = self.plan.list(data=data_filter)
        assert "items" in retrieved_plan_list["data"]

    #python3 -m pytest -k test_plan_update -p no:warnings
    @pytest.mark.vcr()
    def test_plan_update(self):
        created_plan = self.plan.create(data=self.plan_data)

        data_update = {
            "metadata": self.metadata,
            "status": 1,
            "name": "plan-{0}".format(uuid4().hex[:4]),
            "short_name": "short_plan-{0}".format(uuid4().hex[:4]),
            "description": "description",
        }

        updated_plan = self.plan.update(id_=created_plan["data"]["id"], data=data_update)
        assert created_plan["data"]["id"] == created_plan["data"]["id"]
        assert updated_plan["data"]["metadata"] == self.metadata

    #python3 -m pytest -k test_plan_delete -p no:warnings
    @pytest.mark.vcr()
    def test_plan_delete(self):
        created_plan = self.plan.create(data=self.plan_data)
        deleted_plan = self.plan.delete(id_=created_plan["data"]["id"])
        assert deleted_plan["data"]["deleted"]
        assert deleted_plan["data"]["id"] == created_plan["data"]["id"]
        assert deleted_plan["status"] == 200


if __name__ == "__main__":
    unittest.main()
