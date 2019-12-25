from .base import Resource

from ..utils.urls import URL


__all__ = [
    'Card'
]


class Card(Resource):
    endpoint = URL.CARD
