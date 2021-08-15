# Copyright 2021 iiPython

# Modules
import sys
from typing import Union

# Argument parser
class Arguments(object):
    def __init__(self) -> None:
        self.args = {}
        self.parse_args()

    def parse_args(self) -> None:
        if not hasattr(self, "argv"):
            self.argv = sys.argv[1:]

        for arg in self.argv:
            if arg.strip() and arg[0] == "-" and not arg.startswith("--"):
                try:
                    value = self.argv[self.argv.index(arg) + 1]
                    self.args[arg[1:]] = value

                except IndexError:
                    raise ValueError("Config key '{}' has no value!".format(arg))

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
