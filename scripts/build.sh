bash scripts/clean.sh
python3 setup.py sdist bdist_wheel

pip install twine
twine upload --repository  dist/*

pip install .
