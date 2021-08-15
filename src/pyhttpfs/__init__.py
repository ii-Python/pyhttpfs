# Copyright 2021 iiPython

# Modules
import os
import sys
import platform
from flask import Flask

# Meta
__version__ = "1.0.6"

# Initialization
base_dir = os.path.abspath(os.path.dirname(__file__))
pyhttpfs = Flask(
    "PyHTTPFS",
    template_folder = os.path.join(base_dir, "templates")
)
pyhttpfs.assets_dir = os.path.join(base_dir, "assets")
pyhttpfs.static_dir = os.path.join(pyhttpfs.assets_dir, "static")

@pyhttpfs.context_processor
def inject_globals():
    return {"v": __version__, "pyv": platform.python_version(), "pyhttpfs": pyhttpfs}

# Routes
from .routing import *
