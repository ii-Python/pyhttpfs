# Copyright 2021 iiPython

# Modules
import os
import json
from typing import Any

# Initialization
_PYHTTPFS_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Config class
class Configuration(object):
    def __init__(self) -> None:
        self._raw_data = {}
        self._config_names = ["config", "pyhttpfs"]

        self._generate_config()

    def _generate_config(self) -> None:
        config_files, loaded = [[os.path.join(path, file) for file in os.listdir(path) if file.count(".") == 1 and file.split(".")[0] in self._config_names and file.split(".")[1] == "json"] for path in [os.getcwd(), _PYHTTPFS_DIR]], []
        for config_file in config_files:
            config_file = config_file[0]  # Stop since we are double indexed

            if config_file in loaded:
                continue

            # Load file
            try:
                with open(config_file, "r") as config:
                    self._raw_data | json.loads(config.read())

                loaded.append(config_file)

            except Exception as exc:
                print("Warning: Failed to load config file at '{}';\n\t{}".format(config_file, exc))

    def get(self, key: Any) -> Any:
        if key not in self._raw_data:
            return None

        return self._raw_data[key]

config = Configuration()
