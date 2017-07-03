FROM grpc/python:1.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY client.py /usr/src/app/client.py
COPY services /usr/src/app/services
COPY entities /usr/src/app/entities

CMD ["python", "client.py"]
