from .base import Resource

from ..utils.urls import URL


__all__ = [
    "Customer"
]


class Customer(Resource):
    endpoint = URL.CUSTOMER
