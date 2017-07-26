IMAGE_NAME:=bufferapp/events-collector:client

.PHONY: all
all: run

.PHONY: run
run:
	docker run --rm -e EVENTS_COLLECTOR_HOSTNAME=localhost --net=host $(IMAGE_NAME)

.PHONY: build
build:
	 docker build . -t $(IMAGE_NAME)
