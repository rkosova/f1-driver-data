FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install waitress
CMD ["witress-serve", "--call", "f1_driver_data:create_app"]
