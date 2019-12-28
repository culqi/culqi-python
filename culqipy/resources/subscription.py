from .base import Resource

from ..utils.urls import URL


__all__ = [
    "Subscription"
]


class Subscription(Resource):
    endpoint = URL.subscription
