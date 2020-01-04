from ..schemas import card
from ..utils.urls import URL
from .base import Resource

__all__ = ["Card"]


class Card(Resource):
    schema = card.SCHEMA
    endpoint = URL.CARD
