#!/usr/bin/python3
import os
import subprocess

show = subprocess.run(["pip", "show", "pyhttpfs"], stdout = subprocess.PIPE).stdout.decode("UTF-8")
location = show.split("Location: ")[1].split("\n")[0]

subprocess.run(["bash", "scripts/build.sh"])
subprocess.run(["pip", "install", "."])

subprocess.run(["code", os.path.join(location, "pyhttpfs")])
