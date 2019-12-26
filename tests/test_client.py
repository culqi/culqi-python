import os
import unittest

from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client


class ClientTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.api_key = os.environ.get('API_KEY', 'sample_api_key')
        self.api_secret = os.environ.get('API_SECRET', 'sample_api_secret')
        self.client = Client(self.api_key, self.api_secret)

    def test_version(self):
        # pylint: disable=protected-access
        assert self.client._get_version() == self.version

    def test_keys(self):
        assert self.api_key == self.client.api_key
        assert self.api_secret == self.client.api_secret

    def test_session_headers(self):
        session_headers = self.client.session.headers
        headers = {
            'User-Agent': f'Culqi-API-Python/{self.version}',
            'Authorization': f'Bearer {self.api_secret}',
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

        assert headers['User-Agent'] == session_headers['User-Agent']
        assert headers['Authorization'] == session_headers['Authorization']
        assert headers['Content-type'] == session_headers['Content-type']
        assert headers['Accept'] == session_headers['Accept']


if __name__ == '__main__':
    unittest.main()
