import os
import unittest

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import RESOURCE_PREFIX, Culqi


class ClientTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ClientTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)

    def test_version(self):
        # pylint: disable=protected-access
        assert self.culqi._get_version() == self.version

    def test_keys(self):
        assert self.public_key == self.culqi.public_key
        assert self.private_key == self.culqi.private_key

    def test_session_headers(self):
        session_headers = self.culqi.session.headers
        headers = {
            "User-Agent": "Culqi-API-Python/{0}".format(self.version),
            "Authorization": "Bearer {0}".format(self.private_key),
            "Content-type": "application/json",
            "Accept": "application/json",
        }

        assert headers["User-Agent"] == session_headers["User-Agent"]
        assert headers["Authorization"] == session_headers["Authorization"]
        assert headers["Content-type"] == session_headers["Content-type"]
        assert headers["Accept"] == session_headers["Accept"]

    def test_non_injected_property(self):
        attribute_name = "dummy_attribute"
        message = (
            "'Culqi' object has no attribute '%sdummy_attribute'" % RESOURCE_PREFIX
        )

        with pytest.raises(AttributeError) as excinfo:
            getattr(self.culqi, attribute_name)

        assert message in str(excinfo.value)


if __name__ == "__main__":
    unittest.main()
