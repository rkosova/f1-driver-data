#!/bin/bash
python -m venv venv
. ./venv/bin/activate
ls
pip install F1DriverData-0.1-py3-none-any.whl
pip install waitress
pip install flask

waitress-serve --call "f1_driver_data:create_app"