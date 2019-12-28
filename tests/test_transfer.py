import os
import unittest

# import pytest
from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Transfer


class TransferTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TransferTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.client = Client(self.api_key, self.api_secret)
        self.transfer = Transfer(client=self.client)

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.transfer._get_url() == "https://api.culqi.com/v2/transfers"
        assert self.transfer._get_url(
            id_) == "https://api.culqi.com/v2/transfers/{0}".format(id_)

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
