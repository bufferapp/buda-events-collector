# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buda/entities/payment_terms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='buda/entities/payment_terms.proto',
  package='buda',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!buda/entities/payment_terms.proto\x12\x04\x62uda*<\n\x0cPaymentTerms\x12\x14\n\x10\x44UE_UPON_RECEIPT\x10\x00\x12\n\n\x06NET_30\x10\x01\x12\n\n\x06NET_60\x10\x02\x62\x06proto3')
)

_PAYMENTTERMS = _descriptor.EnumDescriptor(
  name='PaymentTerms',
  full_name='buda.PaymentTerms',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DUE_UPON_RECEIPT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NET_30', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NET_60', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=43,
  serialized_end=103,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTTERMS)

PaymentTerms = enum_type_wrapper.EnumTypeWrapper(_PAYMENTTERMS)
DUE_UPON_RECEIPT = 0
NET_30 = 1
NET_60 = 2


DESCRIPTOR.enum_types_by_name['PaymentTerms'] = _PAYMENTTERMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
