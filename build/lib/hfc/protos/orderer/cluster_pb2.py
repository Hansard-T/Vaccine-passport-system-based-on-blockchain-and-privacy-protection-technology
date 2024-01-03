# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/orderer/cluster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.common import common_pb2 as hfc_dot_protos_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/orderer/cluster.proto',
  package='orderer',
  syntax='proto3',
  serialized_options=_b('\n%org.hyperledger.fabric.protos.ordererZ,github.com/hyperledger/fabric/protos/orderer'),
  serialized_pb=_b('\n hfc/protos/orderer/cluster.proto\x12\x07orderer\x1a\x1ehfc/protos/common/common.proto\"/\n\x0bStepRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"\x1f\n\x0cStepResponse\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\"`\n\rSubmitRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\x1b\n\x13last_validation_seq\x18\x02 \x01(\x04\x12!\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x10.common.Envelope\">\n\x0eSubmitResponse\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.Status\x12\x0c\n\x04info\x18\x02 \x01(\t2}\n\x07\x43luster\x12=\n\x06Submit\x12\x16.orderer.SubmitRequest\x1a\x17.orderer.SubmitResponse(\x01\x30\x01\x12\x33\n\x04Step\x12\x14.orderer.StepRequest\x1a\x15.orderer.StepResponseBU\n%org.hyperledger.fabric.protos.ordererZ,github.com/hyperledger/fabric/protos/ordererb\x06proto3')
  ,
  dependencies=[hfc_dot_protos_dot_common_dot_common__pb2.DESCRIPTOR,])




_STEPREQUEST = _descriptor.Descriptor(
  name='StepRequest',
  full_name='orderer.StepRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='orderer.StepRequest.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='orderer.StepRequest.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=77,
  serialized_end=124,
)


_STEPRESPONSE = _descriptor.Descriptor(
  name='StepResponse',
  full_name='orderer.StepResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='orderer.StepResponse.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=126,
  serialized_end=157,
)


_SUBMITREQUEST = _descriptor.Descriptor(
  name='SubmitRequest',
  full_name='orderer.SubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='orderer.SubmitRequest.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_validation_seq', full_name='orderer.SubmitRequest.last_validation_seq', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='orderer.SubmitRequest.content', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=159,
  serialized_end=255,
)


_SUBMITRESPONSE = _descriptor.Descriptor(
  name='SubmitResponse',
  full_name='orderer.SubmitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='orderer.SubmitResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='orderer.SubmitResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=257,
  serialized_end=319,
)

_SUBMITREQUEST.fields_by_name['content'].message_type = hfc_dot_protos_dot_common_dot_common__pb2._ENVELOPE
_SUBMITRESPONSE.fields_by_name['status'].enum_type = hfc_dot_protos_dot_common_dot_common__pb2._STATUS
DESCRIPTOR.message_types_by_name['StepRequest'] = _STEPREQUEST
DESCRIPTOR.message_types_by_name['StepResponse'] = _STEPRESPONSE
DESCRIPTOR.message_types_by_name['SubmitRequest'] = _SUBMITREQUEST
DESCRIPTOR.message_types_by_name['SubmitResponse'] = _SUBMITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StepRequest = _reflection.GeneratedProtocolMessageType('StepRequest', (_message.Message,), dict(
  DESCRIPTOR = _STEPREQUEST,
  __module__ = 'hfc.protos.orderer.cluster_pb2'
  # @@protoc_insertion_point(class_scope:orderer.StepRequest)
  ))
_sym_db.RegisterMessage(StepRequest)

StepResponse = _reflection.GeneratedProtocolMessageType('StepResponse', (_message.Message,), dict(
  DESCRIPTOR = _STEPRESPONSE,
  __module__ = 'hfc.protos.orderer.cluster_pb2'
  # @@protoc_insertion_point(class_scope:orderer.StepResponse)
  ))
_sym_db.RegisterMessage(StepResponse)

SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITREQUEST,
  __module__ = 'hfc.protos.orderer.cluster_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SubmitRequest)
  ))
_sym_db.RegisterMessage(SubmitRequest)

SubmitResponse = _reflection.GeneratedProtocolMessageType('SubmitResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITRESPONSE,
  __module__ = 'hfc.protos.orderer.cluster_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SubmitResponse)
  ))
_sym_db.RegisterMessage(SubmitResponse)


DESCRIPTOR._options = None

_CLUSTER = _descriptor.ServiceDescriptor(
  name='Cluster',
  full_name='orderer.Cluster',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=321,
  serialized_end=446,
  methods=[
  _descriptor.MethodDescriptor(
    name='Submit',
    full_name='orderer.Cluster.Submit',
    index=0,
    containing_service=None,
    input_type=_SUBMITREQUEST,
    output_type=_SUBMITRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Step',
    full_name='orderer.Cluster.Step',
    index=1,
    containing_service=None,
    input_type=_STEPREQUEST,
    output_type=_STEPRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLUSTER)

DESCRIPTOR.services_by_name['Cluster'] = _CLUSTER

# @@protoc_insertion_point(module_scope)