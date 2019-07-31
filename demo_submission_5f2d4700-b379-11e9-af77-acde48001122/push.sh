#!/usr/bin/env bash

./build.sh

docker tag demo_submission_5f2d4700-b379-11e9-af77-acde48001122 docker-registry.staging.eyrabenchmark.net/demo_submission_5f2d4700-b379-11e9-af77-acde48001122
docker push docker-registry.staging.eyrabenchmark.net/demo_submission_5f2d4700-b379-11e9-af77-acde48001122