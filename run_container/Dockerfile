FROM python:3.10-slim
WORKDIR /app

RUN pip install waitress
COPY /home/svcgithub/dist .
RUN pip install F1DriverData.whl