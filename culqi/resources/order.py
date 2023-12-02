from culqi.utils.culqi_validation import CulqiValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource


__all__ = ["Order"]


class Order(Resource):
    endpoint = URL.ORDER
    
    def create(self, data, **options):
        CulqiValidation.order_validation(self, data)
        return Resource.create(self, data, **options)

    def confirm(self, id_, data=None, **options):
        url = self._get_url(id_, "confirm")
        return self._post(url, data, **options)
    def confirmtipo(self, data=None, **options):
        CulqiValidation.order_validation(self, data)
        url = self._get_url("confirm")
        return self._post(url, data, **options)