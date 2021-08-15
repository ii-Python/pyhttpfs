# Copyright 2021 iiPython

# Modules
from colorama import Fore

# Color mapping
_CL_MAP = {
    "red": Fore.RED, "green": Fore.GREEN, "blue": Fore.BLUE, "cyan": Fore.CYAN,
    "yellow": Fore.YELLOW, "dark": Fore.LIGHTBLACK_EX, "reset": Fore.RESET
}

# Handle logging
def _format_str(message: str) -> str:
    for key in _CL_MAP:
        message = message.replace(f"[{key}]", _CL_MAP[key])

    return message + _CL_MAP["reset"]

def log(message: str, terminate: int = None) -> None:
    print(_format_str(message))
    if terminate is not None:
        return exit(terminate)
