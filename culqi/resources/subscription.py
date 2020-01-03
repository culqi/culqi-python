from ..utils.urls import URL
from .base import Resource

__all__ = ["Subscription"]


class Subscription(Resource):
    endpoint = URL.SUBSCRIPTION
