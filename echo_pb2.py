# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\necho.proto\x12\x04\x65\x63ho\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\tEchoReply\x12\x0f\n\x07message\x18\x01 \x01(\t25\n\x04\x45\x63ho\x12-\n\x05Reply\x12\x11.echo.EchoRequest\x1a\x0f.echo.EchoReply\"\x00\x62\x06proto3')



_ECHOREQUEST = DESCRIPTOR.message_types_by_name['EchoRequest']
_ECHOREPLY = DESCRIPTOR.message_types_by_name['EchoReply']
EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoReply = _reflection.GeneratedProtocolMessageType('EchoReply', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREPLY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoReply)
  })
_sym_db.RegisterMessage(EchoReply)

_ECHO = DESCRIPTOR.services_by_name['Echo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ECHOREQUEST._serialized_start=20
  _ECHOREQUEST._serialized_end=50
  _ECHOREPLY._serialized_start=52
  _ECHOREPLY._serialized_end=80
  _ECHO._serialized_start=82
  _ECHO._serialized_end=135
# @@protoc_insertion_point(module_scope)