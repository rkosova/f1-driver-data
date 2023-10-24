#!/bin/bash

REGISTRY_IP="10.0.40.160"
PORT="5000"

IMAGE_NAME="run_image_f1_dd"
FULL_IMAGE_REF="${REGISTRY_IP}:${PORT}/${IMAGE_NAME}:latest"

echo "Pulling docker image: "
docker pull "$FULL_IMAGE_REF"

if [ $? -eq 0 ]; then
  echo "Image successfully pulled: $FULL_IMAGE_REF"
  NAME="F1DriverData_test"
  doker run --name "$NAME" -p 9002:8080 -d "$FULL_IMAGE_REF"

  api_response = $(curl -s "${REGISTRY_IP}:9001/driver/Max%20Verstappen")

  expected_json = '{
    "championships": "2.0",
    "entries": "164.0",
    "name": "Max Verstappen",
    "nationality": "Netherlands",
    "podiums": "78.0",
    "poles": "21.0",
    "seasons": "[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]",
    "starts": "164.0",
    "wins": "36.0"
  }'

  if [ "$api_response" = "$expected_json" ]; then
    echo "Integration test passed. JSON response matches the expected."
    docker stop "$NAME"
    exit 0
  else
    echo "Integration test failed. JSON response doesn't match the expected."
    exit 1
  fi
else
  echo "Failed to pull the image: $FULL_IMAGE_REF"
  exit 1
fi
