from ..utils.errors import ErrorMessage, NotAllowedError
from ..utils.urls import URL
from .base import Resource

__all__ = ["Token"]


class Token(Resource):
    endpoint = URL.TOKEN

    def create(self, data, **options):
        url = "https://secure.culqi.com/v2/tokens"
        
        headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
        if "headers" in options:
            options["headers"].update(headers)
        else:
            options["headers"] = headers

        return self._post(url, data, **options)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
