from culqi.utils.errors import ErrorMessage, NotAllowedError
from culqi.utils.validation.refund_validation import RefundValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Refund"]


class Refund(Resource):
    endpoint = URL.REFUND

    def create(self, data, **options):
        RefundValidation.create(self, data)
        return Resource.create(self, data, **options)

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
    
    def list(self, data={}, **options):
        RefundValidation.list(self, data)
        url = self._get_url()
        return self._get(url, data, **options)
    
    def read(self, id_, data=None, **options):
        RefundValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._get(url, data, **options)
    
    def update(self, id_, data=None, **options):
        RefundValidation.update(self, id_)
        url = self._get_url(id_)
        return self._patch(url, data, **options)
