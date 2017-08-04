FROM grpc/python:1.4


COPY $PWD /usr/src/app/

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /usr/src/app

CMD ["python", "client.py"]
