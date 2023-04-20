from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Card"]


class Card(Resource):
    endpoint = URL.CARD
