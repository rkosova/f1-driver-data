#!/bin/bash
python -m venv venv
. ./venv/bin/activate
ls
pip install F1DriverData-0.1-py3-none-any.whl
pip install gunicorn
pip install flask

gunicorn f1_driver_data:create_app --bind 0.0.0.0:8080