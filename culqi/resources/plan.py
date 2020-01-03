from ..utils.urls import URL
from .base import Resource
from ..schemas import plan

__all__ = ["Plan"]


class Plan(Resource):
    schema = plan.SCHEMA
    endpoint = URL.PLAN
