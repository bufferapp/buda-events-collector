from concurrent import futures
import time
import grpc
import boto3
import json

from services.event_collector_pb2 import Response
import services.event_collector_pb2_grpc as collector_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class EventCollectorServicer(collector_grpc.EventCollectorServicer):

    def __init__(self):
        self.client = boto3.client('kinesis')

    def send_data_to_stream(self, data, stream_name):
        response = self.client.put_record(
            StreamName=stream_name,
            Data=data,
            PartitionKey='string'
        )
        return response

    def TrackFunnelEvent(self, visit, context):
        print('Tracking visit: {}'.format(visit.id))
        data = visit.SerializeToString()
        response = self.send_data_to_stream(data, 'buffer_app_events')
        return Response(message=json.dumps(response))


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    collector_grpc.add_EventCollectorServicer_to_server(
        EventCollectorServicer(),
        server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
