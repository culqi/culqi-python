import os
import unittest
from copy import deepcopy
from uuid import uuid4

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Client
from culqi.resources import Plan

from .data import Data


class PlanTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PlanTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.client = Client(self.public_key, self.private_key)
        self.plan = Plan(client=self.client)

        self.metadata = {"order_id": "0001"}

    @property
    def plan_data(self):
        plan_data = deepcopy(Data.PLAN)
        plan_data["name"] = "plan-{0}".format(uuid4().hex[:4])

        return plan_data

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.plan._get_url() == "https://api.culqi.com/v2/plans"
        assert self.plan._get_url(id_) == "https://api.culqi.com/v2/plans/{0}".format(
            id_
        )

    @pytest.mark.vcr()
    def test_plan_create(self):
        plan = self.plan.create(data=self.plan_data)
        assert plan["data"]["object"] == "plan"

    @pytest.mark.vcr()
    def test_plan_retrieve(self):
        created_plan = self.plan.create(data=self.plan_data)
        retrieved_plan = self.plan.read(created_plan["data"]["id"])
        assert created_plan["data"]["id"] == retrieved_plan["data"]["id"]

    @pytest.mark.vcr()
    def test_plan_list(self):
        retrieved_plan_list = self.plan.list()
        assert "items" in retrieved_plan_list["data"]

    @pytest.mark.vcr()
    def test_plan_update(self):
        created_plan = self.plan.create(data=self.plan_data)

        metadatada = {"metadata": self.metadata}
        updated_plan = self.plan.update(id_=created_plan["data"]["id"], data=metadatada)

        assert created_plan["data"]["id"] == created_plan["data"]["id"]
        assert updated_plan["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_plan_delete(self):
        created_plan = self.plan.create(data=self.plan_data)
        deleted_plan = self.plan.delete(id_=created_plan["data"]["id"])

        assert deleted_plan["data"]["deleted"]
        assert deleted_plan["data"]["id"] == created_plan["data"]["id"]
        assert deleted_plan["status"] == 200


if __name__ == "__main__":
    unittest.main()
