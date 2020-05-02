#!/bin/bash
# An account and a generated token from pypi.org is needed
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*