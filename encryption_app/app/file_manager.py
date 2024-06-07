import os

class FileManager:
    def __init__(self):
        self.encrypted_dir = "encrypted_files"
        self.decrypted_dir = "decrypted_files"
        self.keys_dir = "keys"
        self._create_directories()

    def _create_directories(self):
        os.makedirs(self.encrypted_dir, exist_ok=True)
        os.makedirs(self.decrypted_dir, exist_ok=True)
        os.makedirs(self.keys_dir, exist_ok=True)

    def read_file(self, file):
        try:
            return file.read()
        except Exception as e:
            raise IOError(f"Error reading file: {e}")

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'wb') as file:
                file.write(content)
        except Exception as e:
            raise IOError(f"Error writing to file: {e}")

    def save_encrypted_file(self, filename, content):
        file_path = os.path.join(self.encrypted_dir, filename)
        self.write_file(file_path, content)
        return file_path

    def save_decrypted_file(self, filename, content):
        file_path = os.path.join(self.decrypted_dir, filename)
        self.write_file(file_path, content)
        return file_path

    def save_key(self, filename, content):
        file_path = os.path.join(self.keys_dir, filename)
        self.write_file(file_path, content)
        return file_path
