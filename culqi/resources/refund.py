from culqi.utils.errors import CustomException, ErrorMessage, NotAllowedError
from culqi.utils.validation.refund_validation import RefundValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Refund"]


class Refund(Resource):
    endpoint = URL.REFUND

    def create(self, data, **options):
        try:
            RefundValidation.create(self, data)
            return Resource.create(self, data, **options)
        except CustomException as e:
            return e.error_data

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
    
    def list(self, data={}, **options):
        try:
            RefundValidation.list(self, data)
            url = self._get_url()
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def read(self, id_, data=None, **options):
        try:
            RefundValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def update(self, id_, data=None, **options):
        try:
            RefundValidation.update(self, id_)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e.error_data
