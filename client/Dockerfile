FROM python:3.6

ENV GRPC_PYTHON_VERSION 1.4.0
RUN python -m pip install --upgrade pip
RUN pip install grpcio==${GRPC_PYTHON_VERSION} grpcio-tools==${GRPC_PYTHON_VERSION}


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY client.py /usr/src/app/client.py
COPY buda /usr/src/app/buda

CMD ["python", "client.py"]
