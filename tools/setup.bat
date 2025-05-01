:: Requires twine~=4.0.2 to be installed
:: This script will build your package and attempt to upload it to pypi using the metadata in setup.py

:: Note: PyPI no longer accepts direct username/password authentication via this method. Instead, create an API token for your
:: PyPI account and use that for authentication. For more information, refer to https://stackoverflow.com/questions/77809196/

cd ..
python setup.py sdist
twine upload dist/*

pause
