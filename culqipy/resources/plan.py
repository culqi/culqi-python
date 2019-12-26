from .base import Resource

from ..utils.urls import URL


__all__ = [
    "Plan"
]


class Plan(Resource):
    endpoint = URL.PLAN
