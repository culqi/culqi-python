import os
import unittest

import pytest
from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Iin


class IinTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IinTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.client = Client(self.api_key, self.api_secret)
        self.iin = Iin(client=self.client)

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.iin._get_url() == "https://api.culqi.com/v2/iins"
        assert self.iin._get_url(
            id_) == "https://api.culqi.com/v2/iins/{0}".format(id_)

    # @pytest.mark.vcr()
    # def test_iin_retrieve(self):
    #     retrieved_iin = self.iin.read(created_iin["data"]["id"])
    #     assert created_iin["data"]["id"] == retrieved_iin["data"]["id"]

    @pytest.mark.vcr()
    def test_iin_list(self):
        retrieved_iin_list = self.iin.list()
        assert "items" in retrieved_iin_list["data"]


if __name__ == "__main__":
    unittest.main()
