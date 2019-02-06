import os
import grpc
import time
import buda.services.events_collector_service_pb2_grpc as collector_grpc
from client import signins


def get_stub(ip):
    channel = grpc.insecure_channel(ip + ':50051')
    return collector_grpc.EventsCollectorStub(channel)


if __name__ == '__main__':
    ip = os.environ.get('EVENTS_COLLECTOR_HOSTNAME', 'events-collector')
    stub = get_stub(ip)

    retries = 0
    success = False
    while not success:
        try:
            signins.run_test(stub)
            success = True
        except grpc._channel._Rendezvous as e:
            print(
                "Error connecting to server. Exponentially backing off... {}", e)
            backoff = min(0.0625 * 2 ** retries, 1.0)
            print("Sleeping for {} before retrying request...".format(backoff))
            retries += 1
            time.sleep(backoff)
            continue
