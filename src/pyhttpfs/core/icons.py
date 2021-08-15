# Copyright 2021 iiPython

# Modules
import os
import json
from pyhttpfs import pyhttpfs

# Initialization
_ICONS_DIR = os.path.join(pyhttpfs.static_dir, "icons")
_ICONS_FILE = os.path.join(pyhttpfs.assets_dir, "icons.json")
_CAN_LOAD = os.path.isfile(_ICONS_FILE)
if not _CAN_LOAD:
    print("Warning: no icons file is present, icons will be disabled.")

_ICON_DATA = json.loads(open(_ICONS_FILE, "r").read()) if _CAN_LOAD else {}

# Icon loader
def format_img(path: str) -> str:
    return "<img style = 'width: 16px; height: 16px;' src = '/stat/icons/{}'>".format(path)

def format_icon(ext: str, manual: bool = False) -> str:
    if manual is True:
        return format_img([i["name"] for i in _ICON_DATA if i["name"] == ext + ".png"][0])

    for icon in _ICON_DATA:
        if ext in icon["matches"]:
            return format_img(icon["name"])

    return format_icon("_blank", True)

def determine_icon_css(filename: str, filetype: str) -> str:
    if not _CAN_LOAD:
        return ""

    elif filetype == "folder":
        if filename == "../":
            return format_icon("_top", True)

        return format_icon("_folder", True)

    elif "." not in filename:
        return format_icon("_blank", True)

    # Calculate extension
    return format_icon(filename.split(".")[-1])
