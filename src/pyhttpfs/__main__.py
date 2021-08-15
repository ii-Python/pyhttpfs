# Copyright 2021 iiPython

# Modules
from pyhttpfs import pyhttpfs
from pyhttpfs.core.args import args

# Launch server
def main():
    pyhttpfs.run(
        host = args.get("b", accept = str) or "0.0.0.0",
        port = args.get("p", accept = int) or 8080,
        debug = True
    )

if __name__ == "__main__":
    main()
