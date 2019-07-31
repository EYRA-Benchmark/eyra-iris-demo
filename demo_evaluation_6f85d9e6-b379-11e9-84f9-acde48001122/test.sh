#!/usr/bin/env bash

./build.sh

docker run --rm --memory=4g -v $(pwd)/data/input/:/input/ -v $(pwd)/data/output/:/output/ demo_evaluation_6f85d9e6-b379-11e9-84f9-acde48001122