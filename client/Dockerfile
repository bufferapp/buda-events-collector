FROM grpc/python:1.4


COPY client.py /usr/src/app/client.py
COPY buda-python-0.3.0.tar.gz /tmp

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /usr/src/app

CMD ["python", "client.py"]
