import os
import unittest

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Iin
from culqi.utils.errors import ErrorMessage, NotAllowedError


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

    @pytest.mark.vcr()
    def test_iin_create(self):
        with pytest.raises(NotAllowedError) as excinfo:
            iin_data = {}
            self.iin.create(data=iin_data)

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)

    @pytest.mark.vcr()
    def test_iin_update(self):
        with pytest.raises(NotAllowedError) as excinfo:
            iin_data = {}
            self.iin.update("sample_id", data=iin_data)

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)

    @pytest.mark.vcr()
    def test_iin_delete(self):
        with pytest.raises(NotAllowedError) as excinfo:
            self.iin.delete("sample_id")

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)


if __name__ == "__main__":
    unittest.main()
