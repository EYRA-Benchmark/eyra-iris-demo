#!/usr/bin/env bash

./build.sh

docker run --rm --memory=4g -v $(pwd)/data/input/:/input/ -v $(pwd)/data/output/:/output/ demo_submission_5f2d4700-b379-11e9-af77-acde48001122