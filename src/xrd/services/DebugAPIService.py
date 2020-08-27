# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from xrd.core import config
from xrd.core.xrdnode import xrdNode
from xrd.generated import xrddebug_pb2
from xrd.generated.xrddebug_pb2_grpc import DebugAPIServicer
from xrd.services.grpcHelper import GrpcExceptionWrapper


class DebugAPIService(DebugAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, xrdnode: xrdNode):
        self.xrdnode = xrdnode

    @GrpcExceptionWrapper(xrddebug_pb2.GetFullStateResp)
    def GetFullState(self, request: xrddebug_pb2.GetFullStateReq, context) -> xrddebug_pb2.GetFullStateResp:
        return xrddebug_pb2.GetFullStateResp(
            coinbase_state=self.xrdnode.get_address_state(config.dev.coinbase_address).pbdata,
            addresses_state=self.xrdnode.get_all_address_state()
        )
