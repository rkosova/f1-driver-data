#!/bin/bash
python -m venv venv
source venv/bin/activate
ls
pip install -r requirements.txt
pip install F1DriverData-0.1-py3-none-any.whl
pip install waitress
pip install flask

pip show F1DriverData
python -c "import f1_driver_data
print(dir(f1_driver_data))"


waitress-serve --call f1_driver_data:create_app