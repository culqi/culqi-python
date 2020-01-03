from ..utils.urls import URL
from .base import Resource
from ..schemas import subscription

__all__ = ["Subscription"]


class Subscription(Resource):
    schema = subscription.SCHEMA
    endpoint = URL.SUBSCRIPTION
