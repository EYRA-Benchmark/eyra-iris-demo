FROM python:3.7-slim

RUN mkdir -p /opt/algorithm /input /output

WORKDIR /opt/algorithm

COPY requirements.txt /opt/algorithm/
RUN python -m pip install -r requirements.txt

ADD algorithm_src /opt/algorithm/

ENTRYPOINT "python" "-m" "run_submission"
