from ..utils.urls import URL
from .base import Resource
from ..schemas import customer

__all__ = ["Customer"]


class Customer(Resource):
    schema = customer.SCHEMA
    endpoint = URL.CUSTOMER
