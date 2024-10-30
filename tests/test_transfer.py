import os
import unittest

# import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Transfer
from culqi.utils.urls import URL


class TransferTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TransferTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"
        self.culqi = Culqi(self.public_key, self.private_key)
        self.transfer = Transfer(client=self.culqi)

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.transfer._get_url() ==f"{URL.BASE}/v2/transfers"
        assert self.transfer._get_url(
            id_
        ) ==f"{URL.BASE}/v2/transfers/{id_}"

    # @pytest.mark.vcr()
    # def test_transfer_retrieve(self):
    #     retrieved_transfer = self.transfer.read(created_transfer["data"]["id"])
    #     assert created_transfer["data"]["id"] == retrieved_transfer["data"]["id"]

    # Failing test: Request time out
    # @pytest.mark.vcr()
    # def test_transfer_list(self):
    #     retrieved_transfer_list = self.transfer.list()
    #     assert "items" in retrieved_transfer_list["data"]


if __name__ == "__main__":
    unittest.main()
