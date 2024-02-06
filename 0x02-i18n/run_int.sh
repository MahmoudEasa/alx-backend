#!/usr/bin/env bash

# Initialize translations with
pybabel extract -F babel.cfg -o messages.pot .

# Two dictionaries with
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr

# Compile dictionaries with
# pybabel compile -d translations

