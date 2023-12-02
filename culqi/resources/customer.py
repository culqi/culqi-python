from culqi.utils.culqi_validation import CulqiValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Customer"]


class Customer(Resource):
    endpoint = URL.CUSTOMER

    def create(self, data, **options):
        CulqiValidation.customer_validation(self, data)
        return Resource.create(self, data, **options)
