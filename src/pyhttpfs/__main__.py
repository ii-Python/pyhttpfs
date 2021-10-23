# Copyright 2021 iiPython

# Modules
import os
import sys
if "--debug" in sys.argv:
    sys.argv.remove("--debug")
    sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from pyhttpfs.core.args import args
from pyhttpfs import pyhttpfs, banner

sys.modules["flask.cli"].show_server_banner = lambda *x: None
banner.show()

# Launch server
def main():
    try:
        pyhttpfs.run(
            host = args.get("b", accept = str) or "0.0.0.0",
            port = args.get("p", accept = int) or 8080,
            debug = True
        )

    except PermissionError:
        print("Errno 13 Permission Denied: are you binding to port <1024? Try using sudo.")

if __name__ == "__main__":
    main()
