from concurrent import futures
import time
import grpc
import boto3
import json
import logging

from buda.services.events_collector_service_pb2 import Response
import buda.services.events_collector_service_pb2_grpc as collector_grpc

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

    def CollectFunnelEvent(self, funnel_event, context):
        logger.info('Collecting funnel_event: {}'.format(funnel_event.id))
        data = funnel_event.SerializeToString()
        response = self.send_data_to_stream(data, 'buda_funnel_events')
        return Response(message=response)

    def CollectFunnel(self, funnel, context):
        logger.info('Collecting funnel: {}'.format(funnel.id))
        data = funnel.SerializeToString()

        response = self.send_data_to_stream(data, 'buda_funnels')
        return Response(message=response)


    def CollectSubscriptionCreated(self, subscription_created, context):
        logger.info('Collecting subscription created {}'.format(subscription_created.id))
        data = subscription_created.SerializeToString()

        response = self.send_data_to_stream(data, 'buda_subscription_created')
        return Response(message='')

    def CollectSubscriptionPeriodUpdated(self, subscription_period_updated, context):
        logger.info('Collecting subscription period updated {}'.format(subscription_period_updated.id))
        data = period_updated.SerializeToString()

        response = self.send_data_to_stream(data, 'buda_subscription_period_updated')
        return Response(message='')

    def CollectSubscriptionCancelled(self, subscription_cancelled, context):
        logger.info('Collecting subscription cancelled: {}'.format(subscription_cancelled.subscription_id))
        data = subscription_cancelled.SerializeToString()

        response = self.send_data_to_stream(data, 'buda_subscription_cancelled')
        return Response(message='')

    def CollectVisit(self, visit, context):
        logger.info('Collecting visit: {}'.format(visit.id))
        data = visit.SerializeToString()

        response = self.send_data_to_stream(data, 'buda_visits')
        return Response(message='')

    def CollectSignup(self, signup, context):
        logger.info('Collecting signup: {}'.format(signup.id))
        data = signup.SerializeToString()

        response = self.send_data_to_stream(data, 'buda_signups')
        return Response(message='')

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
