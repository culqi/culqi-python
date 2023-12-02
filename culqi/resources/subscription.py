from culqi.utils.culqi_validation import CulqiValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Subscription"]


class Subscription(Resource):
    endpoint = URL.SUBSCRIPTION
    
    def create(self, data, **options):
        CulqiValidation.subscription_validation(self, data)
        return Resource.create(self, data, **options)
