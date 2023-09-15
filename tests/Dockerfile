FROM python:3.10-slim
WORKDIR /app
RUN pip install waitress

COPY .. .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["ls -R"]
CMD ["pytest"]
