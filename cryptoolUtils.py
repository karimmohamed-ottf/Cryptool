from colors import DIM, BOLD, FG_BLUE, FG_RED
from ascii import crypto_ascii
from wrappers import class_error_handling
import os

class CryptoUtils():
    def __init__(self):
        pass

    def clear_screen(self):
        os.system("clear")

    def ascii_logo(self):
        print(crypto_ascii)

    @class_error_handling
    def pause(self):
        input(f"{DIM}{FG_BLUE}\nPress Enter to Return... ")

    @class_error_handling
    def error_message(self):
        print(f"{BOLD}{FG_RED}==> an error has accured, Check your Input!")
        self.pause()

    def exit_program(self):
        print(f"{DIM}{FG_BLUE}\n==> Exitting... ")
        exit(0)

    @class_error_handling
    def welcome_message(self):
        self.clear_screen()
        self.ascii_logo()
        self.pause()
