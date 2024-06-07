import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

class KeyManager:
    def generate_key(self, seed=None, length=32):
        if seed:
            seed = seed.encode()
        else:
            seed = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=seed,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(seed)
        return key

    def store_key(self, key, file_path):
        try:
            with open(file_path, 'wb') as file:
                file.write(key)
        except Exception as e:
            raise IOError(f"Error writing key to file: {e}")

    def retrieve_key(self, key_file):
        try:
            return key_file.read()
        except Exception as e:
            raise IOError(f"Error reading key file: {e}")

    def generate_key_from_password(self, password, salt=None, length=32):
        password = password.encode()
        if not salt:
            salt = os.urandom(16)
        kdf = Scrypt(
            salt=salt,
            length=length,
            n=2**14,
            r=8,
            p=1,
            backend=default_backend()
        )
        key = kdf.derive(password)
        return key
