# Copyright 2021 iiPython

# Modules
import os
from platform import python_version

# Color map
def _to_ansi(code: int) -> str:
    return f"\033[{code}m"

_color_map = {
    "black": 30, "red": 31, "green": 32,
    "yellow": 33, "blue": 34, "magenta": 35,
    "cyan": 36, "white": 37, "reset": 39
}
_new_clmap = {}
for color in _color_map:
    _cl = _color_map[color]
    _new_clmap[color] = _to_ansi(_cl)

_color_map = _new_clmap

# Handle logging
def _format_str(message: str) -> str:
    for key in _color_map:
        message = message.replace(f"[{key}]", _color_map[key]).replace(f"[/{key}]", _color_map["reset"])

    return message + _color_map["reset"]

def log(text: str, code: int = None) -> None:
    print(_format_str(text))
    if text is not None:
        return exit(text)

# Banner
class Banner(object):
    def __init__(self, version: str, show_prod_warning: bool = True) -> None:
        self.conf = {
            "show_prod_warn": show_prod_warning
        }
        self.version = version

    def show(self) -> None:
        if os.environ.get("_pyhfs_bnr_ld", ""):
            return

        os.environ["_pyhfs_bnr_ld"] = "true"
        print(_format_str(f"[yellow]PyHTTPFS v{self.version}; running on Python {python_version()}"))
        if self.conf["show_prod_warn"]:
            print(_format_str("[red]Please note: PyHTTPFS is not meant for production, use it wisely."))

banner = Banner
