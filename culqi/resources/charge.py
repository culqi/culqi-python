from culqi.utils.validation.charge_validation import ChargeValidation
from culqi.utils.errors import ErrorMessage, NotAllowedError
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Charge"]


class Charge(Resource):
    endpoint = URL.CHARGE

    def create(self, data, **options):
        ChargeValidation.create(self, data)
        return Resource.create(self, data, **options)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def capture(self, id_, data=None, **options):
        ChargeValidation.capture(self, id_)
        url = self._get_url(id_, "capture")
        return self._post(url, data, **options)
    
    def list(self, data={}, **options):
        ChargeValidation.list(self, data)
        url = self._get_url()
        return self._get(url, data, **options)
    
    def read(self, id_, data=None, **options):
        ChargeValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._get(url, data, **options)
    
    def update(self, id_, data=None, **options):
        ChargeValidation.update(self, id_)
        url = self._get_url(id_)
        return self._patch(url, data, **options)
