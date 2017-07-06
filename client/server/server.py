from concurrent import futures
import time
import grpc
import boto3
import json
import logging

from buda.services.events_collector_pb2 import Response
import buda.services.events_collector_pb2_grpc as collector_grpc

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class EventsCollectorServicer(collector_grpc.EventsCollectorServicer):

    def __init__(self):
        self.client = boto3.client('kinesis')

    def send_data_to_stream(self, data, stream_name):
        response = self.client.put_record(
            StreamName=stream_name,
            Data=data,
            PartitionKey='string'
        )
        return json.dumps(response)

    def TrackFunnelEvent(self, funnel_event, context):
        print('Tracking funnel_event: {}'.format(funnel_event.id))
        data = funnel_event.SerializeToString()
        response = self.send_data_to_stream(data, 'buffer_app_events')
        return Response(message=response)

    def TrackFunnel(self, funnel, context):
        print('Tracking funnel: {}'.format(funnel.id))
        data = funnel.SerializeToString()

        response = self.send_data_to_stream(data, 'buffer_app_events')
        return Response(message=response)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    logger.info('Server initialized')

    collector_grpc.add_EventsCollectorServicer_to_server(
        EventsCollectorServicer(),
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
