from .base import Resource

from ..utils.errors import NotAllowedError, ErrorMessage
from ..utils.urls import URL


__all__ = [
    "Event"
]


class Event(Resource):
    endpoint = URL.EVENT

    def create(self, data, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def update(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
