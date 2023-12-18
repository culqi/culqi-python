from culqi.utils.validation.order_validation import OrderValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource


__all__ = ["Order"]


class Order(Resource):
    endpoint = URL.ORDER
    
    def create(self, data, **options):
        OrderValidation.create(self, data)
        return Resource.create(self, data, **options)

    def confirm(self, id_, data={}, **options):
        OrderValidation.confirm(self, id_)
        headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
        if "headers" in options:
            options["headers"].update(headers)
        else:
            options["headers"] = headers
        url = self._get_url(id_, "confirm")
        return self._post(url, data, **options)
    def confirmtype(self, data={}, **options):
        OrderValidation.confirm_type(self, data)
        headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
        if "headers" in options:
            options["headers"].update(headers)
        else:
            options["headers"] = headers
        url = self._get_url("confirm")
        return self._post(url, data, **options)
    
    def list(self, data={}, **options):
        OrderValidation.list(self, data)
        url = self._get_url()
        return self._get(url, data, **options)
    
    def read(self, id_, data=None, **options):
        OrderValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._get(url, data, **options)
    
    def update(self, id_, data=None, **options):
        OrderValidation.update(self, id_)
        url = self._get_url(id_)
        return self._patch(url, data, **options)
    
    def delete(self, id_, data=None, **options):
        OrderValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._delete(url, data, **options)