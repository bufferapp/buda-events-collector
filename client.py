import grpc

from entities.funnel_pb2 import FunnelEvent
import services.event_collector_pb2_grpc as collector_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = collector_grpc.EventCollectorStub(channel)

    v = FunnelEvent(
        id='funnel_id',
        user_id='user_id'
    )

    print(stub.TrackFunnelEvent(v))
