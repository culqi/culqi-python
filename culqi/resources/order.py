from culqi.utils.errors import CustomException
from culqi.utils.validation.order_validation import OrderValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource


__all__ = ["Order"]


class Order(Resource):
    endpoint = URL.ORDER
    
    def create(self, data, **options):
        try:
            OrderValidation.create(self, data)
            return Resource.create(self, data, **options)
        except CustomException as e:
            return e.error_data

    def confirm(self, id_, data={}, **options):
        try:
            OrderValidation.confirm(self, id_)
            headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
            if "headers" in options:
                options["headers"].update(headers)
            else:
                options["headers"] = headers
            url = self._get_url(id_, "confirm")
            return self._post(url, data, **options)
        except CustomException as e:
            return e.error_data
    def confirmtype(self, data={}, **options):
        try:
            OrderValidation.confirm_type(self, data)
            headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
            if "headers" in options:
                options["headers"].update(headers)
            else:
                options["headers"] = headers
            url = self._get_url("confirm")
            return self._post(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def list(self, data={}, **options):
        try:
            OrderValidation.list(self, data)
            url = self._get_url()
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def read(self, id_, data=None, **options):
        try:
            OrderValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def update(self, id_, data=None, **options):
        try:
            OrderValidation.update(self, id_)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def delete(self, id_, data=None, **options):
        try:
            OrderValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._delete(url, data, **options)
        except CustomException as e:
            return e.error_data