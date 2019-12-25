import json

from types import ModuleType

from requests import session

from .version import VERSION
from .utils import capitalize_camel_case
from . import resources


RESOURCE_CLASSES = {}

for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[capitalize_camel_case(name)]


class Client:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = session()

        self._set_client_headers()

        for name, klass in RESOURCE_CLASSES.items():
            setattr(self, name, klass(self))

    @staticmethod
    def _get_version():
        return '.'.join(VERSION)

    @staticmethod
    def _update_request(data, options):
        """Updates The resource data and header options."""
        data = json.dumps(data)

        if 'headers' not in options:
            options['headers'] = {}

        options['headers'].update({
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })

        return data, options

    def _set_client_headers(self):
        self.session.headers.update({
            'User-Agent': f'Culqi-API-Python/{self._get_version()}',
            'Authorization': f'Bearer {self.api_secret}',
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })

    def request(self, method, url, **options):
        """Dispatches a request to the CULQUI HTTP API."""
        response = getattr(self.session, method)(url, **options)

        return {
            'status': response.status_code,
            'data': response.json()
        }

    def get(self, url, params, **options):
        return self.request('get', url, params=params, **options)

    def post(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request('post', url, data=data, **options)

    def patch(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request('patch', url, data=data, **options)

    def delete(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request('delete', url, data=data, **options)

    def put(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request('put', url, data=data, **options)
