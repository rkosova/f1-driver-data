FROM python:3.10-slim
RUN pip install mkdocs
WORKDIR /app
COPY ./mkdocs_documentation .
CMD ["mkdocs", "build"]
