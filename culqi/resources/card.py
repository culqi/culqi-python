from culqi.utils.errors import CustomException
from culqi.utils.validation.card_validation import CardValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Card"]


class Card(Resource):
    endpoint = URL.CARD
    
    def create(self, data, **options):
        try:
            CardValidation.create(self, data)
            return Resource.create(self, data, **options)
        except CustomException as e:
            return e.error_data
    
    def list(self, data={}, **options):
        try:
            CardValidation.list(self, data)
            url = self._get_url()
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def read(self, id_, data=None, **options):
        try:
            CardValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def update(self, id_, data=None, **options):
        try:
            CardValidation.update(self, id_)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def delete(self, id_, data=None, **options):
        try:
            CardValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._delete(url, data, **options)
        except CustomException as e:
            return e.error_data
