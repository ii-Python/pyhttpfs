# Copyright 2021 iiPython

# Modules
import os
import urllib.parse
from pyhttpfs import pyhttpfs
from pyhttpfs.core.args import args
from pyhttpfs.core.config import config
from pyhttpfs.core.icons import determine_icon_css
from flask import redirect, url_for, abort, send_file, render_template

# Initialization
explorer_location = args.get("l") or config.get("defaultExplorerLocation") or os.getcwd()
if explorer_location is None:
    pyhttpfs.log("[red]No explorer location set, use the `-l` flag, or a config file.", terminate = 1)

elif not os.path.isdir(explorer_location):
    pyhttpfs.log("[red]Specified explorer location does not exist.", terminate = 1)

explorer_location = os.path.abspath(explorer_location)
pyhttpfs.explorer_location = explorer_location

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
    fullpath = os.path.abspath(os.path.join(explorer_location, path))
    if explorer_location not in fullpath:
        return abort(403)

    is_root = fullpath == explorer_location

    # Handle files
    if os.path.isfile(fullpath):
        return send_file(fullpath, conditional = True)

    elif not os.path.isdir(fullpath):
        return abort(404)

    # Handle sorting items
    sorted_folders, sorted_files, max_name_length = [], [], 0
    for item in sorted((["../"] if not is_root else []) + os.listdir(fullpath)):
        filepath = os.path.join(fullpath, item)
        if os.path.islink(filepath):
            continue

        filetype = {True: "folder", False: "file"}[os.path.isdir(filepath)]
        icon = determine_icon_css(item, filetype)
        new_item = {
            "name": item, "icon": icon, "size": format_bytes(os.path.getsize(filepath)) if filetype == "file" else "---",
            "type": filetype, "path": filepath.replace(explorer_location, "", 1).lstrip("/")
        }
        if new_item["type"] == "folder":
            sorted_folders.append(new_item)

        else:
            sorted_files.append(new_item)

        # Update longest filename
        length = len(new_item["name"][:75])
        if length > max_name_length:
            max_name_length = length

    # Render item
    return render_template(
        "explorer.html",
        items = sorted_folders + sorted_files,
        path = ("/" if is_root else "") + (fullpath.replace(explorer_location, "", 1) if is_root else fullpath),
        extra_spacer = f"<style>td.spacer {{ padding-left: {250 + (8 * max_name_length)}px; }}</style>"
    ), 200

@pyhttpfs.route("/stat/<path:path>")
def get_static_file(path):
    return send_file(os.path.join(pyhttpfs.static_dir, path), conditional = True)

@pyhttpfs.errorhandler(404)
def handle_404(e):
    return render_template("errors/404.html")
