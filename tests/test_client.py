import os
import unittest

from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi


class ClientTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ClientTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = "pk_test_90667d0a57d45c48"
        self.private_key = "sk_test_1573b0e8079863ff"
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
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        assert headers["User-Agent"] == session_headers["User-Agent"]
        assert headers["Authorization"] == session_headers["Authorization"]
        assert headers["Content-Type"] == session_headers["Content-Type"]
        assert headers["Accept"] == session_headers["Accept"]


if __name__ == "__main__":
    unittest.main()
