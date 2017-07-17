FROM python:3.6

ENV GRPC_PYTHON_VERSION 1.4.0
RUN python -m pip install --upgrade pip
RUN pip install grpcio==${GRPC_PYTHON_VERSION} grpcio-tools==${GRPC_PYTHON_VERSION}

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /usr/src/app
COPY server.py /usr/src/app/server.py

CMD ["python", "-u", "server.py"]
