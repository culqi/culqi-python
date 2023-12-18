from culqi.utils.urls import URL
from culqi.resources.base import Resource
from culqi.utils.validation.plan_validation import PlanValidation

__all__ = ["Plan"]


class Plan(Resource):
    endpoint = URL.PLAN

    def create(self, data, **options):
        PlanValidation.create(self, data)
        return Resource.create(self, data, **options)
    
    def list(self, data={}, **options):
        PlanValidation.list(self, data)
        url = self._get_url()
        return self._get(url, data, **options)
    
    def read(self, id_, data=None, **options):
        PlanValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._get(url, data, **options)
    
    def update(self, id_, data=None, **options):
        PlanValidation.update(self, id_)
        url = self._get_url(id_)
        return self._patch(url, data, **options)
    
    def delete(self, id_, data=None, **options):
        PlanValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._delete(url, data, **options)
