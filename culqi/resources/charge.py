from culqi.utils.culqi_validation import CulqiValidation
from culqi.utils.errors import ErrorMessage, NotAllowedError
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Charge"]


class Charge(Resource):
    endpoint = URL.CHARGE

    def create(self, data, **options):
        CulqiValidation.charge_validation(self, data)
        return Resource.create(self, data, **options)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def capture(self, id_, data=None, **options):
        url = self._get_url(id_, "capture")
        return self._post(url, data, **options)
