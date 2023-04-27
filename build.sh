#!/usr/bin/env bash

set -o errexit  # exit on error

poetry install

pip install -r requirements.txt