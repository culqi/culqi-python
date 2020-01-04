from ..schemas import subscription
from ..utils.urls import URL
from .base import Resource

__all__ = ["Subscription"]


class Subscription(Resource):
    schema = subscription.SCHEMA
    endpoint = URL.SUBSCRIPTION
