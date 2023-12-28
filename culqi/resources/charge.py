from culqi.utils.validation.charge_validation import ChargeValidation
from culqi.utils.errors import CustomException, ErrorMessage, NotAllowedError
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Charge"]


class Charge(Resource):
    endpoint = URL.CHARGE

    def create(self, data, **options):
        try:
            ChargeValidation.create(self, data)
            return Resource.create(self, data, **options)
        except CustomException as e:
            return e

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def capture(self, id_, data=None, **options):
        try:
            ChargeValidation.capture(self, id_)
            url = self._get_url(id_, "capture")
            return self._post(url, data, **options)
        except CustomException as e:
            return e
    
    def list(self, data={}, **options):
        try:
            ChargeValidation.list(self, data)
            url = self._get_url()
            return self._get(url, data, **options)
        except CustomException as e:
            return e
    
    def read(self, id_, data=None, **options):
        try:
            ChargeValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e
    
    def update(self, id_, data=None, **options):
        try:
            ChargeValidation.update(self, id_)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e
