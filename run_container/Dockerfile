FROM python:3.10-slim
WORKDIR /app

RUN pip install waitress
COPY dist .
RUN ls
RUN pip install F1DriverData*.whl

CMD ['waitress-serve', '--call', "'F1DriverData:create_app'"]