from culqi.utils.urls import URL
from culqi.resources.base import Resource
from culqi.utils.culqi_validation import CulqiValidation

__all__ = ["Plan"]


class Plan(Resource):
    endpoint = URL.PLAN

    def create(self, data, **options):
        CulqiValidation.plan_validation(self, data)
        return Resource.create(self, data, **options)
