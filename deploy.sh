#!/usr/bin/bash

poetry export --without-hashes --format=requirements.txt | sed -e 's/;.*//' >example/requirements.txt
echo "requirements.txt generated from pyproject.toml"

cd example
chalice deploy
