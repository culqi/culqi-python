import json
import logging
from copy import deepcopy
from types import ModuleType

from requests import session

from culqi.utils.constants import CONSTANTS
from culqi.utils.validation.helpers import Helpers

from . import resources
from culqi.utils import capitalize_camel_case
from culqi.version import VERSION
import culqi.utils.encoder as encoder

RESOURCE_CLASSES = {}
SCHEMAS = {}

for name, module in resources.__dict__.items():
    capitalized_name = capitalize_camel_case(name)
    is_module = isinstance(module, ModuleType)
    is_in_module = capitalized_name in getattr(module, "__dict__", {})
    if is_module and is_in_module:
        RESOURCE_CLASSES[name] = module.__dict__[capitalized_name]

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    rsa_aes_encoder = encoder.RsaAesEncoder()
except Exception as e:
    logger.error('Unable to create an instance of Base64Decoder class.', exc_info=True)

class Culqi:
    def __init__(self, public_key, private_key):
        Helpers.validate_string_start(public_key, "pk")
        Helpers.validate_string_start(private_key, "sk")
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
        
        if 'test' in self.private_key:
            xCulqiEnv = CONSTANTS.X_CULQI_ENV_TEST
        else:
            xCulqiEnv = CONSTANTS.X_CULQI_ENV_LIVE
            
        self.session.headers.update(
            {
                "User-Agent": "Culqi-API-Python/{0}".format(self._get_version()),
                "Authorization": "Bearer {0}".format(self.private_key),
                "Content-type": "application/json",
                "Accept": "application/json",
                "x-culqi-env": xCulqiEnv,
                "x-api-version": CONSTANTS.X_API_VERSION,
                "x-culqi-client": CONSTANTS.X_CULQI_CLIENT,
                "x-culqi-client-version": CONSTANTS.X_CULQI_CLIENT_VERSION,
            }
        )

    def request(self, method, url, data, **options):
        """Dispatch a request to the CULQUI HTTP API."""
        if method == "get":
            response = getattr(self.session, method)(url, params=data, **options)
        else:
            response = getattr(self.session, method)(url, data, **options)
            
        data = response.json()

        if "data" in data:
            data["items"] = deepcopy(data["data"])
            del data["data"]

        return {"status": response.status_code, "data": data}

    def get(self, url, params, **options):
        params, options = self._update_request(params, options)
        return self.request("get", url, data=params, **options)

    def post(self, url, data, **options):
        data, options = rsa_aes_encoder.encrypt_validation(data, options)
        data, options = self._update_request(data, options) 
        return self.request("post", url, data, **options)

    def patch(self, url, data, **options):
        data, options = rsa_aes_encoder.encrypt_validation(data, options)
        data, options = self._update_request(data, options)
        return self.request("patch", url, data=data, **options)

    def delete(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("delete", url, data=data, **options)

    def put(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("put", url, data=data, **options)
