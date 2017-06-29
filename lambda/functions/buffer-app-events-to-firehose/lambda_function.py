import config
import base64
import json
import funnel_pb2 as funnel
import boto3

stream_name = 'temp.buffer_app_events'
stream = boto3.client('firehose')


def write_batch(b):
    stream.put_record_batch(
        DeliveryStreamName=stream_name,
        Records=b
    )


def format_date(date):
    if date:
        return date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def normalize(proto):
    d = {
        'id': proto.id,
        'user_id': proto.user_id,
        'funnel_id': proto.funnel_id,
        'funnel_event_id:': proto.funnel_event_id,
        'created_at': format_date(proto.created_at.ToDatetime())
    }

    return d


def lambda_handler(event, context):

    batch = []

    if not event['Records']:
        return

    for record in event['Records']:
        # Decode
        decoded = base64.b64decode(record['kinesis']['data'])
        data = funnel.FunnelEvent.FromString(decoded)

        value_data = normalize(data)

        record = json.dumps(value_data) + '\n'

        if len(batch) < 500:
            batch.append({'Data': record})
        else:
            write_batch(batch)
            batch = []
            batch.append({'Data': record})

    if batch:
        write_batch(batch)

    return len(event['Records'])
