# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apps/common/grpc/common.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pps/common/grpc/common.proto\x12\x0b\x63ore.common\x1a\x1cgoogle/protobuf/struct.proto\"\x11\n\x0f\x44\x61taListRequest\">\n\x10\x44\x61taListResponse\x12*\n\x07results\x18\x01 \x03(\x0b\x32\x19.core.common.DataResponse\"\x90\x01\n\x0b\x44\x61taRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x12/\n\tdata_json\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x01\x88\x01\x01\x42\x0e\n\x0c_descriptionB\x0c\n\n_data_json\"\xb9\x01\n\x0c\x44\x61taResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x05 \x01(\tH\x00\x88\x01\x01\x12/\n\tdata_json\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructH\x01\x88\x01\x01\x42\x0e\n\x0c_descriptionB\x0c\n\n_data_json2W\n\x14\x44\x61taCreateController\x12?\n\x06\x43reate\x12\x18.core.common.DataRequest\x1a\x19.core.common.DataResponse\"\x00\x32[\n\x12\x44\x61taListController\x12\x45\n\x04List\x12\x1c.core.common.DataListRequest\x1a\x1d.core.common.DataListResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apps.common.grpc.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DATALISTREQUEST']._serialized_start=76
  _globals['_DATALISTREQUEST']._serialized_end=93
  _globals['_DATALISTRESPONSE']._serialized_start=95
  _globals['_DATALISTRESPONSE']._serialized_end=157
  _globals['_DATAREQUEST']._serialized_start=160
  _globals['_DATAREQUEST']._serialized_end=304
  _globals['_DATARESPONSE']._serialized_start=307
  _globals['_DATARESPONSE']._serialized_end=492
  _globals['_DATACREATECONTROLLER']._serialized_start=494
  _globals['_DATACREATECONTROLLER']._serialized_end=581
  _globals['_DATALISTCONTROLLER']._serialized_start=583
  _globals['_DATALISTCONTROLLER']._serialized_end=674
# @@protoc_insertion_point(module_scope)
