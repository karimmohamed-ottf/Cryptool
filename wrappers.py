def class_error_handling(func):
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except (KeyboardInterrupt, EOFError):
            self.exit_program()
        except (ValueError):
            self.exit_program()
    return wrapper

def invalid_token_handling(func):
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except (InvalidToken, ValueError):
            print(f"{BOLD}{FG_RED}==> Corrupted Key File or Target!")  
    return wrapper
