import os
import unittest

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Client
from culqi.resources import Event


class EventTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EventTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.client = Client(self.public_key, self.private_key)
        self.event = Event(client=self.client)

    def test_url(self):
        # pylint: disable=protected-access
        id_ = "sample_id"

        assert self.event._get_url() == "https://api.culqi.com/v2/events"
        assert self.event._get_url(id_) == "https://api.culqi.com/v2/events/{0}".format(
            id_
        )

    # @pytest.mark.vcr()
    # def test_event_retrieve(self):
    #     retrieved_event = self.event.read(created_event["data"]["id"])
    #     assert created_event["data"]["id"] == retrieved_event["data"]["id"]

    @pytest.mark.vcr()
    def test_event_list(self):
        retrieved_event_list = self.event.list()
        assert "items" in retrieved_event_list["data"]


if __name__ == "__main__":
    unittest.main()
