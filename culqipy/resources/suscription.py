from .base import Resource

from ..utils.urls import URL


__all__ = [
    'Suscription'
]


class Suscription(Resource):
    endpoint = URL.SUSCRIPTION
