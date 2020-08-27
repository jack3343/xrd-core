# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xrdmining.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import xrd.generated.xrd_pb2 as xrd__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xrdmining.proto',
  package='xrd',
  syntax='proto3',
  serialized_pb=_b('\n\x0fxrdmining.proto\x12\x03xrd\x1a\txrd.proto\"-\n\x1bGetBlockMiningCompatibleReq\x12\x0e\n\x06height\x18\x01 \x01(\x04\"\'\n\x15GetLastBlockHeaderReq\x12\x0e\n\x06height\x18\x01 \x01(\x04\"p\n\x1cGetBlockMiningCompatibleResp\x12%\n\x0b\x62lockheader\x18\x01 \x01(\x0b\x32\x10.xrd.BlockHeader\x12)\n\rblockmetadata\x18\x02 \x01(\x0b\x32\x12.xrd.BlockMetaData\"|\n\x16GetLastBlockHeaderResp\x12\x12\n\ndifficulty\x18\x01 \x01(\x04\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x0e\n\x06reward\x18\x04 \x01(\x04\x12\x0c\n\x04hash\x18\x05 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x06 \x01(\x04\"+\n\x11GetBlockToMineReq\x12\x16\n\x0ewallet_address\x18\x01 \x01(\x0c\"\x80\x01\n\x12GetBlockToMineResp\x12\x1a\n\x12\x62locktemplate_blob\x18\x01 \x01(\t\x12\x12\n\ndifficulty\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x17\n\x0freserved_offset\x18\x04 \x01(\r\x12\x11\n\tseed_hash\x18\x05 \x01(\t\"#\n\x13SubmitMinedBlockReq\x12\x0c\n\x04\x62lob\x18\x01 \x01(\x0c\"%\n\x14SubmitMinedBlockResp\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x32\xc7\x02\n\tMiningAPI\x12_\n\x18GetBlockMiningCompatible\x12 .xrd.GetBlockMiningCompatibleReq\x1a!.xrd.GetBlockMiningCompatibleResp\x12M\n\x12GetLastBlockHeader\x12\x1a.xrd.GetLastBlockHeaderReq\x1a\x1b.xrd.GetLastBlockHeaderResp\x12\x41\n\x0eGetBlockToMine\x12\x16.xrd.GetBlockToMineReq\x1a\x17.xrd.GetBlockToMineResp\x12G\n\x10SubmitMinedBlock\x12\x18.xrd.SubmitMinedBlockReq\x1a\x19.xrd.SubmitMinedBlockRespb\x06proto3')
  ,
  dependencies=[xrd__pb2.DESCRIPTOR,])




_GETBLOCKMININGCOMPATIBLEREQ = _descriptor.Descriptor(
  name='GetBlockMiningCompatibleReq',
  full_name='xrd.GetBlockMiningCompatibleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='xrd.GetBlockMiningCompatibleReq.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=35,
  serialized_end=80,
)


_GETLASTBLOCKHEADERREQ = _descriptor.Descriptor(
  name='GetLastBlockHeaderReq',
  full_name='xrd.GetLastBlockHeaderReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='xrd.GetLastBlockHeaderReq.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=82,
  serialized_end=121,
)


_GETBLOCKMININGCOMPATIBLERESP = _descriptor.Descriptor(
  name='GetBlockMiningCompatibleResp',
  full_name='xrd.GetBlockMiningCompatibleResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blockheader', full_name='xrd.GetBlockMiningCompatibleResp.blockheader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blockmetadata', full_name='xrd.GetBlockMiningCompatibleResp.blockmetadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=123,
  serialized_end=235,
)


_GETLASTBLOCKHEADERRESP = _descriptor.Descriptor(
  name='GetLastBlockHeaderResp',
  full_name='xrd.GetLastBlockHeaderResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='xrd.GetLastBlockHeaderResp.difficulty', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='xrd.GetLastBlockHeaderResp.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='xrd.GetLastBlockHeaderResp.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='xrd.GetLastBlockHeaderResp.reward', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='xrd.GetLastBlockHeaderResp.hash', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='xrd.GetLastBlockHeaderResp.depth', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=237,
  serialized_end=361,
)


_GETBLOCKTOMINEREQ = _descriptor.Descriptor(
  name='GetBlockToMineReq',
  full_name='xrd.GetBlockToMineReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet_address', full_name='xrd.GetBlockToMineReq.wallet_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=363,
  serialized_end=406,
)


_GETBLOCKTOMINERESP = _descriptor.Descriptor(
  name='GetBlockToMineResp',
  full_name='xrd.GetBlockToMineResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocktemplate_blob', full_name='xrd.GetBlockToMineResp.blocktemplate_blob', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='xrd.GetBlockToMineResp.difficulty', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='xrd.GetBlockToMineResp.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved_offset', full_name='xrd.GetBlockToMineResp.reserved_offset', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed_hash', full_name='xrd.GetBlockToMineResp.seed_hash', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=409,
  serialized_end=537,
)


_SUBMITMINEDBLOCKREQ = _descriptor.Descriptor(
  name='SubmitMinedBlockReq',
  full_name='xrd.SubmitMinedBlockReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blob', full_name='xrd.SubmitMinedBlockReq.blob', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=539,
  serialized_end=574,
)


