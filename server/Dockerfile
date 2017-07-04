FROM grpc/python:1.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /usr/src/app/server.py
COPY buda /usr/src/app/buda

CMD ["python", "-u", "server.py"]
