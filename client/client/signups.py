from buda.entities.signup_pb2 import Signup
from client.utils import *


def make_test_signup():
    event = Signup(
        id=new_uuid(),
        user_id=new_uuid(),
        visitor_id=new_uuid(),
        legacy_visitor_id=new_uuid(),
    )

    event.created_at.GetCurrentTime()

    return event


def run_test(stub):
    events = [make_test_signup() for i in range(100)]
    for event in events:
        stub.CollectSignup(event)
