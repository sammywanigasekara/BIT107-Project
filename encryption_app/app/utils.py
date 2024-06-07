import os

def generate_random_bytes(length):
    """Generate random bytes of specified length."""
    return os.urandom(length)

def save_file(file_path, content):
    """Save content to a file at the specified path."""
    try:
        with open(file_path, 'wb') as file:
            file.write(content)
    except Exception as e:
        raise IOError(f"Error writing to file: {e}")

def read_file(file_path):
    """Read and return content from a file at the specified path."""
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except Exception as e:
        raise IOError(f"Error reading file: {e}")
