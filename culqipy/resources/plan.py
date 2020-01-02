from ..utils.urls import URL
from .base import Resource

__all__ = ["Plan"]


class Plan(Resource):
    endpoint = URL.PLAN
