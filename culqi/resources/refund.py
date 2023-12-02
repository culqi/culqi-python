from culqi.utils.errors import ErrorMessage, NotAllowedError
from culqi.utils.culqi_validation import CulqiValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Refund"]


class Refund(Resource):
    endpoint = URL.REFUND

    def create(self, data, **options):
        CulqiValidation.refund_validation(self, data)
        return Resource.create(self, data, **options)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
