from ..utils.errors import ErrorMessage, NotAllowedError
from ..utils.urls import URL
from .base import Resource

__all__ = ["Transfer"]


class Transfer(Resource):
    endpoint = URL.TRANSFER

    def create(self, data, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def update(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
