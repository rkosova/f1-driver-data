FROM python:3.10-slim
WORKDIR /app
RUN pip install waitress

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN mv tests/test_driverBp.py .

CMD ["pytest"]
