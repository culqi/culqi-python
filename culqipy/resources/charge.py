from .base import Resource

from ..utils.errors import NotAllowedError, ErrorMessage
from ..utils.urls import URL


__all__ = [
    'Charge'
]


class Charge(Resource):
    endpoint = URL.CHARGE

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def capture(self, id_, data=None, **options):
        url = self._get_url(id_, 'capture')
        return self._post(url, data, **options)
