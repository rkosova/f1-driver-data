FROM python:3.10-slim
WORKDIR /app
COPY ./f1_driver_data .
COPY ./requirements.txt .
COPY ./setup.py .
COPY ./app_deploy.sh .
RUN pip install build
RUN pip install -r requirements.txt
CMD ["python", "-m", "build", "--wheel"]