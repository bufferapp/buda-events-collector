import os
import grpc
import time
import uuid
import buda.services.events_collector_service_pb2_grpc as collector_grpc
from buda.entities.action_taken_pb2 import ActionTaken
from buda.entities.uuid_pb2 import Uuid


if __name__ == "__main__":
    channel = grpc.insecure_channel("localhost:50051")
    stub = collector_grpc.EventsCollectorStub(channel)

    event = ActionTaken(
        id=Uuid(id=uuid.uuid4().hex),
        application="my-awesome-app",
        location="awesome_page",
        action="amazing_button_clicked",
    )
    event.created_at.GetCurrentTime()

    request = stub.CollectActionTaken(event)
