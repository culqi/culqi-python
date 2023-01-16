from ..utils.urls import URL
from .base import Resource

__all__ = ["Card"]


class Card(Resource):
    endpoint = URL.CARD
