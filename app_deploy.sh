#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install F1DriverData-0.1-py3-none-any.whl
pip install waitress
pip install flask

python -c "import f1_driver_data
print(dir(f1_driver_data))"

waitress-serve --call f1_driver_data:create_app
