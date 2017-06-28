import grpc

from entities.visit_pb2 import Visit
import services.events_collector_pb2_grpc as collector_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = collector_grpc.EventsCollectorStub(channel)

    v = Visit(
        id='myVisit',
        uri='/welcome'
    )

    print(stub.TrackVisit(v))
