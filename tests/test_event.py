import os
import unittest

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Event
from culqi.utils.errors import ErrorMessage, NotAllowedError


class EventTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EventTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.event = Event(client=self.culqi)

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

    @pytest.mark.vcr()
    def test_event_create(self):
        with pytest.raises(NotAllowedError) as excinfo:
            event_data = {}
            self.event.create(data=event_data)

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)

    @pytest.mark.vcr()
    def test_event_update(self):
        with pytest.raises(NotAllowedError) as excinfo:
            event_data = {}
            self.event.update("sample_id", data=event_data)

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)

    @pytest.mark.vcr()
    def test_event_delete(self):
        with pytest.raises(NotAllowedError) as excinfo:
            self.event.delete("sample_id")

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)


if __name__ == "__main__":
    unittest.main()
