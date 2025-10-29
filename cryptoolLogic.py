from cryptography.fernet import Fernet, InvalidToken
import os 
from wrappers import invalid_token_handling

class Crypto():
    def __init__(self):
        self.generated_key = None

    def generate_key(self, key_file_path):
        self.generated_key = Fernet.generate_key()
        with open(key_file_path, "wb") as key_file:
            key_file.write(self.generated_key)

    @invalid_token_handling
    def encrypt(self, key_file_path, file_path):
        with open(key_file_path, "rb") as key_file:
            encryption_key = key_file.read()
        fernet_instance = Fernet(encryption_key)
        with open(file_path, "rb") as target_file:
            original_content = target_file.read()
        encrypted_content = fernet_instance.encrypt(original_content)
        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_content)

    @invalid_token_handling
    def decrypt(self, key_file_path, encrypted_file_path):
        with open(key_file_path, "rb") as key_file:
            encryption_key = key_file.read()
        fernet_instance = Fernet(encryption_key)
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_content = encrypted_file.read()
        decrypted_content = fernet_instance.decrypt(encrypted_content)
        decrypted_file_path = encrypted_file_path.replace(".enc", "")
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_content)

