import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import base64

class RsaAesEncoder:

    def _encrypt(self, data, public_key):
        # Generate a random encryption key
        key = get_random_bytes(32)
        iv = get_random_bytes(16)
        
        # Message to be encrypted
        message = json.dumps(data).encode('utf-8')

        # Initialize the cipher with the key and IV
        cipher = AES.new(key, AES.MODE_GCM, iv)

        # Encrypt the message
        # Note that the message length must be a multiple of 16 bytes
        ciphertext = cipher.encrypt(message)
        
        encrypted_message = base64.b64encode(ciphertext).decode('utf-8')

        # Encrypt the key with the public key
        cipher = PKCS1_OAEP.new(RSA.import_key(public_key), hashAlgo=SHA256)
        ciphertext_key = cipher.encrypt(key)

        # Encrypt the iv with the public key
        cipher = PKCS1_OAEP.new(RSA.import_key(public_key), hashAlgo=SHA256)
        ciphertext_iv = cipher.encrypt(iv)

        # Convert the encrypted message to a string
        encrypted_aes_key = base64.b64encode(ciphertext_key).decode()
        encrypted_aes_iv = base64.b64encode(ciphertext_iv).decode()

        return {
            "encrypted_data": encrypted_message, 
            "encrypted_key": encrypted_aes_key, 
            "encrypted_iv": encrypted_aes_iv
        }

    def encrypt_validation(self, data, options):
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