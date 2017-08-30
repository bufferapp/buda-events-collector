FROM grpc/python:1.4

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY server.py /usr/src/app/server.py
COPY autoreload /usr/src/app/autoreload

WORKDIR /usr/src/app

CMD ["python", "-u", "server.py"]
