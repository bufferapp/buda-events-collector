from concurrent import futures
import time
import grpc
import boto3
import json
import logging

from services.event_collector_pb2 import Response
import services.event_collector_pb2_grpc as collector_grpc

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
    logger.info('Server initialized')

    collector_grpc.add_EventCollectorServicer_to_server(
        EventCollectorServicer(),
        server
    )
    logger.info('Servicer added')

    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info('Server started')

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
