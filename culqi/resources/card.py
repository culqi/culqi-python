from culqi.utils.culqi_validation import CulqiValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Card"]


class Card(Resource):
    endpoint = URL.CARD
    
    def create(self, data, **options):
        CulqiValidation.card_validation(self, data)
        return Resource.create(self, data, **options)
