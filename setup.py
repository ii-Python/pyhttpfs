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
def find_packages(dir):
    packs = []
    for p, _, __ in os.walk(dir):
        path = p.replace("\\", "/").replace("/", ".").replace(dir + ".", "")
        if "egg-info" not in path and "__pycache__" not in path:
            if path != dir:
                packs.append(path)

    return packs

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
    version = get_version("src/pyhttpfs/__init__.py"),
    description = "Fast and efficient filesystem browser",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "iiPython",
    author_email = "ben@iipython.cf",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords = "http filesystem browser fileserver httpserver",
    package_dir = {"pyhttpfs": "src/pyhttpfs"},
    package_data = {"pyhttpfs": ["templates/*", "assets/*", "assets/static/*"]},
    packages = find_packages("src"),
    python_requires = ">=3.6, <4",
    entry_points = """
        [console_scripts]
        pyhttpfs=pyhttpfs.__main__:main
    """
)
