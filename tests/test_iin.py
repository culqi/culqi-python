import os
import unittest

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Iin


class IinTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IinTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.iin = Iin(client=self.culqi)

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.iin._get_url() == "https://api.culqi.com/v2/iins"
        assert self.iin._get_url(id_) == "https://api.culqi.com/v2/iins/{0}".format(id_)

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
