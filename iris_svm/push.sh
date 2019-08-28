#!/usr/bin/env bash

./build.sh

TAG=${1:-latest}

echo "Using tag: $TAG."

docker tag iris_svm eyra/iris_svm:$TAG
docker push eyra/iris_svm