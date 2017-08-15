from concurrent import futures
import time
import grpc
import logging
from kiner.producer import KinesisProducer

from buda.services.events_collector_service_pb2 import Response
import buda.services.events_collector_service_pb2_grpc as collector_grpc

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class EventsCollectorServicer(collector_grpc.EventsCollectorServicer):

    def __init__(self):
        self.funnel_events_producer = KinesisProducer(
            'buda_funnel_events', batch_size=50, max_retries=5, threads=5
        )
        self.funnels_producer = KinesisProducer(
            'buda_funnels', batch_size=50, max_retries=5, threads=5
        )
        self.subscription_created_producer = KinesisProducer(
            'buda_subscription_created', batch_size=50,
            max_retries=5, threads=5
        )
        self.subscription_period_updated_producer = KinesisProducer(
            'buda_subscription_period_updated', batch_size=50,
            max_retries=5, threads=5
        )
        self.subscription_period_canceled_producer = KinesisProducer(
            'buda_subscription_period_canceled', batch_size=50,
            max_retries=5, threads=5
        )
        self.buda_visits_producer = KinesisProducer(
            'buda_visits', batch_size=50, max_retries=5, threads=5
        )
        self.buda_signups_producer = KinesisProducer(
            'buda_signups', batch_size=50, max_retries=5, threads=5
        )

    def CollectFunnelEvent(self, funnel_event, context):
        logger.info('Collecting funnel_event: {}'.format(funnel_event.id))
        data = funnel_event.SerializeToString()
        self.funnel_events_producer.put_record(data)
        return Response(message='OK')

    def CollectFunnel(self, funnel, context):
        logger.info('Collecting funnel: {}'.format(funnel.id))
        data = funnel.SerializeToString()
        self.funnels_producer.put_record(data)
        return Response(message='OK')

    def CollectSubscriptionCreated(self, subscription_created, context):
        logger.info('Collecting subscription created {}'.format(subscription_created.id))
        data = subscription_created.SerializeToString()
        self.subscription_created_producer.put_record(data)
        return Response(message='OK')

    def CollectSubscriptionPeriodUpdated(self, subscription_period_updated, context):
        logger.info('Collecting subscription period updated {}'.format(subscription_period_updated.id))
        data = subscription_period_updated.SerializeToString()
        self.subscription_period_updated_producer.put_record(data)
        return Response(message='OK')

    def CollectSubscriptionCancelled(self, subscription_cancelled, context):
        logger.info('Collecting subscription cancelled: {}'.format(subscription_cancelled.subscription_id))
        data = subscription_cancelled.SerializeToString()
        self.subscription_period_canceled_producer.put_record(data)
        return Response(message='OK')

    def CollectVisit(self, visit, context):
        logger.info('Collecting visit: {}'.format(visit.id))
        data = visit.SerializeToString()
        self.buda_visits_producer.put_record(data)
        return Response(message='OK')

    def CollectSignup(self, signup, context):
        logger.info('Collecting signup: {}'.format(signup.id))
        data = signup.SerializeToString()
        self.buda_signups_producer.put_record(data)
        return Response(message='OK')


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
