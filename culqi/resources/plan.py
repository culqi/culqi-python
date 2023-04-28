from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Plan"]


class Plan(Resource):
    endpoint = URL.PLAN
