#!/usr/bin/env bash

./build.sh

docker tag demo_evaluation_6f85d9e6-b379-11e9-84f9-acde48001122 docker-registry.staging.eyrabenchmark.net/demo_evaluation_6f85d9e6-b379-11e9-84f9-acde48001122
docker push docker-registry.staging.eyrabenchmark.net/demo_evaluation_6f85d9e6-b379-11e9-84f9-acde48001122