from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class Decryptor:
    def __init__(self):
        self.algorithm = algorithms.AES
        self.key = None

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def decrypt(self, encrypted_data, key):
        self.key = key
        if len(self.key) not in [16, 24, 32]:  # 128, 192, 256 bits
            raise ValueError("Invalid key size for AES")
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]
        cipher = Cipher(self.algorithm(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_data
