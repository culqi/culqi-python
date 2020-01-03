import os
import unittest

from dotenv import load_dotenv

<<<<<<< HEAD
from culqi import __version__
from culqi.client import Culqi
=======
from culqi import __version__ 
from culqi.client import Culqi 
>>>>>>> 47d2ef3b617be67c0725ae1808bf9fb7441f19e5


class ClientTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ClientTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
<<<<<<< HEAD
        self.culqi = Culqi(self.public_key, self.private_key)
=======
        self.culqi = Culqi(self.public_key, self.private_key) 
>>>>>>> 47d2ef3b617be67c0725ae1808bf9fb7441f19e5

    def test_version(self):
        # pylint: disable=protected-access
        assert self.culqi._get_version() == self.version

    def test_keys(self):
        assert self.public_key == self.culqi.public_key
<<<<<<< HEAD
        assert self.private_key == self.culqi.private_key
=======
        assert self.private_key == self.culqi.private_key 
>>>>>>> 47d2ef3b617be67c0725ae1808bf9fb7441f19e5

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


if __name__ == "__main__":
    unittest.main()
