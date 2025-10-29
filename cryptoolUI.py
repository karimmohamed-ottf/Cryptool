from colors import *
from ascii import crypto_ascii
from cryptoolLogic import Crypto
from cryptoolUtils import CryptoUtils
from wrappers import class_error_handling
import os

class CryptoUI():
    def __init__(self):
        self.cryptoutils = CryptoUtils()
        self.crypto = Crypto()

    @class_error_handling
    def main(self):
        while True:
            self.cryptoutils.clear_screen()
            self.cryptoutils.ascii_logo()
            user_choice = input(f'''\n\n{BOLD}{FG_WHITE}Enter Your Choice:
\n{BOLD}{FG_WHITE}1) Encrypt File
2) Decrypt File
3) Generate Key File
4) Exit Program\n\n{FG_WHITE}>>>{RESET} ''')
            menu_options = {
                "1": lambda: self.files_operations("Encrypt", "file_to_encrypt"),
                "2": lambda: self.files_operations("Decrypt", "file_to_decrypt"),
                "3": lambda: self.generate_key_file(),
                "4": lambda: self.cryptoutils.exit_program()
            }
            if user_choice in menu_options:
                func = menu_options[user_choice]
                func()
            else:
                self.cryptoutils.error_message()
                self.cryptoutils.pause()
                self.cryptoutils.clear_screen() 

    @class_error_handling
    def files_operations(self, operation_name, operation_file):
        while True:
            self.cryptoutils.clear_screen()
            self.cryptoutils.ascii_logo()
            operation_file = input(f"{BOLD}{FG_WHITE}\nEnter The Path For The File To {operation_name}:\n{FG_WHITE}>>>{RESET} ")
            if os.path.exists(operation_file):
                encryption_key_file = input(f"{BOLD}{FG_WHITE}Enter the Path for the Key File:\n{FG_WHITE}>>>{RESET} ")
                if os.path.exists(encryption_key_file):
                    if operation_name.lower() == "encrypt":
                        self.crypto.encrypt(encryption_key_file, operation_file)
                    else:
                        self.crypto.decrypt(encryption_key_file, operation_file)

                    print(f"{BOLD}{FG_GREEN}==> Successfully {operation_name}ed: {operation_file}")
                    self.cryptoutils.pause()
                    break
                else:
                    self.cryptoutils.error_message()
                    return
            else:
                self.cryptoutils.error_message()
                return

    @class_error_handling
    def generate_key_file(self):
        while True:
            self.cryptoutils.clear_screen()
            self.cryptoutils.ascii_logo()
            generated_key_file = input(f"{BOLD}{FG_WHITE}\nEnter the Path for a new Key file to be Generated:\n>>> {RESET}")
            self.crypto.generate_key(generated_key_file)
            print(f"{BOLD}{FG_GREEN}\n==> Successfully Generated a Key File to {generated_key_file}")
            print(f"{BOLD}{FG_RED}*** This is a Plain Text Key, Make Sure To Store It Safely ***")
            self.cryptoutils.pause()
            return

    def exit_program(self):
        self.cryptoutils.exit_program()
