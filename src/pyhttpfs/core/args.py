# Copyright 2021 iiPython

# Modules
import sys
from typing import Union

# Argument parser
class Arguments(object):
    def __init__(self) -> None:
        self.args = {}
        self.shorthands = {
            "dir": "l",
            "bind": "b",
            "port": "p"
        }

        self.parse_args()

    def parse_args(self) -> None:
        if not hasattr(self, "argv"):
            self.argv = sys.argv[1:]

        waiting = None
        for arg in self.argv:
            if not arg.strip() or not arg[0] == "-" and waiting is None:
                continue

            elif waiting is not None:
                self.args[waiting] = arg
                waiting = None
                continue

            arg = arg.lstrip("-")
            if arg in self.shorthands:
                arg = self.shorthands[arg]

            waiting = arg

        if waiting is not None:
            raise ValueError(f"'{waiting}' was provided but no value was specified!")

    def get(self, key: str, accept: type = None) -> Union[str, None]:
        if key not in self.args:
            return None

        value = self.args[key]
        if accept is not None:
            try:
                return accept(value)

            except ValueError:
                raise ValueError("key '{}' needs a '{}' object!".format(key, accept.__name__))

        return value

args = Arguments()
