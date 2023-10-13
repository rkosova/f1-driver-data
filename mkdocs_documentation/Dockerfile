FROM python:3.10-slim
RUN pip install mkdocs
WORKDIR /app/mkdocs_documentation
COPY ./f1_driver_data .
EXPOSE 8000
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
