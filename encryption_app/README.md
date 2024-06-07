# Encryption and Decryption Application

## Overview

This project implements a comprehensive encryption and decryption application with a user-friendly interface. The application supports both DES and AES encryption algorithms, allowing users to choose between different key sizes and encryption methods. Additionally, it features key generation from seed/salt and password-based encryption and decryption.

## Features

- **Encrypt File**: Encrypt a file using a provided path, file name, and key.
- **Decrypt File**: Decrypt a file using a provided path, file name, and key.
- **Generate Key from Seed/Salt**: Generate a key from a seed/salt provided through the UI.
- **Encrypt with Password**: Encrypt a file using a provided path, file name, and password.
- **Decrypt with Password**: Decrypt a file using a provided path, file name, and password.
- **256-bit AES Encryption and Decryption**: Supports encryption and decryption using 256-bit AES for enhanced security.

## Project Structure

encryption_app/
├── main.py
├── app/
│ ├── encryption_app.py
│ ├── file_manager.py
│ ├── key_manager.py
│ ├── encryptor.py
│ ├── decryptor.py
│ └── utils.py
├── encrypted_files/
│ └── [encrypted files and metadata will be stored here]
├── decrypted_files/
│ └── [decrypted files will be stored here]
├── keys/
│ └── [keys will be stored here]
└── requirements.txt

## Installation

- **Clone the repository**
  git clone https://github.com/your-repo/encryption_app.git
  cd encryption_app

- **Install dependencies**
  pip install -r requirements.txt

## Running the Application

- **Start the Streamlit app**
  streamlit run main.py

- **Access the application**
  Open your web browser and go to http://localhost:8501 to use the application.
