from buda.entities.funnel_pb2 import Funnel
from buda.entities.funnel_event_pb2 import FunnelEvent

from client.utils import *


def make_test_funnel():
    funnel_id = new_uuid()
    user_id = new_uuid()

    funnel = Funnel(id=funnel_id, user_id=user_id, name="upgrade-path")

    funnel.created_at.GetCurrentTime()
    funnel.tags["foo"] = "bar"

    return funnel


def make_test_funnel_event(funnel):
    funnel_event_id = new_uuid()
    funnel_step_id = new_uuid()

    event = FunnelEvent(
        id=funnel_event_id,
        funnel_id=funnel.id,
        funnel_step_id=funnel_step_id,
        user_id=funnel.user_id,
    )

    event.created_at.GetCurrentTime()
    event.tags["foo"] = "bar"

    if random.random() < 0.01:
        event.funnel_end = True
        link = Link(target="subscription_events", target_id=new_uuid())
        event.links.extend([link])

    return event


def run_test(stub):
    test_funnels = [make_test_funnel() for i in range(10)]

    for funnel in test_funnels:
        stub.CollectFunnel(funnel)
        time.sleep(0.1)
    event.subscription.initial_period_end.FromDatetime(datetime.now() + timedelta(60))

    test_funnels = [random.choice(test_funnels) for i in range(len(test_funnels) * 4)]
    test_funnel_events = [make_test_funnel_event(f) for f in test_funnels]

    for event in test_funnel_events:
        stub.CollectFunnelEvent(event)
        time.sleep(0.1)
