
.PHONY: python
python:
	protoc \
	--python_out . \
	--proto_path protobufs \
	protobufs/entities/utm.proto \
	protobufs/entities/funnel.proto \

	python -m grpc_tools.protoc \
		--python_out . \
		--grpc_python_out . \
		--proto_path protobufs \
		protobufs/services/events_collector.proto

.PHONY: clean
clean:
	rm -rf entities services
