from ..schemas import plan
from ..utils.urls import URL
from .base import Resource

__all__ = ["Plan"]


class Plan(Resource):
    schema = plan.SCHEMA
    endpoint = URL.PLAN
