from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Customer"]


class Customer(Resource):
    endpoint = URL.CUSTOMER
