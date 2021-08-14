# Copyright 2021 iiPython

# Modules
from src import pyhttpfs

# Launch server
pyhttpfs.run(
    host = "0.0.0.0",
    port = 8080,
    debug = True
)
