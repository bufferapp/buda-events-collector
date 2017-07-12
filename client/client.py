import grpc
import uuid
import time
import random

from buda.entities.funnel_pb2 import Funnel
from buda.entities.funnel_event_pb2 import FunnelEvent
from buda.entities.link_pb2 import Link
from buda.entities.uuid_pb2 import Uuid

import buda.services.events_collector_pb2_grpc as collector_grpc


def new_uuid():
    return Uuid(id=uuid.uuid4().hex)


def make_test_funnel():
    funnel_id = new_uuid()
    user_id = new_uuid()

    funnel = Funnel(
        id=funnel_id,
        user_id=user_id,
        name='upgrade-path'
    )

    funnel.created_at.GetCurrentTime()
    funnel.tags['foo'] = 'bar'

    return funnel


def make_test_funnel_event(funnel):
    funnel_event_id = new_uuid()
    funnel_step_id = new_uuid()

    event = FunnelEvent(
        id=funnel_event_id,
        funnel_id=funnel.id,
        funnel_step_id=funnel_step_id,
        user_id=funnel.user_id
    )

    event.created_at.GetCurrentTime()
    event.tags['foo'] = 'bar'

    if random.random() < 0.01:
        event.funnel_end = True
        link = Link(target="subscription_events", target_id=new_uuid())
        event.links.extend([link])

    return event


if __name__ == '__main__':
    ip = 'events-collector'
    channel = grpc.insecure_channel(ip + ':50051')
    stub = collector_grpc.EventsCollectorStub(channel)

    test_funnels = [make_test_funnel() for i in range(10)]

    for funnel in test_funnels:
        stub.CollectFunnel(funnel)
        time.sleep(0.1)

    test_funnels = [random.choice(test_funnels) for i in range(len(test_funnels) * 4)]
    test_funnel_events = [make_test_funnel_event(f) for f in test_funnels]

    for event in test_funnel_events:
        stub.CollectFunnelEvent(event)
        time.sleep(0.1)
