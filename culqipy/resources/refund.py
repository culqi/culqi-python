from .base import Resource

from ..utils.errors import NotAllowedError, ErrorMessage
from ..utils.urls import URL


__all__ = [
    'Refund'
]


class Refund(Resource):
    endpoint = URL.REFUND

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
