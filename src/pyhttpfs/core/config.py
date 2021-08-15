# Copyright 2021 iiPython

# Modules
import os
import json
from typing import Any
from pyhttpfs import pyhttpfs, base_dir

# Config class
class Configuration(object):
    def __init__(self) -> None:
        self._raw_data = {}
        self._generate_config()

    def _generate_config(self) -> None:
        config_file = os.path.join(base_dir, "pyhttpfs.json")
        if os.path.isfile(config_file):
            try:
                with open(config_file, "r") as config:
                    self._raw_data = json.loads(config.read())

            except Exception as exc:
                pyhttpfs.log("[red]Failed to load config file at '{}';\n\t{}".format(config_file, exc))

    def get(self, key: Any) -> Any:
        if key not in self._raw_data:
            return None

        return self._raw_data[key]

config = Configuration()
