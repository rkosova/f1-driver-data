#!/bin/bash

REGISTRY_IP="10.0.40.160"
PORT="5000"

IMAGE_NAME="run_image_f1_dd"

FULL_IMAGE_REF="${REGISTRY_IP}:${PORT}/${IMAGE_NAME}:latest"

echo "Pulling docker image: "
docker pull "$FULL_IMAGE_REF"

if [ $? -eq 0 ]; then
  echo "Image successfully pulled: $FULL_IMAGE_REF"
  NAME="F1DriverData"
  docker stop "$NAME"
  docker rm "$NAME"
  docker run --name "$NAME" -p 8082:8080 -d "$FULL_IMAGE_REF" 
else
  echo "Failed to pull the image: $FULL_IMAGE_REF"
  exit 1
fi
