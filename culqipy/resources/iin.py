from ..utils.errors import ErrorMessage, NotAllowedError
from ..utils.urls import URL
from .base import Resource

__all__ = ["Iin"]


class Iin(Resource):
    endpoint = URL.IIN

    def create(self, data, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def update(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
