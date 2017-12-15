from buda.entities.action_taken_pb2 import ActionTaken
from client.utils import new_uuid


def make_test_action_taken():
    event = ActionTaken(
        id=new_uuid(),
        application='my-awesome-app',
        location='awesome_page',
        action='amazing_button_clicked'
    )

    event.created_at.GetCurrentTime()
    event.metadata['userId'] = new_uuid().id
    event.metadata['foo'] = 'bar'

    return event


def run_test(stub):
    events = [make_test_action_taken() for i in range(100)]
    for event in events:
        stub.CollectActionTaken(event)
