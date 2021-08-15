# Copyright 2021 iiPython

# Modules
import os
import json
from pyhttpfs import pyhttpfs

# Initialization
_ICONS_FILE = os.path.join(pyhttpfs.assets_dir, "icons.json")
_CAN_LOAD = os.path.isfile(_ICONS_FILE)
if not _CAN_LOAD:
    print("Warning: no icons file is present, icons will be disabled.")

_ICON_DATA = json.loads(open(_ICONS_FILE, "r").read()) if _CAN_LOAD else {}

# Icon loader
def format_img(data: str) -> str:
    return "<img style = 'max-width: 16px;' src = '{}'>".format(data)

def format_icon(ext: str = None, identifier: str = None) -> str:
    if identifier is not None:
        for icon in _ICON_DATA:
            if "id" in icon and icon["id"] == identifier:
                return format_img(icon["data"])

    for icon in _ICON_DATA:
        if "matches" in icon and ext in icon["matches"]:
            return format_img(icon["data"])

    return format_icon(identifier = "blank")

def determine_icon_css(filename: str, filetype: str) -> str:
    if not _CAN_LOAD:
        return ""

    elif filetype == "folder":
        if filename == "../":
            return format_icon(identifier = "top")

        return format_icon(identifier = "folder")

    elif "." not in filename:
        return format_icon(identifier = "blank")

    # Calculate extension
    return format_icon(filename.split(".")[-1])
