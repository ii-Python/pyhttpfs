# Copyright 2021 iiPython

# Modules
import os
import urllib.parse
from pyhttpfs import pyhttpfs
from pyhttpfs.core.args import args
from pyhttpfs.core.config import config
from pyhttpfs.core.icons import determine_icon_css
from flask import redirect, url_for, abort, send_file, render_template

# Handle file size
suffixes = ["B", "KB", "MB", "GB", "TB", "PB"]
def format_bytes(nbytes: int) -> str:
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1

    f = ("%.2f" % nbytes).rstrip("0").rstrip(".")
    return "%s %s" % (f, suffixes[i])

# Routes
@pyhttpfs.route("/")
@pyhttpfs.route("/pub")
def _redir_idx():
    return redirect(url_for("explore_path"))

@pyhttpfs.route("/pub/")
@pyhttpfs.route("/pub/<path:path>")
def explore_path(path: str = "./"):

    # Handle special characters
    try:
        path = urllib.parse.unquote(path)

    except Exception:
        return abort(400)

    # Initialization
    explorer_location = args.get("l") or config.get("defaultExplorerLocation") or os.getcwd()
    if explorer_location is None:
        raise RuntimeError("The current explorer location is None!")

    elif not os.path.isdir(explorer_location):
        raise RuntimeError("Explorer location isn't a valid directory!")

    explorer_location = os.path.abspath(explorer_location)
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
        if os.path.islink(filepath):
            continue

        filetype = {True: "folder", False: "file"}[os.path.isdir(filepath)]
        icon = determine_icon_css(item, filetype)

        al_sorted_items.append(
            {
                "name": item, "icon": icon, "size": format_bytes(os.path.getsize(filepath)) if filetype == "file" else "---",
                "type": filetype, "path": filepath.replace(explorer_location, "", 1).lstrip("/")
            }
        )

    sorted_items = [_ for _ in al_sorted_items if _["type"] == "folder"] + [_ for _ in al_sorted_items if _["type"] == "file"]  # Folders first, then files
    return render_template(
        "explorer.html",
        items = sorted_items,
        path = ("/" if fullpath == explorer_location else "") + (fullpath.replace(explorer_location, "", 1) if explorer_location != "/" else fullpath),
        extra_spacer = f"<style>td.spacer {{ padding-left: {250 + (8 * len(max([_['name'][:75] for _ in sorted_items], key = len)))}px; }}</style>"
    ), 200

@pyhttpfs.route("/stat/<path:path>")
def get_static_file(path):
    return send_file(os.path.join(pyhttpfs.static_dir, path), conditional = True)
