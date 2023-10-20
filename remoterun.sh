#!/bin/bash

REGISTRY_IP="10.0.40.160"
PORT="5000"

IMAGE_NAME="run_image_f1_dd"

FULL_IMAGE_REF="${REGISTRY_IP}:${REGISTRY_PORT}/${IMAGE_NAME}:latest"

echo "Pulling docker image: "
docker pull "$FULL_IMAGE_REF"

if [ $? -eq 0 ]; then
  echo "Image successfully pulled: $FULL_IMAGE_REF"
  NAME="F1DriverData_test"
  docker run --name "$NAME" -p 9001:8080 -d "$FULL_IMAGE_REF" 
  docker run --name "$NAME" -p 9001:8080
else
  echo "Failed to pull the image: $FULL_IMAGE_REF"
  exit 1
fi
