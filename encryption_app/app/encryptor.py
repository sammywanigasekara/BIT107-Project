from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class Encryptor:
    def __init__(self):
        self.algorithm = algorithms.AES
        self.key = None

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def encrypt(self, data, key):
        self.key = key
        if len(self.key) not in [16, 24, 32]:  # 128, 192, 256 bits
            raise ValueError("Invalid key size for AES")
        iv = os.urandom(16)
        cipher = Cipher(self.algorithm(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = iv + encryptor.update(data) + encryptor.finalize()
        return encrypted_data
