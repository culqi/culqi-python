from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Subscription"]


class Subscription(Resource):
    endpoint = URL.SUBSCRIPTION
