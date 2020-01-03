from ..utils.errors import ErrorMessage, NotAllowedError
from ..utils.urls import URL
from .base import Resource
from ..schemas import refund

__all__ = ["Refund"]


class Refund(Resource):
    schema = refund.SCHEMA
    endpoint = URL.REFUND

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
