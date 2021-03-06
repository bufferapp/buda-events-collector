# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buda/entities/subscription_cancelled.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from buda.entities import uuid_pb2 as buda_dot_entities_dot_uuid__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buda/entities/subscription_cancelled.proto',
  package='buda',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*buda/entities/subscription_cancelled.proto\x12\x04\x62uda\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18\x62uda/entities/uuid.proto\"\xa1\x01\n\x15SubscriptionCancelled\x12\x16\n\x02id\x18\x01 \x01(\x0b\x32\n.buda.Uuid\x12#\n\x0fsubscription_id\x18\x02 \x01(\x0b\x32\n.buda.Uuid\x12\x1b\n\x07user_id\x18\x03 \x01(\x0b\x32\n.buda.Uuid\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,buda_dot_entities_dot_uuid__pb2.DESCRIPTOR,])




_SUBSCRIPTIONCANCELLED = _descriptor.Descriptor(
  name='SubscriptionCancelled',
  full_name='buda.SubscriptionCancelled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='buda.SubscriptionCancelled.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscription_id', full_name='buda.SubscriptionCancelled.subscription_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='buda.SubscriptionCancelled.user_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='buda.SubscriptionCancelled.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=273,
)

_SUBSCRIPTIONCANCELLED.fields_by_name['id'].message_type = buda_dot_entities_dot_uuid__pb2._UUID
_SUBSCRIPTIONCANCELLED.fields_by_name['subscription_id'].message_type = buda_dot_entities_dot_uuid__pb2._UUID
_SUBSCRIPTIONCANCELLED.fields_by_name['user_id'].message_type = buda_dot_entities_dot_uuid__pb2._UUID
_SUBSCRIPTIONCANCELLED.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['SubscriptionCancelled'] = _SUBSCRIPTIONCANCELLED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscriptionCancelled = _reflection.GeneratedProtocolMessageType('SubscriptionCancelled', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIPTIONCANCELLED,
  __module__ = 'buda.entities.subscription_cancelled_pb2'
  # @@protoc_insertion_point(class_scope:buda.SubscriptionCancelled)
  ))
_sym_db.RegisterMessage(SubscriptionCancelled)


# @@protoc_insertion_point(module_scope)
