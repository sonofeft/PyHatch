python setup.py sdist bdist_wheel
python -m twine upload --skip-existing dist/*

rem use:  twine check dist/*  OR twine check dist/*24.tar.gz (where: 24 is current version)
