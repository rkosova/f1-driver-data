# F1 DRIVER DATA

Simple API for querying F1 driver data.

## Endpoints

`GET /driver/all`

- Gets all data

`GET /driver/all?name=<Full Driver Name>`

- Gets specified driver

`GET /driver/

- Gets top `n` drivers with respect to `parameter` (e.g., top 10 drivers with the most race wins)

`GET /driver/bottom/{n}{parameter}`

- Gets bottom `n` drivers with respect to `parameter` (e.g., bottom 10 drivers with the most race wins)
