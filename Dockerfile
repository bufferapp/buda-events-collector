FROM python:3-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY server.py /usr/src/app/server.py

WORKDIR /usr/src/app

CMD ["python", "-u", "server.py"]
