# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AirTweet.proto
# Protobuf Python Version: 4.24.0-main
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x41irTweet.proto\x12\x08\x41irTweet\"\x9c\x01\n\x05\x45vent\x12\x1d\n\x15server_timestamp_usec\x18\x01 \x01(\x03\x12\x10\n\x08tweet_id\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0f\n\x07penalty\x18\x04 \x01(\x01\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12\x12\n\nstream_end\x18\x06 \x01(\x08\x12\x11\n\tmissed_id\x18\x07 \x03(\t\x12\r\n\x05score\x18\x08 \x01(\x03\"/\n\x06Signal\x12\x10\n\x08tweet_id\x18\x01 \x01(\t\x12\x13\n\x0bprobability\x18\x02 \x03(\x01\x42\x02H\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AirTweet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001'
  _globals['_EVENT']._serialized_start=29
  _globals['_EVENT']._serialized_end=185
  _globals['_SIGNAL']._serialized_start=187
  _globals['_SIGNAL']._serialized_end=234
# @@protoc_insertion_point(module_scope)
