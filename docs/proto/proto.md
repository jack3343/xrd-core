# Protocol Documentation
<a name="top"/>

## Table of Contents

- [xrd.proto](#xrd.proto)
    - [AddressList](#xrd.AddressList)
    - [AddressState](#xrd.AddressState)
    - [Block](#xrd.Block)
    - [BlockExtended](#xrd.BlockExtended)
    - [BlockHeader](#xrd.BlockHeader)
    - [BlockHeaderExtended](#xrd.BlockHeaderExtended)
    - [BlockMetaData](#xrd.BlockMetaData)
    - [BlockMetaDataList](#xrd.BlockMetaDataList)
    - [EphemeralMessage](#xrd.EphemeralMessage)
    - [GenesisBalance](#xrd.GenesisBalance)
    - [GetAddressStateReq](#xrd.GetAddressStateReq)
    - [GetAddressStateResp](#xrd.GetAddressStateResp)
    - [GetBlockReq](#xrd.GetBlockReq)
    - [GetBlockResp](#xrd.GetBlockResp)
    - [GetKnownPeersReq](#xrd.GetKnownPeersReq)
    - [GetKnownPeersResp](#xrd.GetKnownPeersResp)
    - [GetLatestDataReq](#xrd.GetLatestDataReq)
    - [GetLatestDataResp](#xrd.GetLatestDataResp)
    - [GetLocalAddressesReq](#xrd.GetLocalAddressesReq)
    - [GetLocalAddressesResp](#xrd.GetLocalAddressesResp)
    - [GetNodeStateReq](#xrd.GetNodeStateReq)
    - [GetNodeStateResp](#xrd.GetNodeStateResp)
    - [GetObjectReq](#xrd.GetObjectReq)
    - [GetObjectResp](#xrd.GetObjectResp)
    - [GetStakersReq](#xrd.GetStakersReq)
    - [GetStakersResp](#xrd.GetStakersResp)
    - [GetStatsReq](#xrd.GetStatsReq)
    - [GetStatsResp](#xrd.GetStatsResp)
    - [GetWalletReq](#xrd.GetWalletReq)
    - [GetWalletResp](#xrd.GetWalletResp)
    - [LatticePublicKeyTxnReq](#xrd.LatticePublicKeyTxnReq)
    - [MR](#xrd.MR)
    - [MsgObject](#xrd.MsgObject)
    - [NodeInfo](#xrd.NodeInfo)
    - [Peer](#xrd.Peer)
    - [PingReq](#xrd.PingReq)
    - [PongResp](#xrd.PongResp)
    - [PushTransactionReq](#xrd.PushTransactionReq)
    - [PushTransactionResp](#xrd.PushTransactionResp)
    - [StakeValidator](#xrd.StakeValidator)
    - [StakeValidatorsList](#xrd.StakeValidatorsList)
    - [StakeValidatorsTracker](#xrd.StakeValidatorsTracker)
    - [StakeValidatorsTracker.ExpiryEntry](#xrd.StakeValidatorsTracker.ExpiryEntry)
    - [StakeValidatorsTracker.FutureStakeAddressesEntry](#xrd.StakeValidatorsTracker.FutureStakeAddressesEntry)
    - [StakeValidatorsTracker.FutureSvDictEntry](#xrd.StakeValidatorsTracker.FutureSvDictEntry)
    - [StakeValidatorsTracker.SvDictEntry](#xrd.StakeValidatorsTracker.SvDictEntry)
    - [StakerData](#xrd.StakerData)
    - [StoredPeers](#xrd.StoredPeers)
    - [Timestamp](#xrd.Timestamp)
    - [Transaction](#xrd.Transaction)
    - [Transaction.CoinBase](#xrd.Transaction.CoinBase)
    - [Transaction.Destake](#xrd.Transaction.Destake)
    - [Transaction.Duplicate](#xrd.Transaction.Duplicate)
    - [Transaction.LatticePublicKey](#xrd.Transaction.LatticePublicKey)
    - [Transaction.Stake](#xrd.Transaction.Stake)
    - [Transaction.Transfer](#xrd.Transaction.Transfer)
    - [Transaction.Vote](#xrd.Transaction.Vote)
    - [TransactionCount](#xrd.TransactionCount)
    - [TransactionCount.CountEntry](#xrd.TransactionCount.CountEntry)
    - [TransactionExtended](#xrd.TransactionExtended)
    - [TransferCoinsReq](#xrd.TransferCoinsReq)
    - [TransferCoinsResp](#xrd.TransferCoinsResp)
    - [Wallet](#xrd.Wallet)
    - [WalletStore](#xrd.WalletStore)

    - [GetLatestDataReq.Filter](#xrd.GetLatestDataReq.Filter)
    - [GetStakersReq.Filter](#xrd.GetStakersReq.Filter)
    - [NodeInfo.State](#xrd.NodeInfo.State)
    - [Transaction.Type](#xrd.Transaction.Type)


    - [AdminAPI](#xrd.AdminAPI)
    - [P2PAPI](#xrd.P2PAPI)
    - [PublicAPI](#xrd.PublicAPI)


- [xrdbase.proto](#xrdbase.proto)
    - [GetNodeInfoReq](#xrd.GetNodeInfoReq)
    - [GetNodeInfoResp](#xrd.GetNodeInfoResp)



    - [Base](#xrd.Base)


- [xrdlegacy.proto](#xrdlegacy.proto)
    - [BKData](#xrd.BKData)
    - [FBData](#xrd.FBData)
    - [LegacyMessage](#xrd.LegacyMessage)
    - [MRData](#xrd.MRData)
    - [NoData](#xrd.NoData)
    - [PBData](#xrd.PBData)
    - [PLData](#xrd.PLData)
    - [PONGData](#xrd.PONGData)
    - [SYNCData](#xrd.SYNCData)
    - [VEData](#xrd.VEData)

    - [LegacyMessage.FuncName](#xrd.LegacyMessage.FuncName)




- [Scalar Value Types](#scalar-value-types)



<a name="xrd.proto"/>
<p align="right"><a href="#top">Top</a></p>

## xrd.proto



<a name="xrd.AddressList"/>

### AddressList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="xrd.AddressState"/>

### AddressState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  | FIXME: Discuss. 32 or 64 bits? |
| pubhashes | [bytes](#bytes) | repeated |  |
| transaction_hashes | [bytes](#bytes) | repeated |  |






<a name="xrd.Block"/>

### Block



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#xrd.BlockHeader) |  |  |
| transactions | [Transaction](#xrd.Transaction) | repeated |  |
| dup_transactions | [Transaction](#xrd.Transaction) | repeated | TODO: Review this |
| vote | [Transaction](#xrd.Transaction) | repeated |  |
| genesis_balance | [GenesisBalance](#xrd.GenesisBalance) | repeated | This is only applicable to genesis blocks |






<a name="xrd.BlockExtended"/>

### BlockExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block | [Block](#xrd.Block) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="xrd.BlockHeader"/>

### BlockHeader



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  | Header |
| epoch | [uint64](#uint64) |  |  |
| timestamp | [Timestamp](#xrd.Timestamp) |  | FIXME: Temporary |
| hash_header | [bytes](#bytes) |  |  |
| hash_header_prev | [bytes](#bytes) |  |  |
| reward_block | [uint64](#uint64) |  |  |
| reward_fee | [uint64](#uint64) |  |  |
| merkle_root | [bytes](#bytes) |  |  |
| hash_reveal | [bytes](#bytes) |  |  |
| stake_selector | [bytes](#bytes) |  |  |






<a name="xrd.BlockHeaderExtended"/>

### BlockHeaderExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#xrd.BlockHeader) |  |  |
| transaction_count | [TransactionCount](#xrd.TransactionCount) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="xrd.BlockMetaData"/>

### BlockMetaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="xrd.BlockMetaDataList"/>

### BlockMetaDataList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number_hashes | [BlockMetaData](#xrd.BlockMetaData) | repeated |  |






<a name="xrd.EphemeralMessage"/>

### EphemeralMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [bytes](#bytes) |  |  |
| ttl | [uint64](#uint64) |  |  |
| data | [bytes](#bytes) |  | Encrypted String containing aes256_symkey, prf512_seed, xmss_address, signature |






<a name="xrd.EphemeralMessage.Data"/>

### EphemeralMessage.Data



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| aes256_symkey | [bytes](#bytes) |  |  |
| prf512_seed | [bytes](#bytes) |  |  |
| xmss_address | [bytes](#bytes) |  |  |
| xmss_signature | [bytes](#bytes) |  |  |






<a name="xrd.GenesisBalance"/>

### GenesisBalance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | Address is string only here to increase visibility |
| balance | [uint64](#uint64) |  |  |






<a name="xrd.GetAddressStateReq"/>

### GetAddressStateReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="xrd.GetAddressStateResp"/>

### GetAddressStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [AddressState](#xrd.AddressState) |  |  |






<a name="xrd.GetBlockReq"/>

### GetBlockReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  | Indicates the index number in mainchain |
| after_hash | [bytes](#bytes) |  | request the node that comes after hash |






<a name="xrd.GetBlockResp"/>

### GetBlockResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#xrd.NodeInfo) |  |  |
| block | [Block](#xrd.Block) |  |  |






<a name="xrd.GetKnownPeersReq"/>

### GetKnownPeersReq







<a name="xrd.GetKnownPeersResp"/>

### GetKnownPeersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#xrd.NodeInfo) |  |  |
| known_peers | [Peer](#xrd.Peer) | repeated |  |






<a name="xrd.GetLatestDataReq"/>

### GetLatestDataReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetLatestDataReq.Filter](#xrd.GetLatestDataReq.Filter) |  |  |
| offset | [uint32](#uint32) |  | Offset in the result list (works backwards in this case) |
| quantity | [uint32](#uint32) |  | Number of items to retrive. Capped at 100 |






<a name="xrd.GetLatestDataResp"/>

### GetLatestDataResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| blockheaders | [BlockHeaderExtended](#xrd.BlockHeaderExtended) | repeated |  |
| transactions | [TransactionExtended](#xrd.TransactionExtended) | repeated |  |
| transactions_unconfirmed | [TransactionExtended](#xrd.TransactionExtended) | repeated |  |






<a name="xrd.GetLocalAddressesReq"/>

### GetLocalAddressesReq







<a name="xrd.GetLocalAddressesResp"/>

### GetLocalAddressesResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="xrd.GetNodeStateReq"/>

### GetNodeStateReq







<a name="xrd.GetNodeStateResp"/>

### GetNodeStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [NodeInfo](#xrd.NodeInfo) |  |  |






<a name="xrd.GetObjectReq"/>

### GetObjectReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [bytes](#bytes) |  |  |






<a name="xrd.GetObjectResp"/>

### GetObjectResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| found | [bool](#bool) |  |  |
| address_state | [AddressState](#xrd.AddressState) |  |  |
| transaction | [TransactionExtended](#xrd.TransactionExtended) |  |  |
| block | [Block](#xrd.Block) |  |  |






<a name="xrd.GetStakersReq"/>

### GetStakersReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetStakersReq.Filter](#xrd.GetStakersReq.Filter) |  | Indicates which group of stakers (current / next) |
| offset | [uint32](#uint32) |  | Offset in the staker list |
| quantity | [uint32](#uint32) |  | Number of stakers to retrive. Capped at 100 |






<a name="xrd.GetStakersResp"/>

### GetStakersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stakers | [StakerData](#xrd.StakerData) | repeated |  |






<a name="xrd.GetStatsReq"/>

### GetStatsReq







<a name="xrd.GetStatsResp"/>

### GetStatsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#xrd.NodeInfo) |  |  |
| epoch | [uint64](#uint64) |  | Current epoch |
| uptime_network | [uint64](#uint64) |  | Indicates uptime in seconds |
| stakers_count | [uint64](#uint64) |  | Number of active stakers |
| block_last_reward | [uint64](#uint64) |  |  |
| block_time_mean | [uint64](#uint64) |  |  |
| block_time_sd | [uint64](#uint64) |  |  |
| coins_total_supply | [uint64](#uint64) |  |  |
| coins_emitted | [uint64](#uint64) |  |  |
| coins_atstake | [uint64](#uint64) |  |  |






<a name="xrd.GetWalletReq"/>

### GetWalletReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="xrd.GetWalletResp"/>

### GetWalletResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallet | [Wallet](#xrd.Wallet) |  | FIXME: Encrypt |






<a name="xrd.LatticePublicKeyTxnReq"/>

### LatticePublicKeyTxnReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  |  |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |
| xmss_pk | [bytes](#bytes) |  |  |
| xmss_ots_index | [uint64](#uint64) |  |  |






<a name="xrd.MR"/>

### MR
FIXME: This is legacy. Plan removal


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [string](#string) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="xrd.MsgObject"/>

### MsgObject



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ephemeral | [EphemeralMessage](#xrd.EphemeralMessage) |  | Overlapping - objects used for 2-way exchanges P2PRequest request = 1; P2PResponse response = 2; |






<a name="xrd.NodeInfo"/>

### NodeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| state | [NodeInfo.State](#xrd.NodeInfo.State) |  |  |
| num_connections | [uint32](#uint32) |  |  |
| num_known_peers | [uint32](#uint32) |  |  |
| uptime | [uint64](#uint64) |  | Uptime in seconds |
| block_height | [uint64](#uint64) |  |  |
| block_last_hash | [bytes](#bytes) |  |  |
| stake_enabled | [bool](#bool) |  |  |
| network_id | [string](#string) |  |  |






<a name="xrd.Peer"/>

### Peer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ip | [string](#string) |  |  |






<a name="xrd.PingReq"/>

### PingReq







<a name="xrd.PongResp"/>

### PongResp







<a name="xrd.PushTransactionReq"/>

### PushTransactionReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_signed | [Transaction](#xrd.Transaction) |  |  |






<a name="xrd.PushTransactionResp"/>

### PushTransactionResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| some_response | [string](#string) |  |  |






<a name="xrd.StakeValidator"/>

### StakeValidator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| slave_public_key | [bytes](#bytes) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| activation_blocknumber | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  |  |
| is_banned | [bool](#bool) |  |  |
| is_active | [bool](#bool) |  |  |






<a name="xrd.StakeValidatorsList"/>

### StakeValidatorsList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stake_validators | [StakeValidator](#xrd.StakeValidator) | repeated |  |






<a name="xrd.StakeValidatorsTracker"/>

### StakeValidatorsTracker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sv_dict | [StakeValidatorsTracker.SvDictEntry](#xrd.StakeValidatorsTracker.SvDictEntry) | repeated |  |
| future_stake_addresses | [StakeValidatorsTracker.FutureStakeAddressesEntry](#xrd.StakeValidatorsTracker.FutureStakeAddressesEntry) | repeated |  |
| expiry | [StakeValidatorsTracker.ExpiryEntry](#xrd.StakeValidatorsTracker.ExpiryEntry) | repeated |  |
| future_sv_dict | [StakeValidatorsTracker.FutureSvDictEntry](#xrd.StakeValidatorsTracker.FutureSvDictEntry) | repeated |  |
| total_stake_amount | [uint64](#uint64) |  |  |






<a name="xrd.StakeValidatorsTracker.ExpiryEntry"/>

### StakeValidatorsTracker.ExpiryEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [AddressList](#xrd.AddressList) |  |  |






<a name="xrd.StakeValidatorsTracker.FutureStakeAddressesEntry"/>

### StakeValidatorsTracker.FutureStakeAddressesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#xrd.StakeValidator) |  |  |






<a name="xrd.StakeValidatorsTracker.FutureSvDictEntry"/>

### StakeValidatorsTracker.FutureSvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [StakeValidatorsList](#xrd.StakeValidatorsList) |  |  |






<a name="xrd.StakeValidatorsTracker.SvDictEntry"/>

### StakeValidatorsTracker.SvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#xrd.StakeValidator) |  |  |






<a name="xrd.StakerData"/>

### StakerData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_state | [AddressState](#xrd.AddressState) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |






<a name="xrd.StoredPeers"/>

### StoredPeers



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peers | [Peer](#xrd.Peer) | repeated |  |






<a name="xrd.Timestamp"/>

### Timestamp
TODO: Avoid using timestamp until the github issue is fixed
import &#34;google/protobuf/timestamp.proto&#34;;


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seconds | [int64](#int64) |  |  |
| nanos | [int32](#int32) |  |  |






<a name="xrd.Transaction"/>

### Transaction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Transaction.Type](#xrd.Transaction.Type) |  |  |
| nonce | [uint64](#uint64) |  |  |
| addr_from | [bytes](#bytes) |  |  |
| public_key | [bytes](#bytes) |  |  |
| transaction_hash | [bytes](#bytes) |  |  |
| ots_key | [uint32](#uint32) |  |  |
| signature | [bytes](#bytes) |  |  |
| transfer | [Transaction.Transfer](#xrd.Transaction.Transfer) |  |  |
| stake | [Transaction.Stake](#xrd.Transaction.Stake) |  |  |
| coinbase | [Transaction.CoinBase](#xrd.Transaction.CoinBase) |  |  |
| latticePK | [Transaction.LatticePublicKey](#xrd.Transaction.LatticePublicKey) |  |  |
| duplicate | [Transaction.Duplicate](#xrd.Transaction.Duplicate) |  |  |
| vote | [Transaction.Vote](#xrd.Transaction.Vote) |  |  |






<a name="xrd.Transaction.CoinBase"/>

### Transaction.CoinBase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |






<a name="xrd.Transaction.Destake"/>

### Transaction.Destake







<a name="xrd.Transaction.Duplicate"/>

### Transaction.Duplicate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| prev_header_hash | [uint64](#uint64) |  |  |
| coinbase1_hhash | [bytes](#bytes) |  |  |
| coinbase2_hhash | [bytes](#bytes) |  |  |
| coinbase1 | [Transaction](#xrd.Transaction) |  |  |
| coinbase2 | [Transaction](#xrd.Transaction) |  |  |






<a name="xrd.Transaction.LatticePublicKey"/>

### Transaction.LatticePublicKey



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |






<a name="xrd.Transaction.Stake"/>

### Transaction.Stake



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activation_blocknumber | [uint64](#uint64) |  |  |
| slavePK | [bytes](#bytes) |  |  |
| hash | [bytes](#bytes) |  |  |






<a name="xrd.Transaction.Transfer"/>

### Transaction.Transfer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |
| fee | [uint64](#uint64) |  |  |






<a name="xrd.Transaction.Vote"/>

### Transaction.Vote



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="xrd.TransactionCount"/>

### TransactionCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [TransactionCount.CountEntry](#xrd.TransactionCount.CountEntry) | repeated |  |






<a name="xrd.TransactionCount.CountEntry"/>

### TransactionCount.CountEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="xrd.TransactionExtended"/>

### TransactionExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#xrd.BlockHeader) |  |  |
| tx | [Transaction](#xrd.Transaction) |  |  |






<a name="xrd.TransferCoinsReq"/>

### TransferCoinsReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  | Transaction source address |
| address_to | [bytes](#bytes) |  | Transaction destination address |
| amount | [uint64](#uint64) |  | Amount. It should be expressed in Shor |
| fee | [uint64](#uint64) |  | Fee. It should be expressed in Shor |
| xmss_pk | [bytes](#bytes) |  | XMSS Public key |
| xmss_ots_index | [uint64](#uint64) |  | XMSS One time signature index |






<a name="xrd.TransferCoinsResp"/>

### TransferCoinsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_unsigned | [Transaction](#xrd.Transaction) |  |  |






<a name="xrd.Wallet"/>

### Wallet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | FIXME move to bytes |
| mnemonic | [string](#string) |  |  |
| xmss_index | [int32](#int32) |  |  |






<a name="xrd.WalletStore"/>

### WalletStore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallets | [Wallet](#xrd.Wallet) | repeated |  |








<a name="xrd.GetLatestDataReq.Filter"/>

### GetLatestDataReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALL | 0 |  |
| BLOCKHEADERS | 1 |  |
| TRANSACTIONS | 2 |  |
| TRANSACTIONS_UNCONFIRMED | 3 |  |



<a name="xrd.GetStakersReq.Filter"/>

### GetStakersReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| CURRENT | 0 |  |
| NEXT | 1 |  |



<a name="xrd.NodeInfo.State"/>

### NodeInfo.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| UNSYNCED | 1 |  |
| SYNCING | 2 |  |
| SYNCED | 3 |  |
| FORKED | 4 |  |



<a name="xrd.Transaction.Type"/>

### Transaction.Type


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| TRANSFER | 1 |  |
| STAKE | 2 |  |
| DESTAKE | 3 |  |
| COINBASE | 4 |  |
| LATTICE | 5 |  |
| DUPLICATE | 6 |  |
| VOTE | 7 |  |







<a name="xrd.AdminAPI"/>

### AdminAPI
This is a place holder for testing/instrumentation APIs

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLocalAddresses | [GetLocalAddressesReq](#xrd.GetLocalAddressesReq) | [GetLocalAddressesResp](#xrd.GetLocalAddressesReq) | FIXME: Use TLS and some signature scheme to validate the cli? At the moment, it will run locally |


<a name="xrd.P2PAPI"/>

### P2PAPI
This service describes the P2P API

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#xrd.GetNodeStateReq) | [GetNodeStateResp](#xrd.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#xrd.GetKnownPeersReq) | [GetKnownPeersResp](#xrd.GetKnownPeersReq) |  |
| GetBlock | [GetBlockReq](#xrd.GetBlockReq) | [GetBlockResp](#xrd.GetBlockReq) | rpc PublishBlock(PublishBlockReq) returns (PublishBlockResp); |
| ObjectExchange | [MsgObject](#xrd.MsgObject) | [MsgObject](#xrd.MsgObject) | A bidirectional streaming channel is used to avoid any firewalling/NAT issues. |


<a name="xrd.PublicAPI"/>

### PublicAPI
This service describes the Public API used by clients (wallet/cli/etc)

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#xrd.GetNodeStateReq) | [GetNodeStateResp](#xrd.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#xrd.GetKnownPeersReq) | [GetKnownPeersResp](#xrd.GetKnownPeersReq) |  |
| GetStats | [GetStatsReq](#xrd.GetStatsReq) | [GetStatsResp](#xrd.GetStatsReq) |  |
| GetAddressState | [GetAddressStateReq](#xrd.GetAddressStateReq) | [GetAddressStateResp](#xrd.GetAddressStateReq) |  |
| GetObject | [GetObjectReq](#xrd.GetObjectReq) | [GetObjectResp](#xrd.GetObjectReq) |  |
| GetLatestData | [GetLatestDataReq](#xrd.GetLatestDataReq) | [GetLatestDataResp](#xrd.GetLatestDataReq) |  |
| GetStakers | [GetStakersReq](#xrd.GetStakersReq) | [GetStakersResp](#xrd.GetStakersReq) |  |
| TransferCoins | [TransferCoinsReq](#xrd.TransferCoinsReq) | [TransferCoinsResp](#xrd.TransferCoinsReq) |  |
| PushTransaction | [PushTransactionReq](#xrd.PushTransactionReq) | [PushTransactionResp](#xrd.PushTransactionReq) |  |
| GetLatticePublicKeyTxn | [LatticePublicKeyTxnReq](#xrd.LatticePublicKeyTxnReq) | [TransferCoinsResp](#xrd.LatticePublicKeyTxnReq) |  |





<a name="xrdbase.proto"/>
<p align="right"><a href="#top">Top</a></p>

## xrdbase.proto



<a name="xrd.GetNodeInfoReq"/>

### GetNodeInfoReq







<a name="xrd.GetNodeInfoResp"/>

### GetNodeInfoResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| grpcProto | [string](#string) |  |  |












<a name="xrd.Base"/>

### Base


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeInfo | [GetNodeInfoReq](#xrd.GetNodeInfoReq) | [GetNodeInfoResp](#xrd.GetNodeInfoReq) |  |





<a name="xrdlegacy.proto"/>
<p align="right"><a href="#top">Top</a></p>

## xrdlegacy.proto



<a name="xrd.BKData"/>

### BKData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mrData | [MRData](#xrd.MRData) |  |  |
| block | [Block](#xrd.Block) |  |  |






<a name="xrd.FBData"/>

### FBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |






<a name="xrd.LegacyMessage"/>

### LegacyMessage
Adding old code to refactor while keeping things working


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| func_name | [LegacyMessage.FuncName](#xrd.LegacyMessage.FuncName) |  |  |
| noData | [NoData](#xrd.NoData) |  |  |
| veData | [VEData](#xrd.VEData) |  |  |
| pongData | [PONGData](#xrd.PONGData) |  |  |
| mrData | [MRData](#xrd.MRData) |  |  |
| sfmData | [MRData](#xrd.MRData) |  |  |
| bkData | [BKData](#xrd.BKData) |  |  |
| fbData | [FBData](#xrd.FBData) |  |  |
| pbData | [PBData](#xrd.PBData) |  |  |
| pbbData | [PBData](#xrd.PBData) |  |  |
| syncData | [SYNCData](#xrd.SYNCData) |  |  |






<a name="xrd.MRData"/>

### MRData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [LegacyMessage.FuncName](#xrd.LegacyMessage.FuncName) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="xrd.NoData"/>

### NoData







<a name="xrd.PBData"/>

### PBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |
| block | [Block](#xrd.Block) |  |  |






<a name="xrd.PLData"/>

### PLData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peer_ips | [string](#string) | repeated |  |






<a name="xrd.PONGData"/>

### PONGData







<a name="xrd.SYNCData"/>

### SYNCData







<a name="xrd.VEData"/>

### VEData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| genesis_prev_hash | [bytes](#bytes) |  |  |








<a name="xrd.LegacyMessage.FuncName"/>

### LegacyMessage.FuncName


| Name | Number | Description |
| ---- | ------ | ----------- |
| VE | 0 | Version |
| PL | 1 | Peers List |
| PONG | 2 | Pong |
| MR | 3 | Message received |
| SFM | 4 | Send Full Message |
| BK | 5 | Block |
| FB | 6 | Fetch request for block |
| PB | 7 | Push Block |
| PBB | 8 | Push Block Buffer |
| ST | 9 | Stake Transaction |
| DST | 10 | Destake Transaction |
| DT | 11 | Duplicate Transaction |
| TX | 12 | Transfer Transaction |
| VT | 13 | Vote |
| SYNC | 14 | Add into synced list, if the node replies |










## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double" /> double |  | double | double | float |
| <a name="float" /> float |  | float | float | float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool" /> bool |  | bool | boolean | boolean |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |

