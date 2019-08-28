#!/usr/bin/env bash

./build.sh

TAG=${1:-latest}

echo "Using tag: $TAG."

docker tag iris_eval eyra/iris_eval:$TAG
docker push eyra/iris_eval