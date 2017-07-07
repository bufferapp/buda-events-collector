IMAGE_NAME:=bufferapp/events-collector-server:0.1.0

.PHONY: all
all: run

.PHONY: run
run:
	docker run --env-file .env -p 50051:50051 --rm $(IMAGE_NAME)

.PHONY: build
build:
	 docker build . -t $(IMAGE_NAME)

.PHONY: dev
dev:
	docker run -it --env-file .env --rm $(IMAGE_NAME) /bin/bash
