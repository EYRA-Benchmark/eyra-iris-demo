#!/usr/bin/env bash

./build.sh

docker run --rm --memory=4g -v $(pwd)/data/input/:/data/input/ -v $(pwd)/data/output/:/data/output/ demo_evaluation_6f85d9e6-b379-11e9-84f9-acde48001122