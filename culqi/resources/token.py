from ..utils.errors import CustomException, ErrorMessage, NotAllowedError
from ..utils.urls import URL
from .base import Resource
from ..utils.validation.token_validation import TokenValidation

__all__ = ["Token"]


class Token(Resource):
    endpoint = URL.TOKEN

    def create(self, data, **options):
        try:
            TokenValidation.create_token_validation(self, data)
            headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
            if "headers" in options:
                options["headers"].update(headers)
            else:
                options["headers"] = headers
            url = self._get_url_secure()
            return self._post(url, data, **options)
        except CustomException as e:
            return e.error_data

    def createyape(self, data, **options):
        try:
            TokenValidation.create_token_yape_validation(self, data)
            headers = {"Authorization": "Bearer {0}".format(self.client.public_key)}
            if "headers" in options:
                options["headers"].update(headers)
            else:
                options["headers"] = headers
            url = self._get_url_secure("yape")
            return self._post(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)
    
    def read(self, id_, data=None, **options):
        try:
            TokenValidation.token_retrieve_validation(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
            
    
    def update(self, id_, data=None, **options):
        try:
            TokenValidation.token_update_validation(self, id_)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def list(self, data={}, **options):
        try:
            url = self._get_url()
            TokenValidation.token_list_validation(self, data)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
