from culqi.utils.validation.card_validation import CardValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Card"]


class Card(Resource):
    endpoint = URL.CARD
    
    def create(self, data, **options):
        CardValidation.create(self, data)
        return Resource.create(self, data, **options)
    
    def list(self, data={}, **options):
        CardValidation.list(self, data)
        url = self._get_url()
        return self._get(url, data, **options)
    
    def read(self, id_, data=None, **options):
        CardValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._get(url, data, **options)
    
    def update(self, id_, data=None, **options):
        CardValidation.update(self, id_)
        url = self._get_url(id_)
        return self._patch(url, data, **options)