_SUBMITMINEDBLOCKRESP = _descriptor.Descriptor(
  name='SubmitMinedBlockResp',
  full_name='xrd.SubmitMinedBlockResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='xrd.SubmitMinedBlockResp.error', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=576,
  serialized_end=613,
)

_GETBLOCKMININGCOMPATIBLERESP.fields_by_name['blockheader'].message_type = xrd__pb2._BLOCKHEADER
_GETBLOCKMININGCOMPATIBLERESP.fields_by_name['blockmetadata'].message_type = xrd__pb2._BLOCKMETADATA
DESCRIPTOR.message_types_by_name['GetBlockMiningCompatibleReq'] = _GETBLOCKMININGCOMPATIBLEREQ
DESCRIPTOR.message_types_by_name['GetLastBlockHeaderReq'] = _GETLASTBLOCKHEADERREQ
DESCRIPTOR.message_types_by_name['GetBlockMiningCompatibleResp'] = _GETBLOCKMININGCOMPATIBLERESP
DESCRIPTOR.message_types_by_name['GetLastBlockHeaderResp'] = _GETLASTBLOCKHEADERRESP
DESCRIPTOR.message_types_by_name['GetBlockToMineReq'] = _GETBLOCKTOMINEREQ
DESCRIPTOR.message_types_by_name['GetBlockToMineResp'] = _GETBLOCKTOMINERESP
DESCRIPTOR.message_types_by_name['SubmitMinedBlockReq'] = _SUBMITMINEDBLOCKREQ
DESCRIPTOR.message_types_by_name['SubmitMinedBlockResp'] = _SUBMITMINEDBLOCKRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBlockMiningCompatibleReq = _reflection.GeneratedProtocolMessageType('GetBlockMiningCompatibleReq', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOCKMININGCOMPATIBLEREQ,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.GetBlockMiningCompatibleReq)
  ))
_sym_db.RegisterMessage(GetBlockMiningCompatibleReq)

GetLastBlockHeaderReq = _reflection.GeneratedProtocolMessageType('GetLastBlockHeaderReq', (_message.Message,), dict(
  DESCRIPTOR = _GETLASTBLOCKHEADERREQ,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.GetLastBlockHeaderReq)
  ))
_sym_db.RegisterMessage(GetLastBlockHeaderReq)

GetBlockMiningCompatibleResp = _reflection.GeneratedProtocolMessageType('GetBlockMiningCompatibleResp', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOCKMININGCOMPATIBLERESP,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.GetBlockMiningCompatibleResp)
  ))
_sym_db.RegisterMessage(GetBlockMiningCompatibleResp)

GetLastBlockHeaderResp = _reflection.GeneratedProtocolMessageType('GetLastBlockHeaderResp', (_message.Message,), dict(
  DESCRIPTOR = _GETLASTBLOCKHEADERRESP,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.GetLastBlockHeaderResp)
  ))
_sym_db.RegisterMessage(GetLastBlockHeaderResp)

GetBlockToMineReq = _reflection.GeneratedProtocolMessageType('GetBlockToMineReq', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOCKTOMINEREQ,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.GetBlockToMineReq)
  ))
_sym_db.RegisterMessage(GetBlockToMineReq)

GetBlockToMineResp = _reflection.GeneratedProtocolMessageType('GetBlockToMineResp', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOCKTOMINERESP,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.GetBlockToMineResp)
  ))
_sym_db.RegisterMessage(GetBlockToMineResp)

SubmitMinedBlockReq = _reflection.GeneratedProtocolMessageType('SubmitMinedBlockReq', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITMINEDBLOCKREQ,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.SubmitMinedBlockReq)
  ))
_sym_db.RegisterMessage(SubmitMinedBlockReq)

SubmitMinedBlockResp = _reflection.GeneratedProtocolMessageType('SubmitMinedBlockResp', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITMINEDBLOCKRESP,
  __module__ = 'xrdmining_pb2'
  # @@protoc_insertion_point(class_scope:xrd.SubmitMinedBlockResp)
  ))
_sym_db.RegisterMessage(SubmitMinedBlockResp)



_MININGAPI = _descriptor.ServiceDescriptor(
  name='MiningAPI',
  full_name='xrd.MiningAPI',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=616,
  serialized_end=943,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBlockMiningCompatible',
    full_name='xrd.MiningAPI.GetBlockMiningCompatible',
    index=0,
    containing_service=None,
    input_type=_GETBLOCKMININGCOMPATIBLEREQ,
    output_type=_GETBLOCKMININGCOMPATIBLERESP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLastBlockHeader',
    full_name='xrd.MiningAPI.GetLastBlockHeader',
    index=1,
    containing_service=None,
    input_type=_GETLASTBLOCKHEADERREQ,
    output_type=_GETLASTBLOCKHEADERRESP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockToMine',
    full_name='xrd.MiningAPI.GetBlockToMine',
    index=2,
    containing_service=None,
    input_type=_GETBLOCKTOMINEREQ,
    output_type=_GETBLOCKTOMINERESP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitMinedBlock',
    full_name='xrd.MiningAPI.SubmitMinedBlock',
    index=3,
    containing_service=None,
    input_type=_SUBMITMINEDBLOCKREQ,
    output_type=_SUBMITMINEDBLOCKRESP,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MININGAPI)

DESCRIPTOR.services_by_name['MiningAPI'] = _MININGAPI

# @@protoc_insertion_point(module_scope)
