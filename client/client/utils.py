import os
import grpc
import uuid
import time
import random
from datetime import datetime
from datetime import timedelta
from buda.entities.uuid_pb2 import Uuid


def new_uuid():
    return Uuid(id=uuid.uuid4().hex)


def send_test_events(maker, method, n=100):
    events = [maker() for i in range(n)]

    for event in events:
        method(event)
        time.sleep(0.1)
    return events


def send_test_events_from_list(events, maker, method):
    for event in events:
        event = maker(event)
        method(event)
        time.sleep(0.1)
    return events
