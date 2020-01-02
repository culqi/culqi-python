from ..utils.urls import URL
from .base import Resource

__all__ = ["Customer"]


class Customer(Resource):
    endpoint = URL.CUSTOMER
