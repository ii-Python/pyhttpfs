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
            if arg.strip() and arg[0] == "-":
                try:
                    value = self.argv[self.argv.index(arg) + 1]
                    self.args[arg[1:]] = value

                except IndexError:
                    raise ValueError("Config key '{}' has no value!".format(arg))

    def get(self, key: str) -> Union[str, None]:
        if key not in self.args:
            return None

        return self.args[key]

args = Arguments()
