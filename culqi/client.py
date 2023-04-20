import json
from copy import deepcopy
from types import ModuleType

from requests import session

from . import resources
from culqi.utils import capitalize_camel_case
from culqi.version import VERSION

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

RESOURCE_CLASSES = {}
SCHEMAS = {}

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

    def request(self, method, url, data, **options):
        """Dispatch a request to the CULQUI HTTP API."""
        response = getattr(self.session, method)(url, data, **options)

        data = response.json()

        if "data" in data:
            data["items"] = deepcopy(data["data"])
            del data["data"]

        return {"status": response.status_code, "data": data}
    
    def _encrypt(self, data, public_key):
        # Generate a random encryption key
        key = get_random_bytes(32)
        iv = get_random_bytes(16)
        
        # Message to be encrypted
        message = json.dumps(data).encode('utf-8')

        # Pad the message to a multiple of 16 bytes using PKCS#7 padding
        block_size = 16
        padding_length = block_size - len(message) % block_size
        padding = bytes([padding_length] * padding_length)
        padded_message = message + padding


        # Initialize the cipher with the key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Encrypt the message
        # Note that the message length must be a multiple of 16 bytes
        ciphertext = cipher.encrypt(padded_message)
        
        encrypted_message = base64.b64encode(ciphertext).decode('utf-8')

        # Encrypt the key with the public key
        cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
        ciphertext_key = cipher.encrypt(key)

        # Encrypt the iv with the public key
        cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
        ciphertext_iv = cipher.encrypt(iv)

        # Convert the encrypted message to a string
        encrypted_aes_key = base64.b64encode(ciphertext_key).decode()
        encrypted_aes_iv = base64.b64encode(ciphertext_iv).decode()

        return {
            "encrypted_data": encrypted_message, 
            "encrypted_key": encrypted_aes_key, 
            "encrypted_iv": encrypted_aes_iv
        }
    
    def _encrypt_validation(self, data, options):
        headers = {}
        if("rsa_public_key" in options and "rsa_id" in options):
            data = self._encrypt(data, options["rsa_public_key"])
            headers["x-culqi-rsa-id"] = options["rsa_id"]
            if "headers" in options:
                options["headers"].update(headers)
            else:
                options["headers"] = headers
            del options["rsa_public_key"]
            del options["rsa_id"]
        
        return data, options

    def get(self, url, params, **options):
        return self.request("get", url, params=params, **options)

    def post(self, url, data, **options):
        data, options = self._encrypt_validation(data, options)
        data, options = self._update_request(data, options) 
        return self.request("post", url, data, **options)

    def patch(self, url, data, **options):
        data, options = self._encrypt_validation(data, options)
        data, options = self._update_request(data, options)
        return self.request("patch", url, data=data, **options)

    def delete(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("delete", url, data=data, **options)

    def put(self, url, data, **options):
        data, options = self._update_request(data, options)
        return self.request("put", url, data=data, **options)
