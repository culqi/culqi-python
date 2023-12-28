from culqi.utils.errors import CustomException
from culqi.utils.validation.subscription_validation import SubscriptionValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Subscription"]


class Subscription(Resource):
    endpoint = URL.SUBSCRIPTION
    
    def create(self, data, **options):
        try:
            SubscriptionValidation.create(self, data)
            return Resource.create(self, data, **options)
        except CustomException as e:
            return e
    
    def list(self, data={}, **options):
        try:
            SubscriptionValidation.list(self, data)
            url = self._get_url()
            return self._get(url, data, **options)
        except CustomException as e:
            return e
    
    def read(self, id_, data={}, **options):
        try:
            SubscriptionValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._get(url, data, **options)
        except CustomException as e:
            return e
    
    def update(self, id_, data={}, **options):
        try:
            SubscriptionValidation.update(self, id_)
            url = self._get_url(id_)
            return self._patch(url, data, **options)
        except CustomException as e:
            return e
    
    def delete(self, id_, data=None, **options):
        try:
            SubscriptionValidation.retrieve(self, id_)
            url = self._get_url(id_)
            return self._delete(url, data, **options)
        except CustomException as e:
            return e
