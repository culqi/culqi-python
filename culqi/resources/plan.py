from culqi.utils.errors import CustomException
from culqi.utils.urls import URL
from culqi.resources.base import Resource
from culqi.utils.validation.plan_validation import PlanValidation

__all__ = ["Plan"]


class Plan(Resource):
    endpoint = URL.PLAN

    def create(self, data, **options):
        try:
            PlanValidation.create(self, data)
            return Resource.create(self, data, **options)
        except CustomException as e:
            return e.error_data
    
    def list(self, data={}, **options):
        try:
            PlanValidation.list(self, data)
            url = self._get_url()
            print(url)
            print(data)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def read(self, id_, data=None, **options):
        try:
            PlanValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def update(self, id_, data=None, **options):
        try:
            PlanValidation.update(self, id_, data)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e.error_data
    
    def delete(self, id_, data=None, **options):
        try:
            PlanValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._delete(url, data, **options)
        except CustomException as e:
            return e.error_data
