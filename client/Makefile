IMAGE_NAME:=davidgasquez/events-collector-client:0.1.0

.PHONY: all
all: run

.PHONY: run
run:
	docker run -d --net=host --rm $(IMAGE_NAME)

.PHONY: build
build:
	 docker build . -t $(IMAGE_NAME)
