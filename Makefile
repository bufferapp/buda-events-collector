python:
	protoc \
	--python_out . \
	--proto_path protobufs \
	protobufs/entities/utm.proto \
	protobufs/entities/visit.proto \

	python -m grpc_tools.protoc \
		--python_out . \
		--grpc_python_out . \
		--proto_path protobufs \
		protobufs/services/events_collector.proto

clean:
	rm -rf entities services
