# F1 DRIVER DATA

Simple API for querying F1 driver data.

## Endpoints

`GET /driver/all`

- Gets all data

`GET /driver/all?name=<Full Driver Name>`

- Gets specified driver

`GET /driver/all?rank=top&category=<Category>&n=<Number of Drivers>`

- Gets top `n` drivers with respect to `parameter` (e.g., top 10 drivers with the most race wins)

`GET /driver/all?rank=bottom&category=<Category>&n=<Number of Drivers>`

- Gets bottom `n` drivers with respect to `parameter` (e.g., bottom 10 drivers with the most race wins)
