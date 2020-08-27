# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
import traceback
import os
from statistics import variance, mean

from pyxrdlib.pyxrdlib import hstr2bin, xrdHelper, xrdDescriptor

from xrd.core import config
from xrd.core.AddressState import AddressState
from xrd.core.misc import logger
from xrd.core.xrdnode import xrdNode
from xrd.core.txs.Transaction import Transaction, CODEMAP
from xrd.generated import xrd_pb2
from xrd.generated.xrd_pb2_grpc import PublicAPIServicer
from xrd.services.grpcHelper import GrpcExceptionWrapper


class PublicAPIService(PublicAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    # TODO: Separate the Service from the node model
    def __init__(self, xrdnode: xrdNode):
        self.xrdnode = xrdnode

    @GrpcExceptionWrapper(xrd_pb2.GetAddressFromPKResp)
    def GetAddressFromPK(self, request: xrd_pb2.GetAddressFromPKReq, context) -> xrd_pb2.GetAddressFromPKResp:
        return xrd_pb2.GetAddressFromPKResp(address=bytes(xrdHelper.getAddress(request.pk)))

    @GrpcExceptionWrapper(xrd_pb2.GetPeersStatResp)
    def GetPeersStat(self, request: xrd_pb2.GetPeersStatReq, context) -> xrd_pb2.GetPeersStatResp:
        peers_stat_resp = xrd_pb2.GetPeersStatResp()
        peers_stat = self.xrdnode.get_peers_stat()

        for stat in peers_stat:
            peers_stat_resp.peers_stat.extend([stat])

        return peers_stat_resp

    @GrpcExceptionWrapper(xrd_pb2.IsSlaveResp)
    def IsSlave(self, request: xrd_pb2.IsSlaveReq, context) -> xrd_pb2.IsSlaveResp:
        return xrd_pb2.IsSlaveResp(result=self.xrdnode.is_slave(request.master_address, request.slave_pk))

    @GrpcExceptionWrapper(xrd_pb2.GetNodeStateResp)
    def GetNodeState(self, request: xrd_pb2.GetNodeStateReq, context) -> xrd_pb2.GetNodeStateResp:
        return xrd_pb2.GetNodeStateResp(info=self.xrdnode.get_node_info())

    @GrpcExceptionWrapper(xrd_pb2.GetKnownPeersResp)
    def GetKnownPeers(self, request: xrd_pb2.GetKnownPeersReq, context) -> xrd_pb2.GetKnownPeersResp:
        response = xrd_pb2.GetKnownPeersResp()
        response.node_info.CopyFrom(self.xrdnode.get_node_info())
        response.known_peers.extend([xrd_pb2.Peer(ip=p) for p in self.xrdnode.peer_manager.known_peer_addresses])

        return response

    @GrpcExceptionWrapper(xrd_pb2.GetStatsResp)
    def GetStats(self, request: xrd_pb2.GetStatsReq, context) -> xrd_pb2.GetStatsResp:
        response = xrd_pb2.GetStatsResp()
        response.node_info.CopyFrom(self.xrdnode.get_node_info())

        response.epoch = self.xrdnode.epoch
        response.uptime_network = self.xrdnode.uptime_network
        response.block_last_reward = self.xrdnode.block_last_reward
        response.coins_total_supply = int(self.xrdnode.coin_supply_max)
        response.coins_emitted = int(self.xrdnode.coin_supply)

        response.block_time_mean = 0
        response.block_time_sd = 0

        if request.include_timeseries:
            tmp = list(self.xrdnode.get_block_timeseries(config.dev.block_timeseries_size))
            response.block_timeseries.extend(tmp)
            if len(tmp) > 2:
                vals = [v.time_last for v in tmp[1:]]
                response.block_time_mean = int(mean(vals))
                response.block_time_sd = int(variance(vals) ** 0.5)
        return response

    @GrpcExceptionWrapper(xrd_pb2.GetChainStatsResp)
    def GetChainStats(self, request: xrd_pb2.GetChainStatsReq, context) -> xrd_pb2.GetChainStatsResp:
        response = xrd_pb2.GetChainStatsResp()
        for (path, dirs, files) in os.walk(config.user.data_dir + "/state"):
            for f in files:
                filename = os.path.join(path, f)
                response.state_size += os.path.getsize(filename)

        response.state_size_mb = str(response.state_size / (1024 * 1024))
        response.state_size_gb = str(response.state_size / (1024 * 1024 * 1024))
        return response

    @GrpcExceptionWrapper(xrd_pb2.ParseAddressResp)
    def ParseAddress(self, request: xrd_pb2.ParseAddressReq, context) -> xrd_pb2.ParseAddressResp:
        response = xrd_pb2.ParseAddressResp()
        response.is_valid = xrdHelper.addressIsValid(request.address)
        descriptor = xrdDescriptor.fromBytes(request.address[:3])
        hf_dict = {0: 'SHA2-256', 1: 'SHAKE-128', 2: 'SHAKE-256', 3: 'RESERVED'}
        ss_dict = {0: 'XMSS', 1: 'XMSS-MT'}
        af_dict = {0: 'SHA2-256', 1: 'RESERVED', 3: 'RESERVED'}
        response.desc.hash_function = hf_dict[descriptor.getHashFunction()]
        response.desc.tree_height = descriptor.getHeight()
        response.desc.signatures = 2**response.desc.tree_height
        response.desc.signature_scheme = ss_dict[descriptor.getSignatureType()]
        response.desc.address_format = af_dict[descriptor.getAddrFormatType()]
        return response

    @GrpcExceptionWrapper(xrd_pb2.GetAddressStateResp)
    def GetAddressState(self, request: xrd_pb2.GetAddressStateReq, context) -> xrd_pb2.GetAddressStateResp:
        address_state = self.xrdnode.get_address_state(request.address)
        return xrd_pb2.GetAddressStateResp(state=address_state.pbdata)

    @GrpcExceptionWrapper(xrd_pb2.GetOptimizedAddressStateResp)
    def GetOptimizedAddressState(self,
                                 request: xrd_pb2.GetAddressStateReq,
                                 context) -> xrd_pb2.GetOptimizedAddressStateResp:
        address_state = self.xrdnode.get_optimized_address_state(request.address)
        return xrd_pb2.GetOptimizedAddressStateResp(state=address_state.pbdata)

    @GrpcExceptionWrapper(xrd_pb2.GetMultiSigAddressStateResp)
    def GetMultiSigAddressState(self,
                                request: xrd_pb2.GetMultiSigAddressStateReq,
                                context) -> xrd_pb2.GetMultiSigAddressStateResp:
        multi_sig_address_state = self.xrdnode.get_multi_sig_address_state(request.address)
        if multi_sig_address_state is None:
            return xrd_pb2.GetMultiSigAddressStateResp()
        return xrd_pb2.GetMultiSigAddressStateResp(state=multi_sig_address_state.pbdata)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def TransferCoins(self, request: xrd_pb2.TransferCoinsReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] TransferCoins")
        tx = self.xrdnode.create_send_tx(addrs_to=request.addresses_to,
                                         amounts=request.amounts,
                                         message_data=request.message_data,
                                         fee=request.fee,
                                         xmss_pk=request.xmss_pk,
                                         master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.PushTransactionResp)
    def PushTransaction(self, request: xrd_pb2.PushTransactionReq, context) -> xrd_pb2.PushTransactionResp:
        logger.debug("[PublicAPI] PushTransaction")
        answer = xrd_pb2.PushTransactionResp()

        try:
            tx = Transaction.from_pbdata(request.transaction_signed)
            tx.update_txhash()

            # FIXME: Full validation takes too much time. At least verify there is a signature
            # the validation happens later in the tx pool
            if len(tx.signature) > 1000:
                self.xrdnode.submit_send_tx(tx)
                answer.error_code = xrd_pb2.PushTransactionResp.SUBMITTED
                answer.tx_hash = tx.txhash
            else:
                answer.error_description = 'Signature too short'
                answer.error_code = xrd_pb2.PushTransactionResp.VALIDATION_FAILED

        except Exception as e:
            error_str = traceback.format_exception(None, e, e.__traceback__)
            answer.error_description = str(''.join(error_str))
            answer.error_code = xrd_pb2.PushTransactionResp.ERROR

        return answer

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetMultiSigCreateTxn(self, request: xrd_pb2.MultiSigCreateTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetMultiSigCreateTxnReq")
        tx = self.xrdnode.create_multi_sig_txn(signatories=request.signatories,
                                               weights=request.weights,
                                               threshold=request.threshold,
                                               fee=request.fee,
                                               xmss_pk=request.xmss_pk,
                                               master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetMultiSigSpendTxn(self, request: xrd_pb2.MultiSigSpendTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetMultiSigSpendTxnReq")
        tx = self.xrdnode.create_multi_sig_spend_txn(multi_sig_address=request.multi_sig_address,
                                                     addrs_to=request.addrs_to,
                                                     amounts=request.amounts,
                                                     expiry_block_number=request.expiry_block_number,
                                                     fee=request.fee,
                                                     xmss_pk=request.xmss_pk,
                                                     master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetMultiSigVoteTxn(self, request: xrd_pb2.MultiSigVoteTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetMultiSigSpendTxnReq")
        tx = self.xrdnode.create_multi_sig_vote_txn(shared_key=request.shared_key,
                                                    unvote=request.unvote,
                                                    fee=request.fee,
                                                    xmss_pk=request.xmss_pk,
                                                    master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetMessageTxn(self, request: xrd_pb2.MessageTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetMessageTxn")
        tx = self.xrdnode.create_message_txn(message_hash=request.message,
                                             addr_to=request.addr_to,
                                             fee=request.fee,
                                             xmss_pk=request.xmss_pk,
                                             master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetTokenTxn(self, request: xrd_pb2.TokenTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetTokenTxn")
        tx = self.xrdnode.create_token_txn(symbol=request.symbol,
                                           name=request.name,
                                           owner=request.owner,
                                           decimals=request.decimals,
                                           initial_balances=request.initial_balances,
                                           fee=request.fee,
                                           xmss_pk=request.xmss_pk,
                                           master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetTransferTokenTxn(self, request: xrd_pb2.TransferTokenTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetTransferTokenTxn")
        bin_token_txhash = bytes(hstr2bin(request.token_txhash.decode()))
        tx = self.xrdnode.create_transfer_token_txn(addrs_to=request.addresses_to,
                                                    token_txhash=bin_token_txhash,
                                                    amounts=request.amounts,
                                                    fee=request.fee,
                                                    xmss_pk=request.xmss_pk,
                                                    master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetSlaveTxn(self, request: xrd_pb2.SlaveTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetSlaveTxn")
        tx = self.xrdnode.create_slave_tx(slave_pks=request.slave_pks,
                                          access_types=request.access_types,
                                          fee=request.fee,
                                          xmss_pk=request.xmss_pk,
                                          master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.TransferCoinsResp)
    def GetLatticeTxn(self, request: xrd_pb2.LatticeTxnReq, context) -> xrd_pb2.TransferCoinsResp:
        logger.debug("[PublicAPI] GetLatticeTxn")
        tx = self.xrdnode.create_lattice_tx(pk1=request.pk1,
                                            pk2=request.pk2,
                                            pk3=request.pk3,
                                            fee=request.fee,
                                            xmss_pk=request.xmss_pk,
                                            master_addr=request.master_addr)

        extended_transaction_unsigned = xrd_pb2.TransactionExtended(tx=tx.pbdata,
                                                                    addr_from=tx.addr_from,
                                                                    size=tx.size)
        return xrd_pb2.TransferCoinsResp(extended_transaction_unsigned=extended_transaction_unsigned)

    @GrpcExceptionWrapper(xrd_pb2.GetObjectResp)
    def GetObject(self, request: xrd_pb2.GetObjectReq, context) -> xrd_pb2.GetObjectResp:
        logger.debug("[PublicAPI] GetObject")
        answer = xrd_pb2.GetObjectResp()
        answer.found = False

        # FIXME: We need a unified way to access and validate data.
        query = bytes(request.query)  # query will be as a string, if Q is detected convert, etc.

        try:
            if AddressState.address_is_valid(query):
                if self.xrdnode.get_address_is_used(query):
                    address_state = self.xrdnode.get_optimized_address_state(query)
                    if address_state is not None:
                        answer.found = True
                        answer.address_state.CopyFrom(address_state.pbdata)
                        return answer
        except ValueError:
            pass

        transaction_block_number = self.xrdnode.get_transaction(query)
        transaction = None
        blockheader = None
        if transaction_block_number:
            transaction, block_number = transaction_block_number
            answer.found = True
            block = self.xrdnode.get_block_from_index(block_number)
            blockheader = block.blockheader.pbdata
            timestamp = block.blockheader.timestamp
        else:
            transaction_timestamp = self.xrdnode.get_unconfirmed_transaction(query)
            if transaction_timestamp:
                transaction, timestamp = transaction_timestamp
                answer.found = True

        if transaction:
            txextended = xrd_pb2.TransactionExtended(header=blockheader,
                                                     tx=transaction.pbdata,
                                                     addr_from=transaction.addr_from,
                                                     size=transaction.size,
                                                     timestamp_seconds=timestamp)
            answer.transaction.CopyFrom(txextended)
            return answer

        # NOTE: This is temporary, indexes are accepted for blocks
        try:
            block = self.xrdnode.get_block_from_hash(query)
            if block is None or (block.block_number == 0 and block.prev_headerhash != config.user.genesis_prev_headerhash):
                query_str = query.decode()
                query_index = int(query_str)
                block = self.xrdnode.get_block_from_index(query_index)
                if not block:
                    return answer

            answer.found = True
            block_extended = xrd_pb2.BlockExtended()
            block_extended.header.CopyFrom(block.blockheader.pbdata)
            block_extended.size = block.size
            for transaction in block.transactions:
                tx = Transaction.from_pbdata(transaction)
                extended_tx = xrd_pb2.TransactionExtended(tx=transaction,
                                                          addr_from=tx.addr_from,
                                                          size=tx.size,
                                                          timestamp_seconds=block.blockheader.timestamp)
                block_extended.extended_transactions.extend([extended_tx])
            answer.block_extended.CopyFrom(block_extended)
            return answer
        except Exception:
            pass

        return answer

    @GrpcExceptionWrapper(xrd_pb2.GetLatestDataResp)
    def GetLatestData(self, request: xrd_pb2.GetLatestDataReq, context) -> xrd_pb2.GetLatestDataResp:
        logger.debug("[PublicAPI] GetLatestData")
        response = xrd_pb2.GetLatestDataResp()

        all_requested = request.filter == xrd_pb2.GetLatestDataReq.ALL
        quantity = min(request.quantity, self.MAX_REQUEST_QUANTITY)

        if all_requested or request.filter == xrd_pb2.GetLatestDataReq.BLOCKHEADERS:
            result = []
            for blk in self.xrdnode.get_latest_blocks(offset=request.offset, count=quantity):
                transaction_count = xrd_pb2.TransactionCount()
                for tx in blk.transactions:
                    transaction_count.count[CODEMAP[tx.WhichOneof('transactionType')]] += 1

                result.append(xrd_pb2.BlockHeaderExtended(header=blk.blockheader.pbdata,
                                                          transaction_count=transaction_count))
            response.blockheaders.extend(result)

        if all_requested or request.filter == xrd_pb2.GetLatestDataReq.TRANSACTIONS:
            result = []
            for tx in self.xrdnode.get_latest_transactions(offset=request.offset, count=quantity):
                # FIXME: Improve this once we have a proper database schema
                block_index = self.xrdnode.get_blockidx_from_txhash(tx.txhash)
                block = self.xrdnode.get_block_from_index(block_index)
                header = None
                if block:
                    header = block.blockheader.pbdata
                txextended = xrd_pb2.TransactionExtended(header=header,
                                                         tx=tx.pbdata,
                                                         addr_from=tx.addr_from,
                                                         size=tx.size)
                result.append(txextended)

            response.transactions.extend(result)

        if all_requested or request.filter == xrd_pb2.GetLatestDataReq.TRANSACTIONS_UNCONFIRMED:
            result = []
            for tx_info in self.xrdnode.get_latest_transactions_unconfirmed(offset=request.offset, count=quantity):
                tx = tx_info.transaction
                txextended = xrd_pb2.TransactionExtended(header=None,
                                                         tx=tx.pbdata,
                                                         addr_from=tx.addr_from,
                                                         size=tx.size,
                                                         timestamp_seconds=tx_info.timestamp)
                result.append(txextended)
            response.transactions_unconfirmed.extend(result)

        return response

    # Obsolete
    # @GrpcExceptionWrapper(xrd_pb2.GetTransactionsByAddressResp)
    # def GetTransactionsByAddress(self,
    #                              request: xrd_pb2.GetTransactionsByAddressReq,
    #                              context) -> xrd_pb2.GetTransactionsByAddressResp:
    #     logger.debug("[PublicAPI] GetTransactionsByAddress")
    #     response = xrd_pb2.GetTransactionsByAddressResp()
    #     mini_transactions, balance = self.xrdnode.get_transactions_by_address(request.address)
    #     response.mini_transactions.extend(mini_transactions)
    #     response.balance = balance
    #     return response

    @GrpcExceptionWrapper(xrd_pb2.GetMiniTransactionsByAddressResp)
    def GetMiniTransactionsByAddress(self,
                                     request: xrd_pb2.GetMiniTransactionsByAddressReq,
                                     context) -> xrd_pb2.GetMiniTransactionsByAddressResp:
        logger.debug("[PublicAPI] GetTransactionsByAddress")
        return self.xrdnode.get_mini_transactions_by_address(request.address,
                                                             request.item_per_page,
                                                             request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetTransactionsByAddressResp)
    def GetTransactionsByAddress(self,
                                 request: xrd_pb2.GetTransactionsByAddressReq,
                                 context) -> xrd_pb2.GetTransactionsByAddressResp:
        logger.debug("[PublicAPI] GetTransactionsByAddress")
        return self.xrdnode.get_transactions_by_address(request.address,
                                                        request.item_per_page,
                                                        request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetTokensByAddressResp)
    def GetTokensByAddress(self,
                           request: xrd_pb2.GetTransactionsByAddressReq,
                           context) -> xrd_pb2.GetTokensByAddressResp:
        logger.debug("[PublicAPI] GetTokensByAddress")
        return self.xrdnode.get_tokens_by_address(request.address,
                                                  request.item_per_page,
                                                  request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetSlavesByAddressResp)
    def GetSlavesByAddress(self,
                           request: xrd_pb2.GetTransactionsByAddressReq,
                           context) -> xrd_pb2.GetSlavesByAddressResp:
        logger.debug("[PublicAPI] GetSlavesByAddress")
        return self.xrdnode.get_slaves_by_address(request.address,
                                                  request.item_per_page,
                                                  request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetLatticePKsByAddressResp)
    def GetLatticePKsByAddress(self,
                               request: xrd_pb2.GetTransactionsByAddressReq,
                               context) -> xrd_pb2.GetLatticePKsByAddressResp:
        logger.debug("[PublicAPI] GetLatticePKsByAddress")
        return self.xrdnode.get_lattice_pks_by_address(request.address,
                                                       request.item_per_page,
                                                       request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetMultiSigAddressesByAddressResp)
    def GetMultiSigAddressesByAddress(self,
                                      request: xrd_pb2.GetTransactionsByAddressReq,
                                      context) -> xrd_pb2.GetMultiSigAddressesByAddressResp:
        logger.debug("[PublicAPI] GetMultiSigAddressesByAddress")
        return self.xrdnode.get_multi_sig_addresses_by_address(request.address,
                                                               request.item_per_page,
                                                               request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetMultiSigSpendTxsByAddressResp)
    def GetMultiSigSpendTxsByAddress(self,
                                     request: xrd_pb2.GetMultiSigSpendTxsByAddressReq,
                                     context) -> xrd_pb2.GetMultiSigSpendTxsByAddressResp:
        logger.debug("[PublicAPI] GetMultiSigSpendTxsByAddress")
        return self.xrdnode.get_multi_sig_spend_txs_by_address(request.address,
                                                               request.item_per_page,
                                                               request.page_number,
                                                               request.filter_type)

    @GrpcExceptionWrapper(xrd_pb2.GetInboxMessagesByAddressResp)
    def GetInboxMessagesByAddress(self,
                                  request: xrd_pb2.GetTransactionsByAddressReq,
                                  context) -> xrd_pb2.GetInboxMessagesByAddressResp:
        logger.debug("[PublicAPI] GetInboxMessagesByAddress")
        return self.xrdnode.get_inbox_messages_by_address(request.address,
                                                          request.item_per_page,
                                                          request.page_number)

    @GrpcExceptionWrapper(xrd_pb2.GetVoteStatsResp)
    def GetVoteStats(self,
                     request: xrd_pb2.GetVoteStatsReq,
                     context) -> xrd_pb2.GetVoteStatsResp:
        logger.debug("[PublicAPI] GetVoteStats")
        return self.xrdnode.get_vote_stats(request.multi_sig_spend_tx_hash)

    @GrpcExceptionWrapper(xrd_pb2.GetTransactionResp)
    def GetTransaction(self, request: xrd_pb2.GetTransactionReq, context) -> xrd_pb2.GetTransactionResp:
        logger.debug("[PublicAPI] GetTransaction")
        response = xrd_pb2.GetTransactionResp()
        tx_blocknumber = self.xrdnode.get_transaction(request.tx_hash)
        if tx_blocknumber:
            response.tx.MergeFrom(tx_blocknumber[0].pbdata)
            response.confirmations = self.xrdnode.block_height - tx_blocknumber[1] + 1
            response.block_number = tx_blocknumber[1]
            response.block_header_hash = self.xrdnode.get_block_header_hash_by_number(tx_blocknumber[1])
        else:
            tx_timestamp = self.xrdnode.get_unconfirmed_transaction(request.tx_hash)
            if tx_timestamp:
                response.tx.MergeFrom(tx_timestamp[0].pbdata)
                response.confirmations = 0

        return response

    @GrpcExceptionWrapper(xrd_pb2.GetBalanceResp)
    def GetBalance(self, request: xrd_pb2.GetBalanceReq, context) -> xrd_pb2.GetBalanceResp:
        logger.debug("[PublicAPI] GetBalance")
        address_state = self.xrdnode.get_optimized_address_state(request.address)
        response = xrd_pb2.GetBalanceResp(balance=address_state.balance)
        return response

    @GrpcExceptionWrapper(xrd_pb2.GetTotalBalanceResp)
    def GetTotalBalance(self, request: xrd_pb2.GetTotalBalanceReq, context) -> xrd_pb2.GetTotalBalanceResp:
        logger.debug("[PublicAPI] GetTotalBalance")
        response = xrd_pb2.GetBalanceResp(balance=0)

        for address in request.addresses:
            address_state = self.xrdnode.get_optimized_address_state(address)
            response.balance += address_state.balance

        return response

    @GrpcExceptionWrapper(xrd_pb2.GetOTSResp)
    def GetOTS(self, request: xrd_pb2.GetOTSReq, context) -> xrd_pb2.GetOTSResp:
        logger.debug("[PublicAPI] GetOTS")
        ots_bitfield_by_page, next_unused_ots_index, unused_ots_index_found = \
            self.xrdnode.get_ots(request.address,
                                 request.page_from,
                                 request.page_count,
                                 request.unused_ots_index_from)
        response = xrd_pb2.GetOTSResp(ots_bitfield_by_page=ots_bitfield_by_page,
                                      next_unused_ots_index=next_unused_ots_index,
                                      unused_ots_index_found=unused_ots_index_found)
        return response

    @GrpcExceptionWrapper(xrd_pb2.GetHeightResp)
    def GetHeight(self, request: xrd_pb2.GetHeightReq, context) -> xrd_pb2.GetHeightResp:
        logger.debug("[PublicAPI] GetHeight")
        return xrd_pb2.GetHeightResp(height=self.xrdnode.block_height)

    @GrpcExceptionWrapper(xrd_pb2.GetBlockResp)
    def GetBlock(self, request: xrd_pb2.GetBlockReq, context) -> xrd_pb2.GetBlockResp:
        logger.debug("[PublicAPI] GetBlock")
        block = self.xrdnode.get_block_from_hash(request.header_hash)
        if block:
            return xrd_pb2.GetBlockResp(block=block.pbdata)
        return xrd_pb2.GetBlockResp()

    @GrpcExceptionWrapper(xrd_pb2.GetBlockByNumberResp)
    def GetBlockByNumber(self, request: xrd_pb2.GetBlockByNumberReq, context) -> xrd_pb2.GetBlockByNumberResp:
        logger.debug("[PublicAPI] GetBlockFromNumber")
        block = self.xrdnode.get_block_from_index(request.block_number)
        if block:
            return xrd_pb2.GetBlockByNumberResp(block=block.pbdata)
        return xrd_pb2.GetBlockByNumberResp()
