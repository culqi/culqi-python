from ..utils.urls import URL
from .base import Resource
from ..schemas import card

__all__ = ["Card"]


class Card(Resource):
    schema = card.SCHEMA
    endpoint = URL.CARD
