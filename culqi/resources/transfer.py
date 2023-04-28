from culqi.utils.errors import ErrorMessage, NotAllowedError
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Transfer"]


class Transfer(Resource):
    endpoint = URL.TRANSFER

    def create(self, data, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def update(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
