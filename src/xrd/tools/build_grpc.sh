#!/usr/bin/env bash
pushd . > /dev/null
cd $( dirname "${BASH_SOURCE[0]}" )
cd ..

python -m grpc_tools.protoc -I=xrd/protos --python_out=xrd/generated --grpc_python_out=xrd/generated xrd/protos/xrd.proto
python -m grpc_tools.protoc -I=xrd/protos/xrd.proto -I=xrd/protos --python_out=xrd/generated --grpc_python_out=xrd/generated xrd/protos/xrdlegacy.proto
python -m grpc_tools.protoc -I=xrd/protos --python_out=xrd/generated --grpc_python_out=xrd/generated xrd/protos/xrdbase.proto
python -m grpc_tools.protoc -I=xrd/protos --python_out=xrd/generated --grpc_python_out=xrd/generated xrd/protos/xrdmining.proto

# Patch import problem in generated code
sed -i 's|import xrd_pb2 as xrd__pb2|import xrd.generated.xrd_pb2 as xrd__pb2|g' xrd/generated/xrd_pb2_grpc.py
sed -i 's|import xrd_pb2 as xrd__pb2|import xrd.generated.xrd_pb2 as xrd__pb2|g' xrd/generated/xrdlegacy_pb2.py
sed -i 's|import xrd_pb2 as xrd__pb2|import xrd.generated.xrd_pb2 as xrd__pb2|g' xrd/generated/xrdmining_pb2.py

sed -i 's|import xrdlegacy_pb2 as xrdlegacy__pb2|import xrd.generated.xrdlegacy_pb2 as xrdlegacy__pb2|g' xrd/generated/xrdlegacy_pb2_grpc.py
sed -i 's|import xrdbase_pb2 as xrdbase__pb2|import xrd.generated.xrdbase_pb2 as xrdbase__pb2|g' xrd/generated/xrdbase_pb2_grpc.py
sed -i 's|import xrdmining_pb2 as xrdmining__pb2|import xrd.generated.xrdmining_pb2 as xrdmining__pb2|g' xrd/generated/xrdmining_pb2_grpc.py

find xrd/generated -name '*.py'|grep -v migrations|xargs autoflake --in-place

#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/xrd/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=markdown,proto.md
#
#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/xrd/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=html,index.html

popd > /dev/null
