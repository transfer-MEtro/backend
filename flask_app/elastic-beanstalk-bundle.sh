!#/bin/bash

mkdir -p build
rm build/bundle.zip
zip build/bundle.zip requirements.txt application.py **/*.py