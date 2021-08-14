# Copyright 2021 iiPython

# Modules
import os
import platform
from flask import Flask

# Meta
__version__ = "1.0.2"

# Initialization
base_dir = os.path.abspath(os.path.dirname(__file__))
pyhttpfs = Flask(
    "PyHTTPFS",
    template_folder = os.path.join(base_dir, "templates")
)

@pyhttpfs.context_processor
def inject_globals():
    return {"v": __version__, "pyv": platform.python_version(), "pyhttpfs": pyhttpfs}

# Routes
from .routing import *
