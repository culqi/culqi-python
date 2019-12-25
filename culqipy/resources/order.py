from .base import Resource

from ..utils.urls import URL


__all__ = [
    'Order'
]


class Order(Resource):
    endpoint = URL.ORDER

    def confirm(self, id_, data=None, **options):
        url = self._get_url(id_, 'confirm')
        return self._post(url, data, **options)
