import json
from copy import deepcopy
from types import ModuleType

from requests import session

from . import resources
from .utils import capitalize_camel_case
from .version import VERSION

RESOURCE_PREFIX = "_resource_"
RESOURCE_CLASSES = {}
SCHEMAS = {}

for name, module in resources.__dict__.items():
    capitalized_name = capitalize_camel_case(name)
    is_module = isinstance(module, ModuleType)
    is_in_module = capitalized_name in getattr(module, "__dict__", {})
    if is_module and is_in_module:
        RESOURCE_CLASSES[name] = module.__dict__[capitalized_name]


class Culqi(object):
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.session = session()

        self._set_client_headers()

        # Resouces are dynamically injected as private attributes with a
        # `RESOURCE_PREFIX` here. Due to this injection pylint will throw a
        # `no-member` error (E1101). This error in avoided with an overload
        # of `__getattr__` method few lines below.
        for name, klass in RESOURCE_CLASSES.items():
            setattr(self, RESOURCE_PREFIX + name, klass(self))

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

    # PUT method is never used in Culqi resources
    # def put(self, url, data, **options):
    #     data, options = self._update_request(data, options)
    #     return self.request("put", url, data=data, **options)

    def __getattr__(self, name):
        # This method will be called if the standar accesos for a property
        # named `name` fails. I this situation if the propery name not start
        # with `RESOURCE_PREFIX` ...
        if not name.startswith(RESOURCE_PREFIX):
            # ... we will try to get the prefixed version of the attribute
            # name
            return getattr(self, RESOURCE_PREFIX + name)

        return super(Culqi, self).__getattribute__(name)
