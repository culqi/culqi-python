import json
from copy import deepcopy
from types import ModuleType

from requests import session

from . import resources
from .utils import capitalize_camel_case
from .version import VERSION

RESOURCE_CLASSES = {}

for name, module in resources.__dict__.items():
    capitalized_name = capitalize_camel_case(name)
    is_module = isinstance(module, ModuleType)
    is_in_module = capitalized_name in getattr(module, "__dict__", {})
    if is_module and is_in_module:
        RESOURCE_CLASSES[name] = module.__dict__[capitalized_name]


class Culqi:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.session = session()

        self._set_client_headers()

        for name, klass in RESOURCE_CLASSES.items():
            setattr(self, name, klass(self))

    @staticmethod
    def _get_version():
        return ".".join(VERSION)

    @staticmethod
    def _update_request(data, options):
        """Update The resource data and header options."""
        data = json.dumps(data)

        if "headers" not in options:
            options["headers"] = {}

        options["headers"].update(
            {"Content-type": "application/json", "Accept": "application/json"}
        )

        return data, options

    def _set_client_headers(self):
        self.session.headers.update(
            {
                "User-Agent": "Culqi-API-Python/{0}".format(self._get_version()),
                "Authorization": "Bearer {0}".format(self.private_key),
                "Content-type": "application/json",
                "Accept": "application/json",
            }
        )

    def request(self, method, url, **options):
        """Dispatch a request to the CULQUI HTTP API."""
        response = getattr(self.session, method)(url, **options)

        data = response.json()

        if "data" in data:
            data["items"] = deepcopy(data["data"])
            del data["data"]

        print(data)

        return {"status": response.status_code, "data": data}

    def get(self, url, params, **options):
        return self.request("get", url, params=params, **options)

    def post(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("post", url, data=data, **options)

    def patch(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("patch", url, data=data, **options)

    def delete(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("delete", url, data=data, **options)

    def put(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("put", url, data=data, **options)
