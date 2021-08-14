# Copyright 2021 iiPython

# Modules
import os
from src import pyhttpfs
from src.args import args
from src.config import config
from .core.icons import determine_icon_css
from flask import redirect, url_for, abort, send_file, render_template

# Routes
@pyhttpfs.route("/")
@pyhttpfs.route("/pub")
def _redir_idx():
    return redirect(url_for("explore_path"))

@pyhttpfs.route("/pub/")
@pyhttpfs.route("/pub/<path:path>")
def explore_path(path: str = ""):

    # Handle special characters
    path = path.replace("%20", " ")

    # Initialization
    path = "./" + path
    explorer_location = config.get("defaultExplorerLocation") or args.get("l") or os.getcwd()
    if explorer_location is None:
        raise RuntimeError("The current explorer location is None!")

    elif not os.path.isdir(explorer_location):
        raise RuntimeError("Explorer location isn't a valid directory!")

    fullpath = os.path.abspath(os.path.join(explorer_location, path))
    if explorer_location not in fullpath:
        return abort(403)

    # Handle files
    if os.path.isfile(fullpath):
        return send_file(fullpath, conditional = True)

    # Handle folder
    all_items, al_sorted_items = os.listdir(fullpath) + (["../"] if fullpath != explorer_location else []), []
    for item in sorted(all_items):
        filepath = os.path.join(fullpath, item)
        filetype = {True: "folder", False: "file"}[os.path.isdir(filepath)]

        icon = determine_icon_css(item, filetype)
        al_sorted_items.append(
            {
                "name": item,
                "icon": icon,
                "type": filetype,
                "path": filepath.replace(explorer_location, "", 1)
            }
        )

    sorted_items = [_ for _ in al_sorted_items if _["type"] == "folder"] + [_ for _ in al_sorted_items if _["type"] == "file"]
    return render_template("explorer.html", items = sorted_items, path = path), 200

@pyhttpfs.route("/stat/<path:path>")
def get_static_file(path):
    return send_file(os.path.join(pyhttpfs.static_dir, path), conditional = True)
