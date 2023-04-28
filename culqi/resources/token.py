from ..utils.errors import ErrorMessage, NotAllowedError
from ..utils.urls import URL
from .base import Resource

__all__ = ["Token"]


class Token(Resource):
    endpoint = URL.TOKEN

    def create(self, data, **options):
        headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
        if "headers" in options:
            options["headers"].update(headers)
        else:
            options["headers"] = headers
        url = self._get_url_secure()
        return self._post(url, data, **options)

    def createyape(self, data, **options):
        headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
        if "headers" in options:
            options["headers"].update(headers)
        else:
            options["headers"] = headers
        url = self._get_url_secure("yape")
        return self._post(url, data, **options)
    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
