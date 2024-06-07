import streamlit as st
import os
import json
from app.file_manager import FileManager
from app.key_manager import KeyManager
from app.encryptor import Encryptor
from app.decryptor import Decryptor

class EncryptionApp:
    def __init__(self):
        self.file_manager = FileManager()
        self.key_manager = KeyManager()
        self.encryptor = Encryptor()
        self.decryptor = Decryptor()

    def start(self):
        st.title("File Encryption and Decryption App")

        menu = ["Encrypt File", "Decrypt File", "Generate Key"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Encrypt File":
            self.encrypt_file()
        elif choice == "Decrypt File":
            self.decrypt_file()
        elif choice == "Generate Key":
            self.generate_key()

    def encrypt_file(self):
        st.subheader("Encrypt a File")

        file = st.file_uploader("Choose a file to encrypt")
        key_option = st.selectbox("Select Key Option", ["Generate New Key", "Use Existing Key", "Use Password"])
        if key_option == "Generate New Key":
            if st.button("Generate and Encrypt"):
                try:
                    key = self.key_manager.generate_key()
                    key_file_path = self.file_manager.save_key("generated_key.key", key)
                    content = self.file_manager.read_file(file)
                    encrypted_content = self.encryptor.encrypt(content, key)
                    encrypted_file_path = self.file_manager.save_encrypted_file("encrypted_file.enc", encrypted_content)
                    self._save_metadata(file.name, "generated_key.key", key_option)
                    st.success(f"File encrypted successfully! Encrypted file saved at: {encrypted_file_path}")
                    st.success(f"Generated key saved at: {key_file_path}")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif key_option == "Use Existing Key":
            key_file = st.file_uploader("Choose a key file")
            if key_file and st.button("Encrypt"):
                try:
                    key = self.key_manager.retrieve_key(key_file)
                    content = self.file_manager.read_file(file)
                    encrypted_content = self.encryptor.encrypt(content, key)
                    encrypted_file_path = self.file_manager.save_encrypted_file("encrypted_file.enc", encrypted_content)
                    self._save_metadata(file.name, key_file.name, key_option)
                    st.success(f"File encrypted successfully! Encrypted file saved at: {encrypted_file_path}")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif key_option == "Use Password":
            password = st.text_input("Enter a password", type="password")
            if st.button("Encrypt"):
                try:
                    key = self.key_manager.generate_key_from_password(password)
                    content = self.file_manager.read_file(file)
                    encrypted_content = self.encryptor.encrypt(content, key)
                    encrypted_file_path = self.file_manager.save_encrypted_file("encrypted_file.enc", encrypted_content)
                    self._save_metadata(file.name, password, key_option)
                    st.success(f"File encrypted successfully! Encrypted file saved at: {encrypted_file_path}")
                except Exception as e:
                    st.error(f"Error: {e}")

    def decrypt_file(self):
        st.subheader("Decrypt a File")

        file = st.file_uploader("Choose a file to decrypt")
        metadata_file = st.file_uploader("Choose the corresponding metadata file")
        key_option = st.selectbox("Select Key Option", ["Use Key File", "Use Password"])
        if metadata_file and file:
            metadata = self._load_metadata(metadata_file)
            if key_option == "Use Key File":
                key_file = st.file_uploader("Choose a key file")
                if key_file and st.button("Decrypt"):
                    try:
                        if metadata['encryption_method'] == "Use Existing Key" and key_file.name == metadata['key']:
                            key = self.key_manager.retrieve_key(key_file)
                            content = self.file_manager.read_file(file)
                            decrypted_content = self.decryptor.decrypt(content, key)
                            decrypted_file_path = self.file_manager.save_decrypted_file("decrypted_file.dec", decrypted_content)
                            st.success(f"File decrypted successfully! Decrypted file saved at: {decrypted_file_path}")
                        else:
                            st.error("Error: Incorrect key file for decryption")
                    except ValueError as e:
                        st.error(f"Error: Invalid key size - {e}")
                    except Exception as e:
                        st.error(f"Error: {e}")

            elif key_option == "Use Password":
                password = st.text_input("Enter a password", type="password")
                if st.button("Decrypt"):
                    try:
                        if metadata['encryption_method'] == "Use Password" and password == metadata['key']:
                            key = self.key_manager.generate_key_from_password(password)
                            content = self.file_manager.read_file(file)
                            decrypted_content = self.decryptor.decrypt(content, key)
                            decrypted_file_path = self.file_manager.save_decrypted_file("decrypted_file.dec", decrypted_content)
                            st.success(f"File decrypted successfully! Decrypted file saved at: {decrypted_file_path}")
                        else:
                            st.error("Error: Incorrect password for decryption")
                    except ValueError as e:
                        st.error(f"Error: Invalid key size - {e}")
                    except Exception as e:
                        st.error(f"Error: {e}")
        else:
            st.error("Please upload both the encrypted file and the corresponding metadata file")

    def generate_key(self):
        st.subheader("Generate a Key")
        seed = st.text_input("Enter a seed (optional)")
        if st.button("Generate Key"):
            try:
                key = self.key_manager.generate_key(seed)
                key_file_path = self.file_manager.save_key("generated_key.key", key)
                st.success(f"Key generated and saved to: {key_file_path}")
            except Exception as e:
                st.error(f"Error: {e}")

    def _save_metadata(self, file_name, key, encryption_method):
        metadata = {
            'file_name': file_name,
            'key': key,
            'encryption_method': encryption_method
        }
        metadata_file_path = os.path.join(self.file_manager.encrypted_dir, f"{file_name}_metadata.json")
        with open(metadata_file_path, 'w') as metadata_file:
            json.dump(metadata, metadata_file)

    def _load_metadata(self, metadata_file):
        return json.load(metadata_file)

if __name__ == "__main__":
    app = EncryptionApp()
    app.start()
