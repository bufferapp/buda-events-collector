# Events Collector

A [gRPC](https://grpc.io/) server part of the [Buffer Unified Data Architecture][buda] that collects different events. The events are sent to specific Kinesis streams to be consumed later. You can check what events are supported in the [service definition][events_collector] inside [BUDA Protobufs](https://github.com/bufferapp/buda-protobufs) repository.

[buda]: https://paper.dropbox.com/doc/Buffer-Unified-Data-Architecture-Yu9JtqkwNnQOHmeFynDS3

## Usage

You can communicate with the _Events Collector_ using gRPC. Create or use a library for your prefered language and call the [available methods][events_collector]!

[events_collector]: https://github.com/bufferapp/buda-protobufs/blob/master/buda/services/events_collector.proto

## Development

Before starting, create a `.env` file inside the `server` folder containing your AWS credentials:

```
AWS_ACCESS_KEY_ID=1234567890ASDFGHJKL
AWS_SECRET_ACCESS_KEY=QWERTYUIOPASDFGHJKLZXCVBNM
AWS_DEFAULT_REGION=us-east-1
```

The main logic of the Events Collector resided under the `server.py`. If you want to run the server locally in Docker you need to run `make build && make run` inside the _server_ folder and then, in another terminal, run `make build && make run` this time inside the _client_ folder. 

## Deployment

You can deploy the collector server to Kubernetes using the YAML files located in the [`kubernetes`](kubernetes/) folder. Before creating any new resources check that you have `aws` secrets in place! 

The collector requires a Deployment and a Service. you can create both resources with `kubectl`:

- `kubectl create -f kubernetes/events-collector.deployment.yaml`
- `kubectl create -f kubernetes/events-collector.service.yaml`

If everything worked you can now communicate with it creating a client and pointing it to `event-collector:50051`. 

## Versioning

We use [Semantic Versioning](http://semver.org/) for the Docker images.
 
## Contribute

Contributions are always welcome! Please open an issue if you have questions or suggestions.

## License

MIT License Copyright (c) 2017 Buffer
