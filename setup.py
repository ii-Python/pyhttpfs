# Modules
import os
import codecs
import pathlib
import os.path
from setuptools import setup

# Grab our current path
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding = "utf-8")

# Package finder
def find_packages(dir_: str) -> list:
    packs = []
    for p, _, __ in os.walk(dir_):
        path = p.replace("\\", "/").replace("/", ".").replace(dir_ + ".", "")
        if "egg-info" not in path and "__pycache__" not in path:
            if path != dir_:
                packs.append(path)

    return packs

def find_data_dirs(dir_: str) -> list:
    dirs = []
    for p, _, f in os.walk(dir_):
        name = p.replace(dir_, "", 1).lstrip("/")
        if not name:
            continue

        elif ".egg-info" in name or "__pycache__" in name:
            continue

        has_code = False
        for file in f:
            if file.endswith(".py"):
                has_code = True

        if has_code:
            continue

        dirs.append(name.rstrip("/") + "/*")

    return dirs

# Handle versions (https://github.com/pypa/pip/blob/main/setup.py#L11)
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = "\"" if "\"" in line else "'"
            return line.split(delim)[1]

    else:
        raise RuntimeError("Unable to find version string.")

# Handle setup
setup(
    name = "pyhttpfs",
    url = "https://github.com/ii-Python/pyhttpfs",
    version = get_version("src/pyhttpfs/__init__.py"),
    description = "Fast and efficient filesystem browser",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "iiPython",
    author_email = "ben@iipython.cf",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent"
    ],
    keywords = "http filesystem browser fileserver httpserver",
    package_dir = {"pyhttpfs": "src/pyhttpfs"},
    package_data = {"pyhttpfs": find_data_dirs("src/pyhttpfs")},
    packages = find_packages("src"),
    entry_points = """
        [console_scripts]
        pyhttpfs=pyhttpfs.__main__:main
    """,
    python_requires = ">=3.7, <4",
    license_files = ("LICENSE.txt",),
    install_requires = open("reqs.txt", "r").read().splitlines(),
    license = "MIT",
    project_urls = {
        "Source": "https://github.com/ii-Python/pyhttpfs/",
        "Bug Reports": "https://github.com/ii-Python/pyhttpfs/issues"
    }
)
