!#/bin/bash

mkdir -p build
rm build/bundle.zip
zip build/bundle.zip requirements.txt *.py **/*.py