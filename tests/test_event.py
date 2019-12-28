import os
import unittest

from dotenv import load_dotenv

from culqipy import __version__
from culqipy.client import Client
from culqipy.resources import Event


class EventTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EventTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__


if __name__ == "__main__":
    unittest.main()
