FROM python:3-slim

RUN apt-get update -qqy && \
    apt-get -qqy install wget && \
    rm -rf /var/lib/apt/lists/*

RUN GRPC_HEALTH_PROBE_VERSION=v0.2.0 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY server.py /usr/src/app/server.py
COPY buda/ /usr/src/app/buda/

WORKDIR /usr/src/app

CMD ["python", "-u", "server.py"]
