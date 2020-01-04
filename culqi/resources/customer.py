from ..schemas import customer
from ..utils.urls import URL
from .base import Resource

__all__ = ["Customer"]


class Customer(Resource):
    schema = customer.SCHEMA
    endpoint = URL.CUSTOMER
