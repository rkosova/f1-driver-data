FROM python:3.10-slim
WORKDIR /app
COPY ./f1_driver_data .
COPY ./requirements.txt .
COPY ./setup.py .
RUN pip install build
RUN pip install -r requirements.txt
CMD ["python3", "-m", "build", "--wheel"]