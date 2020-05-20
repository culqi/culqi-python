import os
import unittest
from copy import deepcopy

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Refund
from culqi.utils.errors import ErrorMessage, NotAllowedError

from .data import Data


class RefundTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RefundTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.refund = Refund(client=self.culqi)

        self.metadata = {"order_id": "0001"}

    def get_refund_data(self, kind, provider):
        # pylint-x: disable=no-member
        token_data = deepcopy(Data.CARD[kind][provider])
        token = self.culqi.token.create(data=token_data)

        charge_data = deepcopy(Data.CHARGE)
        charge_data["source_id"] = token["data"]["id"]
        charge = self.culqi.charge.create(data=charge_data)

        refund_data = deepcopy(Data.REFUND)
        refund_data["charge_id"] = charge["data"]["id"]
        return refund_data

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.refund._get_url() == "https://api.culqi.com/v2/refunds"
        assert self.refund._get_url(
            id_
        ) == "https://api.culqi.com/v2/refunds/{0}".format(id_)

    @pytest.mark.vcr()
    def test_refund_create(self):
        refund_data = self.get_refund_data("successful", "visa")
        refund = self.refund.create(data=refund_data)
        assert refund["data"]["object"] == "refund"

    @pytest.mark.vcr()
    def test_refund_retrieve(self):
        refund_data = self.get_refund_data("successful", "visa")
        created_refund = self.refund.create(data=refund_data)
        retrieved_refund = self.refund.read(created_refund["data"]["id"])

        assert created_refund["data"]["id"] == retrieved_refund["data"]["id"]

    @pytest.mark.vcr()
    def test_refund_list(self):
        retrieved_refund_list = self.refund.list()
        assert "items" in retrieved_refund_list["data"]

    @pytest.mark.vcr()
    def test_refund_update(self):
        refund_data = self.get_refund_data("successful", "visa")
        created_refund = self.refund.create(data=refund_data)

        metadatada = {"metadata": self.metadata}
        updated_refund = self.refund.update(
            id_=created_refund["data"]["id"], data=metadatada
        )

        assert updated_refund["data"]["id"] == created_refund["data"]["id"]
        assert updated_refund["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_refund_delete(self):
        with pytest.raises(NotAllowedError) as excinfo:
            refund_data = self.get_refund_data("successful", "visa")
            refund = self.refund.create(data=refund_data)
            self.refund.delete(refund["data"]["id"])

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)


if __name__ == "__main__":
    unittest.main()
