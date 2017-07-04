# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buda/entities/visit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buda.entities import utm_pb2 as buda_dot_entities_dot_utm__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buda/entities/visit.proto',
  package='buda.entities',
  syntax='proto3',
  serialized_pb=_b('\n\x19\x62uda/entities/visit.proto\x12\rbuda.entities\x1a\x17\x62uda/entities/utm.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x01\n\x05Visit\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x1f\n\x03utm\x18\x05 \x01(\x0b\x32\x12.buda.entities.Utm\x12,\n\nuser_agent\x18\x06 \x01(\x0b\x32\x18.buda.entities.UserAgent\x12\x12\n\nvisitor_id\x18\x07 \x01(\t\"-\n\tUserAgent\x12\x0f\n\x07\x62rowser\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[buda_dot_entities_dot_utm__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VISIT = _descriptor.Descriptor(
  name='Visit',
  full_name='buda.entities.Visit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='buda.entities.Visit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='buda.entities.Visit.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='buda.entities.Visit.uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='buda.entities.Visit.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utm', full_name='buda.entities.Visit.utm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='buda.entities.Visit.user_agent', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visitor_id', full_name='buda.entities.Visit.visitor_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=293,
)


_USERAGENT = _descriptor.Descriptor(
  name='UserAgent',
  full_name='buda.entities.UserAgent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='browser', full_name='buda.entities.UserAgent.browser', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='buda.entities.UserAgent.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=340,
)

_VISIT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VISIT.fields_by_name['utm'].message_type = buda_dot_entities_dot_utm__pb2._UTM
_VISIT.fields_by_name['user_agent'].message_type = _USERAGENT
DESCRIPTOR.message_types_by_name['Visit'] = _VISIT
DESCRIPTOR.message_types_by_name['UserAgent'] = _USERAGENT

Visit = _reflection.GeneratedProtocolMessageType('Visit', (_message.Message,), dict(
  DESCRIPTOR = _VISIT,
  __module__ = 'buda.entities.visit_pb2'
  # @@protoc_insertion_point(class_scope:buda.entities.Visit)
  ))
_sym_db.RegisterMessage(Visit)

UserAgent = _reflection.GeneratedProtocolMessageType('UserAgent', (_message.Message,), dict(
  DESCRIPTOR = _USERAGENT,
  __module__ = 'buda.entities.visit_pb2'
  # @@protoc_insertion_point(class_scope:buda.entities.UserAgent)
  ))
_sym_db.RegisterMessage(UserAgent)


# @@protoc_insertion_point(module_scope)
