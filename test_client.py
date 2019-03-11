import os
import grpc
import time
import uuid
import buda.services.events_collector_service_pb2_grpc as collector_grpc
from buda.entities.action_taken_pb2 import ActionTaken
from buda.entities.signup_pb2 import Signup
from buda.entities.uuid_pb2 import Uuid


def new_uuid():
    return Uuid(id=uuid.uuid4().hex)


def generate_action_taken_test_event():
    event = ActionTaken(
        id=new_uuid(),
        application="my-awesome-app",
        location="awesome_page",
        action="amazing_button_clicked",
    )
    event.created_at.GetCurrentTime()

    return event


def generate_singup_test_event():
    event = Signup(
        id=new_uuid(),
        account_id=new_uuid(),
        user_id=new_uuid(),
        visitor_id=new_uuid(),
        legacy_visitor_id=new_uuid(),
    )

    event.created_at.GetCurrentTime()

    return event


if __name__ == "__main__":
    channel = grpc.insecure_channel("localhost:50051")
    stub = collector_grpc.EventsCollectorStub(channel)

    request = stub.CollectActionTaken(generate_action_taken_test_event())
    request = stub.CollectSignup(generate_singup_test_event())
