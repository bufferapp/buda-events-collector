FROM grpc/python:1.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY client.py /usr/src/app/client.py
COPY buda /usr/src/app/buda

CMD ["python", "client.py"]
