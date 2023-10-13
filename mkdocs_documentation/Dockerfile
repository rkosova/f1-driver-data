FROM python:3.10-slim
RUN pip install mkdocs
WORKDIR /app
COPY ./f1_driver_data .
CMD ["mkdocs", "build"]
