from culqi.utils.validation.subscription_validation import SubscriptionValidation
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Subscription"]


class Subscription(Resource):
    endpoint = URL.SUBSCRIPTION
    
    def create(self, data, **options):
        SubscriptionValidation.create(self, data)
        return Resource.create(self, data, **options)
    
    def list(self, data={}, **options):
        SubscriptionValidation.list(self, data)
        url = self._get_url()
        return self._get(url, data, **options)
    
    def read(self, id_, data={}, **options):
        SubscriptionValidation.retrieve(self, id_)
        url = self._get_url(id_)
        return self._get(url, data, **options)
    
    def update(self, id_, data={}, **options):
        SubscriptionValidation.update(self, id_)
        url = self._get_url(id_)
        return self._patch(url, data, **options)
