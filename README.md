# Awesome Blockchain Lab

[![Validate](https://github.com/Blockchains/awesome-blockchainlab/actions/workflows/validate.yml/badge.svg)](https://github.com/Blockchains/awesome-blockchainlab/actions/workflows/validate.yml)

A curated set of **225 open-source blockchain projects** (plus 11 in an [Extended](#extended) tier), forked under [Blockchains](https://github.com/Blockchains), kept in sync with upstream by [fork-sync](https://github.com/Blockchains/fork-sync), and indexed down to individual contracts, circuits and packages in [blockchainlab-index](https://github.com/Blockchains/blockchainlab-index). The [Blockchain Lab forge](https://blockchainlab.com/forge) composes new projects from these components.

**What gets in:** an OSI-approved licence, at least 1,000 stars (a few smaller ecosystem-critical libraries are included on purpose), active in the last 90 days, not archived. Mixed-licence repos are flagged in the licence column, e.g. Uniswap v4-core (BUSL-1.1 core, MIT interfaces) and parts of Chainlink. The forge never copies source-available files into composed projects.

- Machine-readable: [`forge.json`](forge.json)
- Tested starter templates: [blockchainlab-starters](https://github.com/Blockchains/blockchainlab-starters)
- Compose engine (idea to tested Foundry repo): [blockchainlab-compose](https://github.com/Blockchains/blockchainlab-compose)
- Composed examples: [DAO governance token](https://github.com/Blockchains/forge-dao-governance-token) · [USD-priced membership NFT](https://github.com/Blockchains/forge-usd-priced-membership-nft) · [USD savings vault](https://github.com/Blockchains/forge-example-usd-savings-vault) · [gasless membership](https://github.com/Blockchains/forge-example-gasless-membership)

## How to use a project
1. Open the fork (it tracks upstream nightly) or go straight to upstream.
2. Click **Codespaces** for a cloud dev environment, or **Starter** for a tested template that already wires the project in.
3. Reuse individual components from the index: each entry links to its component list, with paths, functions and licences.

## Contents
- [AI agents & payments](#ai-agents--payments) (3)
- [Account abstraction](#account-abstraction) (2)
- [Analytics](#analytics) (2)
- [Bitcoin & Lightning](#bitcoin--lightning) (17)
- [Bridges & interop](#bridges--interop) (1)
- [Chains & protocols](#chains--protocols) (11)
- [Clients & nodes](#clients--nodes) (36)
- [Cosmos](#cosmos) (7)
- [Cryptography & MPC](#cryptography--mpc) (1)
- [Data registries](#data-registries) (2)
- [DeFi protocols](#defi-protocols) (15)
- [Developer tooling](#developer-tooling) (18)
- [Enterprise ledgers](#enterprise-ledgers) (3)
- [Ethereum & EVM specs](#ethereum--evm-specs) (8)
- [Hedera / Hiero](#hedera--hiero) (6)
- [Identity](#identity) (2)
- [Indexing & data](#indexing--data) (5)
- [L2s & rollups](#l2s--rollups) (6)
- [Languages & compilers](#languages--compilers) (7)
- [Move (Sui/Aptos)](#move-suiaptos) (2)
- [NFTs](#nfts) (1)
- [Oracles](#oracles) (2)
- [P2P & storage](#p2p--storage) (11)
- [Payments](#payments) (1)
- [Polkadot / Substrate](#polkadot--substrate) (4)
- [Security & analysis](#security--analysis) (7)
- [Smart-contract libraries](#smart-contract-libraries) (5)
- [Solana](#solana) (9)
- [Wallets](#wallets) (16)
- [Zero knowledge](#zero-knowledge) (15)
- [Extended](#extended) (11)

## AI agents & payments

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [eliza](https://github.com/elizaOS/eliza) | Open source agentic operating system | MIT | 19539 | [Blockchains/eliza](https://github.com/Blockchains/eliza/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/eliza?quickstart=1) |
| [ClawRouter](https://github.com/BlockRunAI/ClawRouter) | The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC payments on Base & Solan | MIT | 6614 | [Blockchains/ClawRouter](https://github.com/Blockchains/ClawRouter/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ClawRouter?quickstart=1) |
| [intentkit](https://github.com/crestalnetwork/intentkit) | IntentKit is an open-source, self-hosted cloud agent cluster that manages a collaborative team of AI agents for you. | MIT | 6515 | [Blockchains/intentkit](https://github.com/Blockchains/intentkit/tree/main) | [Codespaces](https://codespaces.new/Blockchains/intentkit?quickstart=1) |

## Account abstraction

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [account-abstraction](https://github.com/eth-infinitism/account-abstraction) |  | GPL-3.0 | 1940 | [Blockchains/account-abstraction](https://github.com/Blockchains/account-abstraction/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/account-abstraction?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/erc4337-smart-account) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/account-abstraction.json) (32) |
| [permissionless.js](https://github.com/pimlicolabs/permissionless.js) | TypeScript utilities built on viem for ERC-4337: Account Abstraction | MIT | 255 | [Blockchains/permissionless.js](https://github.com/Blockchains/permissionless.js/tree/main) | [Codespaces](https://codespaces.new/Blockchains/permissionless.js?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/permissionless-js.json) (3) |

## Analytics

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [rotki](https://github.com/rotki/rotki) | A portfolio tracking, analytics, accounting and management application that protects your privacy | AGPL-3.0 | 4039 | [Blockchains/rotki](https://github.com/Blockchains/rotki/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/rotki?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/rotki.json) (10) |
| [mempool](https://github.com/mempool/mempool) | Explore the full Bitcoin ecosystem with mempool.space, or be your own explorer and self-host your own instance with one-click installation o | AGPL-3.0 (plus trademark policy) | 2848 | [Blockchains/mempool](https://github.com/Blockchains/mempool/tree/master) | [Codespaces](https://codespaces.new/Blockchains/mempool?quickstart=1) |

## Bitcoin & Lightning

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [lnd](https://github.com/lightningnetwork/lnd) | Lightning Network Daemon ⚡️ | MIT | 8195 | [Blockchains/lnd](https://github.com/Blockchains/lnd/tree/master) | [Codespaces](https://codespaces.new/Blockchains/lnd?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/lnd.json) (165) |
| [bitcoinj](https://github.com/bitcoinj/bitcoinj) | A library for working with Bitcoin | Apache-2.0 | 5234 | [Blockchains/bitcoinj](https://github.com/Blockchains/bitcoinj/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bitcoinj?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/bitcoinj.json) (0) |
| [lightning](https://github.com/ElementsProject/lightning) | Core Lightning — Lightning Network implementation focusing on spec compliance and performance | BSD-MIT (ccan/ modules carry their own licences) | 3100 | [Blockchains/lightning](https://github.com/Blockchains/lightning/tree/master) | [Codespaces](https://codespaces.new/Blockchains/lightning?quickstart=1) |
| [stacks-core](https://github.com/stacks-network/stacks-core) | The Stacks blockchain implementation | GPL-3.0 | 3062 | [Blockchains/stacks-core](https://github.com/Blockchains/stacks-core/tree/main) | [Codespaces](https://codespaces.new/Blockchains/stacks-core?quickstart=1) |
| [damus](https://github.com/damus-io/damus) | iOS nostr client | GPL-3.0 | 2143 | [Blockchains/damus](https://github.com/Blockchains/damus/tree/master) | [Codespaces](https://codespaces.new/Blockchains/damus?quickstart=1) |
| [Bitcoin.org](https://github.com/bitcoin-dot-org/Bitcoin.org) | Bitcoin.org Website | MIT | 1780 | [Blockchains/Bitcoin.org](https://github.com/Blockchains/Bitcoin.org/tree/master) | [Codespaces](https://codespaces.new/Blockchains/Bitcoin.org?quickstart=1) |
| [electrs](https://github.com/romanz/electrs) | An efficient re-implementation of Electrum Server in Rust | MIT | 1397 | [Blockchains/electrs](https://github.com/Blockchains/electrs/tree/master) | [Codespaces](https://codespaces.new/Blockchains/electrs?quickstart=1) |
| [rust-lightning](https://github.com/lightningdevkit/rust-lightning) | Active development happens on git.rust-bitcoin.org, this repo is a mirror of https://git.rust-bitcoin.org/lightningdevkit/rust-lightning | MIT OR Apache-2.0 | 1375 | [Blockchains/rust-lightning](https://github.com/Blockchains/rust-lightning/tree/main) | [Codespaces](https://codespaces.new/Blockchains/rust-lightning?quickstart=1) |
| [eclair](https://github.com/ACINQ/eclair) | A scala implementation of the Lightning Network. | Apache-2.0 | 1347 | [Blockchains/eclair](https://github.com/Blockchains/eclair/tree/master) | [Codespaces](https://codespaces.new/Blockchains/eclair?quickstart=1) |
| [esplora](https://github.com/Blockstream/esplora) | Explorer for Bitcoin and Liquid | MIT | 1269 | [Blockchains/esplora](https://github.com/Blockchains/esplora/tree/master) | [Codespaces](https://codespaces.new/Blockchains/esplora?quickstart=1) |
| [raspibolt](https://github.com/raspibolt/raspibolt) | RaspiBolt v3: Bitcoin & Lightning full node on a Raspberry Pi | MIT | 1259 | [Blockchains/raspibolt](https://github.com/Blockchains/raspibolt/tree/master) | [Codespaces](https://codespaces.new/Blockchains/raspibolt?quickstart=1) |
| [lnbits](https://github.com/lnbits/lnbits) | LNbits, free and open-source Lightning wallet and accounts system. | MIT | 1236 | [Blockchains/lnbits](https://github.com/Blockchains/lnbits/tree/dev) | [Codespaces](https://codespaces.new/Blockchains/lnbits?quickstart=1) |
| [elements](https://github.com/ElementsProject/elements) | Open-source implementation of advanced blockchain features extending the Bitcoin protocol | MIT | 1169 | [Blockchains/elements](https://github.com/Blockchains/elements/tree/master) | [Codespaces](https://codespaces.new/Blockchains/elements?quickstart=1) |
| [rango-client](https://github.com/rango-exchange/rango-client) | Rango Exchange Widget & Wallets Library | Apache-2.0 | 1125 | [Blockchains/rango-client](https://github.com/Blockchains/rango-client/tree/next) | [Codespaces](https://codespaces.new/Blockchains/rango-client?quickstart=1) |
| [bdk](https://github.com/bitcoindevkit/bdk) | A modern, lightweight, descriptor-based wallet library written in Rust! | Apache-2.0 OR MIT | 1072 | [Blockchains/bdk](https://github.com/Blockchains/bdk/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bdk?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/bdk.json) (7) |
| [LndHub](https://github.com/BlueWallet/LndHub) | Wrapper for Lightning Network Daemon. It provides separate accounts for end-users | MIT | 1052 | [Blockchains/LndHub](https://github.com/Blockchains/LndHub/tree/master) | [Codespaces](https://codespaces.new/Blockchains/LndHub?quickstart=1) |
| [robosats](https://github.com/RoboSats/robosats) | A simple and private bitcoin exchange | AGPL-3.0 | 1030 | [Blockchains/robosats](https://github.com/Blockchains/robosats/tree/main) | [Codespaces](https://codespaces.new/Blockchains/robosats?quickstart=1) |

## Bridges & interop

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [wormhole](https://github.com/wormhole-foundation/wormhole) | A reference implementation for the Wormhole blockchain interoperability protocol. | Apache-2.0 | 1898 | [Blockchains/wormhole](https://github.com/Blockchains/wormhole/tree/main) | [Codespaces](https://codespaces.new/Blockchains/wormhole?quickstart=1) |

## Chains & protocols

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [diem](https://github.com/diem/diem) | Diem’s mission is to build a trusted and innovative financial network that empowers people and businesses around the world. | Apache-2.0 | 16661 | [Blockchains/diem](https://github.com/Blockchains/diem/tree/latest) | [Codespaces](https://codespaces.new/Blockchains/diem?quickstart=1) |
| [tendermint](https://github.com/tendermint/tendermint) | ⟁ Tendermint Core (BFT Consensus) in Go | Apache-2.0 | 5862 | [Blockchains/tendermint](https://github.com/Blockchains/tendermint/tree/main) | [Codespaces](https://codespaces.new/Blockchains/tendermint?quickstart=1) |
| [lbry-desktop](https://github.com/lbryio/lbry-desktop) | A browser and wallet for LBRY, the decentralized, user-controlled content marketplace. | MIT | 3518 | [Blockchains/lbry-desktop](https://github.com/Blockchains/lbry-desktop/tree/master) | [Codespaces](https://codespaces.new/Blockchains/lbry-desktop?quickstart=1) |
| [sei-chain](https://github.com/sei-protocol/sei-chain) |  | Apache-2.0 | 2839 | [Blockchains/sei-chain](https://github.com/Blockchains/sei-chain/tree/main) | [Codespaces](https://codespaces.new/Blockchains/sei-chain?quickstart=1) |
| [chainquery](https://github.com/OdyseeTeam/chainquery) | Chainquery parses and syncs the LBRY blockchain data into structured SQL | MIT | 2207 | [Blockchains/chainquery](https://github.com/Blockchains/chainquery/tree/master) | [Codespaces](https://codespaces.new/Blockchains/chainquery?quickstart=1) |
| [Planet](https://github.com/Planetable/Planet) | Build and host decentralized blogs and websites on your Mac | MIT | 1809 | [Blockchains/Planet](https://github.com/Blockchains/Planet/tree/main) | [Codespaces](https://codespaces.new/Blockchains/Planet?quickstart=1) |
| [verge](https://github.com/vergecurrency/verge) | Official Verge Core Source Code Repository | MIT | 1559 | [Blockchains/verge](https://github.com/Blockchains/verge/tree/master) | [Codespaces](https://codespaces.new/Blockchains/verge?quickstart=1) |
| [p2pool](https://github.com/SChernykh/p2pool) | Decentralized pool for Monero mining | GPL-3.0 | 1497 | [Blockchains/p2pool](https://github.com/Blockchains/p2pool/tree/master) | [Codespaces](https://codespaces.new/Blockchains/p2pool?quickstart=1) |
| [node](https://github.com/mysteriumnetwork/node) | Mysterium Network Node -  official implementation of distributed VPN network (dVPN) protocol | GPL-3.0 | 1354 | [Blockchains/node-1](https://github.com/Blockchains/node-1/tree/master) | [Codespaces](https://codespaces.new/Blockchains/node-1?quickstart=1) |
| [IceFireDB](https://github.com/IceFireDB/IceFireDB) | @IceFireLabs -> IceFireDB is a database built for web3.0 It strives to fill the gap between web2 and web3.0 with a friendly database experie | MIT | 1156 | [Blockchains/IceFireDB](https://github.com/Blockchains/IceFireDB/tree/main) | [Codespaces](https://codespaces.new/Blockchains/IceFireDB?quickstart=1) |
| [celestia-node](https://github.com/celestiaorg/celestia-node) | Celestia Data Availability Nodes | Apache-2.0 | 1000 | [Blockchains/celestia-node](https://github.com/Blockchains/celestia-node/tree/main) | [Codespaces](https://codespaces.new/Blockchains/celestia-node?quickstart=1) |

## Clients & nodes

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [bitcoin](https://github.com/bitcoin/bitcoin) | Bitcoin Core integration/staging tree | MIT | 90306 | [Blockchains/bitcoin](https://github.com/Blockchains/bitcoin/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bitcoin?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/bitcoin.json) (2) |
| [go-ethereum](https://github.com/ethereum/go-ethereum) | Go implementation of the Ethereum protocol | LGPL-3.0 | 51385 | [Blockchains/go-ethereum](https://github.com/Blockchains/go-ethereum/tree/upstream-master) | [Codespaces](https://codespaces.new/Blockchains/go-ethereum?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/go-ethereum.json) (165) |
| [linera-protocol](https://github.com/linera-io/linera-protocol) | Main repository for the Linera protocol | Apache-2.0 | 32100 | [Blockchains/linera-protocol](https://github.com/Blockchains/linera-protocol/tree/main) | [Codespaces](https://codespaces.new/Blockchains/linera-protocol?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/linera-protocol.json) (55) |
| [dogecoin](https://github.com/dogecoin/dogecoin) | very currency | MIT | 15232 | [Blockchains/dogecoin](https://github.com/Blockchains/dogecoin/tree/master) | [Codespaces](https://codespaces.new/Blockchains/dogecoin?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/dogecoin.json) (0) |
| [monero](https://github.com/monero-project/monero) | Monero: the secure, private, untraceable cryptocurrency | BSD-3-Clause | 10897 | [Blockchains/monero](https://github.com/Blockchains/monero/tree/master) | [Codespaces](https://codespaces.new/Blockchains/monero?quickstart=1) |
| [chia-blockchain](https://github.com/Chia-Network/chia-blockchain) | Chia blockchain python implementation (full node, farmer, harvester, timelord, and wallet) | Apache-2.0 | 10790 | [Blockchains/chia-blockchain](https://github.com/Blockchains/chia-blockchain/tree/main) | [Codespaces](https://codespaces.new/Blockchains/chia-blockchain?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/chia-blockchain.json) (4) |
| [btcd](https://github.com/btcsuite/btcd) | An alternative full node bitcoin implementation written in Go (golang) | ISC | 6712 | [Blockchains/btcd](https://github.com/Blockchains/btcd/tree/master) | [Codespaces](https://codespaces.new/Blockchains/btcd?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/btcd.json) (57) |
| [reth](https://github.com/paradigmxyz/reth) | Modular, contributor-friendly and blazing-fast implementation of the Ethereum protocol, in Rust | Apache-2.0 | 5807 | [Blockchains/reth](https://github.com/Blockchains/reth/tree/main) | [Codespaces](https://codespaces.new/Blockchains/reth?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/reth.json) (116) |
| [rippled](https://github.com/XRPLF/rippled) | Decentralized cryptocurrency blockchain daemon implementing the XRP Ledger protocol in C++ | ISC | 5218 | [Blockchains/rippled](https://github.com/Blockchains/rippled/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/rippled?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/rippled.json) (3) |
| [grin](https://github.com/mimblewimble/grin) | Minimal implementation of the Mimblewimble protocol. | Apache-2.0 | 5102 | [Blockchains/grin](https://github.com/Blockchains/grin/tree/master) | [Codespaces](https://codespaces.new/Blockchains/grin?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/grin.json) (11) |
| [java-tron](https://github.com/tronprotocol/java-tron) | Java implementation of the Tron whitepaper | LGPL-3.0 | 4164 | [Blockchains/java-tron](https://github.com/Blockchains/java-tron/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/java-tron?quickstart=1) |
| [prysm](https://github.com/OffchainLabs/prysm) | Go implementation of Ethereum proof of stake | GPL-3.0 | 3788 | [Blockchains/prysm](https://github.com/Blockchains/prysm/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/prysm?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/prysm.json) (154) |
| [erigon](https://github.com/erigontech/erigon) | Ethereum implementation on the efficiency frontier | LGPL-3.0 | 3585 | [Blockchains/erigon](https://github.com/Blockchains/erigon/tree/main) | [Codespaces](https://codespaces.new/Blockchains/erigon?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/erigon.json) (183) |
| [neo](https://github.com/neo-project/neo) | NEO Smart Economy | MIT | 3536 | [Blockchains/neo](https://github.com/Blockchains/neo/tree/master-n3) | [Codespaces](https://codespaces.new/Blockchains/neo?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/neo.json) (0) |
| [nano-node](https://github.com/nanocurrency/nano-node) | Nano is digital currency. Its ticker is: XNO and its currency symbol is: Ӿ | BSD-3-Clause | 3525 | [Blockchains/nano-node](https://github.com/Blockchains/nano-node/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/nano-node?quickstart=1) |
| [lighthouse](https://github.com/sigp/lighthouse) | Ethereum consensus client in Rust | Apache-2.0 | 3478 | [Blockchains/lighthouse](https://github.com/Blockchains/lighthouse/tree/stable) | [Codespaces](https://codespaces.new/Blockchains/lighthouse?quickstart=1) |
| [bsc](https://github.com/bnb-chain/bsc) | A BNB Smart Chain client based on the go-ethereum fork | LGPL-3.0 | 3289 | [Blockchains/bsc](https://github.com/Blockchains/bsc/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bsc?quickstart=1) |
| [cardano-node](https://github.com/IntersectMBO/cardano-node) | The core component that is used to participate in a Cardano decentralised blockchain. | Apache-2.0 | 3176 | [Blockchains/cardano-node](https://github.com/Blockchains/cardano-node/tree/master) | [Codespaces](https://codespaces.new/Blockchains/cardano-node?quickstart=1) |
| [nearcore](https://github.com/near/nearcore) | Reference client for NEAR Protocol | GPL-3.0 | 2623 | [Blockchains/nearcore](https://github.com/Blockchains/nearcore/tree/master) | [Codespaces](https://codespaces.new/Blockchains/nearcore?quickstart=1) |
| [avalanchego](https://github.com/ava-labs/avalanchego) | Go implementation of an Avalanche node. | BSD-3-Clause | 2358 | [Blockchains/avalanchego](https://github.com/Blockchains/avalanchego/tree/master) | [Codespaces](https://codespaces.new/Blockchains/avalanchego?quickstart=1) |
| [revm](https://github.com/bluealloy/revm) | Rust implementation of the Ethereum Virtual Machine. | MIT | 2245 | [Blockchains/revm](https://github.com/Blockchains/revm/tree/main) | [Codespaces](https://codespaces.new/Blockchains/revm?quickstart=1) |
| [helios](https://github.com/a16z/helios) | A fast, secure, and portable multichain light client for Ethereum | MIT | 2186 | [Blockchains/helios](https://github.com/Blockchains/helios/tree/master) | [Codespaces](https://codespaces.new/Blockchains/helios?quickstart=1) |
| [agave](https://github.com/anza-xyz/agave) | Web-Scale Blockchain for fast, secure, scalable, decentralized apps and marketplaces. | Apache-2.0 | 1930 | [Blockchains/agave](https://github.com/Blockchains/agave/tree/master) | [Codespaces](https://codespaces.new/Blockchains/agave?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/agave.json) (194) |
| [besu](https://github.com/besu-eth/besu) | An enterprise-grade Java-based, Apache 2.0 licensed Ethereum client https://github.com/besu-eth/besu/wiki | Apache-2.0 | 1846 | [Blockchains/besu](https://github.com/Blockchains/besu/tree/main) | [Codespaces](https://codespaces.new/Blockchains/besu?quickstart=1) |
| [iotex-core](https://github.com/iotexproject/iotex-core) | Official implementation of IoTeX blockchain protocol in Go. An ultra-efficient EVM blockchain offering 1000 TPS with instant 1-block finalit | Apache-2.0 | 1614 | [Blockchains/iotex-core](https://github.com/Blockchains/iotex-core/tree/master) | [Codespaces](https://codespaces.new/Blockchains/iotex-core?quickstart=1) |
| [nethermind](https://github.com/NethermindEth/nethermind) | A robust, high-performance execution client for Ethereum node operators. | GPL-3.0 | 1609 | [Blockchains/nethermind](https://github.com/Blockchains/nethermind/tree/master) | [Codespaces](https://codespaces.new/Blockchains/nethermind?quickstart=1) |
| [harmony](https://github.com/harmony-one/harmony) | The core protocol of harmony | LGPL-3.0 | 1447 | [Blockchains/harmony](https://github.com/Blockchains/harmony/tree/main) | [Codespaces](https://codespaces.new/Blockchains/harmony?quickstart=1) |
| [lodestar](https://github.com/ChainSafe/lodestar) | 🌟 Ethereum Consensus client for the Zig and TypeScript ecosystem | Apache-2.0 | 1422 | [Blockchains/lodestar](https://github.com/Blockchains/lodestar/tree/unstable) | [Codespaces](https://codespaces.new/Blockchains/lodestar?quickstart=1) |
| [bitcoin-abc](https://github.com/Bitcoin-ABC/bitcoin-abc) | Bitcoin ABC develops node software and infrastructure for the eCash project. This a mirror of the official Bitcoin-ABC repository.  Please s | MIT | 1301 | [Blockchains/bitcoin-abc](https://github.com/Blockchains/bitcoin-abc/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bitcoin-abc?quickstart=1) |
| [AElf](https://github.com/AElfProject/AElf) | An AI-enhanced cloud-native layer-1 blockchain network. | MIT | 1267 | [Blockchains/AElf](https://github.com/Blockchains/AElf/tree/dev) | [Codespaces](https://codespaces.new/Blockchains/AElf?quickstart=1) |
| [ckb](https://github.com/nervosnetwork/ckb) | The Nervos CKB is a public permissionless blockchain, and the layer 1 of Nervos network. | MIT | 1219 | [Blockchains/ckb](https://github.com/Blockchains/ckb/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/ckb?quickstart=1) |
| [qtum](https://github.com/qtumproject/qtum) | Qtum Core Wallet | MIT | 1211 | [Blockchains/qtum](https://github.com/Blockchains/qtum/tree/master) | [Codespaces](https://codespaces.new/Blockchains/qtum?quickstart=1) |
| [Waves](https://github.com/wavesplatform/Waves) | ⛓️ Reference Waves Blockchain Node (client) implementation on Scala | MIT | 1166 | [Blockchains/Waves](https://github.com/Blockchains/Waves/tree/version-1.6.x) | [Codespaces](https://codespaces.new/Blockchains/Waves?quickstart=1) |
| [Ravencoin](https://github.com/RavenProject/Ravencoin) | Ravencoin Core integration/staging tree | MIT | 1122 | [Blockchains/Ravencoin](https://github.com/Blockchains/Ravencoin/tree/master) | [Codespaces](https://codespaces.new/Blockchains/Ravencoin?quickstart=1) |
| [bor](https://github.com/0xPolygon/bor) | Official repository for the Polygon Blockchain | LGPL-3.0 | 1104 | [Blockchains/bor](https://github.com/Blockchains/bor/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/bor?quickstart=1) |
| [aeternity](https://github.com/aeternity/aeternity) | æternity blockchain - scalable blockchain for the people - smart contracts, state channels, names, tokens | ISC | 1086 | [Blockchains/aeternity](https://github.com/Blockchains/aeternity/tree/master) | [Codespaces](https://codespaces.new/Blockchains/aeternity?quickstart=1) |

## Cosmos

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [cosmos-sdk](https://github.com/cosmos/cosmos-sdk) | Framework for building performant, customizable blockchains with native interoperability | Apache-2.0 | 7071 | [Blockchains/cosmos-sdk](https://github.com/Blockchains/cosmos-sdk/tree/main) | [Codespaces](https://codespaces.new/Blockchains/cosmos-sdk?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/cosmos-sdk.json) (168) |
| [namada](https://github.com/namada-net/namada) | Rust implementation of Namada, a Proof-of-Stake L1 for interchain asset-agnostic privacy | GPL-3.0 | 2516 | [Blockchains/namada](https://github.com/Blockchains/namada/tree/main) | [Codespaces](https://codespaces.new/Blockchains/namada?quickstart=1) |
| [cli](https://github.com/ignite/cli) | Ignite is a CLI tool and hub designed for constructing Proof of Stake Blockchains rooted in Cosmos-SDK | Apache-2.0 | 1352 | [Blockchains/cli](https://github.com/Blockchains/cli/tree/main) | [Codespaces](https://codespaces.new/Blockchains/cli?quickstart=1) |
| [cosmwasm](https://github.com/CosmWasm/cosmwasm) | WebAssembly Smart Contracts for the Cosmos SDK | Apache-2.0 | 1145 | [Blockchains/cosmwasm](https://github.com/Blockchains/cosmwasm/tree/main) | [Codespaces](https://codespaces.new/Blockchains/cosmwasm?quickstart=1) |
| [node](https://github.com/akash-network/node) | Source code for Akash node, a secure, transparent, and peer-to-peer cloud computing network | Apache-2.0 | 1117 | [Blockchains/node](https://github.com/Blockchains/node/tree/main) | [Codespaces](https://codespaces.new/Blockchains/node?quickstart=1) |
| [ibc](https://github.com/cosmos/ibc) | Interchain Standards (ICS) for the Cosmos network & interchain ecosystem. | Apache-2.0 | 1019 | [Blockchains/ibc](https://github.com/Blockchains/ibc/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ibc?quickstart=1) |
| [cometbft](https://github.com/cometbft/cometbft) | CometBFT: A distributed, Byzantine fault-tolerant, deterministic state machine replication engine. A fork and successor to Tendermint Core. | Apache-2.0 | 922 | [Blockchains/cometbft](https://github.com/Blockchains/cometbft/tree/main) | [Codespaces](https://codespaces.new/Blockchains/cometbft?quickstart=1) |

## Cryptography & MPC

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [tss-lib](https://github.com/bnb-chain/tss-lib) | Threshold Signature Scheme, for ECDSA and EDDSA | MIT | 1045 | [Blockchains/tss-lib](https://github.com/Blockchains/tss-lib/tree/master) | [Codespaces](https://codespaces.new/Blockchains/tss-lib?quickstart=1) |

## Data registries

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [chains](https://github.com/ethereum-lists/chains) | provides metadata for chains | MIT | 9829 | [Blockchains/chains](https://github.com/Blockchains/chains/tree/master) | [Codespaces](https://codespaces.new/Blockchains/chains?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/chains.json) (1) |
| [assets](https://github.com/trustwallet/assets) | A comprehensive, up-to-date collection of information about several thousands (!) of crypto tokens. | MIT | 5394 | [Blockchains/assets](https://github.com/Blockchains/assets/tree/master) | [Codespaces](https://codespaces.new/Blockchains/assets?quickstart=1) |

## DeFi protocols

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [interface](https://github.com/Uniswap/interface) | 🦄 Open source interfaces for the Uniswap protocol | GPL-3.0 | 5533 | [Blockchains/dmm-dao-web-app](https://github.com/Blockchains/dmm-dao-web-app/tree/upstream-main) | [Codespaces](https://codespaces.new/Blockchains/dmm-dao-web-app?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/dmm-dao-web-app.json) (5) |
| [bisq](https://github.com/bisq-network/bisq) | A decentralized bitcoin exchange network | AGPL-3.0 | 5139 | [Blockchains/bisq](https://github.com/Blockchains/bisq/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bisq?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/bisq.json) (0) |
| [v3-core](https://github.com/Uniswap/v3-core) | 🦄 🦄 🦄 Core smart contracts of Uniswap v3 | BUSL-1.1, converted to GPL-2.0-or-later (change date 2023-04-01 passed) | 5026 | [Blockchains/v3-core](https://github.com/Blockchains/v3-core/tree/main) | [Codespaces](https://codespaces.new/Blockchains/v3-core?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/v3-core.json) (35) |
| [v2-core](https://github.com/Uniswap/v2-core) | 🦄 🦄  Core smart contracts of Uniswap V2 | GPL-3.0 | 3354 | [Blockchains/v2-core](https://github.com/Blockchains/v2-core/tree/master) | [Codespaces](https://codespaces.new/Blockchains/v2-core?quickstart=1) |
| [v4-core](https://github.com/Uniswap/v4-core) | 🦄 🦄 🦄 🦄 Core smart contracts of Uniswap v4 | BUSL-1.1 (core) / MIT (interfaces, tests) | 2538 | [Blockchains/v4-core](https://github.com/Blockchains/v4-core/tree/main) | [Codespaces](https://codespaces.new/Blockchains/v4-core?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/uniswap-v4-hook) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/v4-core.json) (45) |
| [rango-sdk](https://github.com/rango-exchange/rango-sdk) | Rango Exchange Typescript SDK | Apache-2.0 | 1656 | [Blockchains/rango-sdk](https://github.com/Blockchains/rango-sdk/tree/next) | [Codespaces](https://codespaces.new/Blockchains/rango-sdk?quickstart=1) |
| [0x-monorepo](https://github.com/0xProject/0x-monorepo) | 0x protocol monorepo - includes our smart contracts and many developer tools | Apache-2.0 | 1408 | [Blockchains/0x-monorepo](https://github.com/Blockchains/0x-monorepo/tree/development) | [Codespaces](https://codespaces.new/Blockchains/0x-monorepo?quickstart=1) |
| [haveno](https://github.com/haveno-dex/haveno) | Decentralized P2P exchange platform built on Monero and Tor | AGPL-3.0 | 1400 | [Blockchains/haveno](https://github.com/Blockchains/haveno/tree/master) | [Codespaces](https://codespaces.new/Blockchains/haveno?quickstart=1) |
| [v3-periphery](https://github.com/Uniswap/v3-periphery) | 🦄 🦄 🦄 Peripheral smart contracts for interacting with Uniswap v3 | GPL-2.0 | 1334 | [Blockchains/v3-periphery](https://github.com/Blockchains/v3-periphery/tree/main) | [Codespaces](https://codespaces.new/Blockchains/v3-periphery?quickstart=1) |
| [v2-periphery](https://github.com/Uniswap/v2-periphery) | 🎚 Peripheral smart contracts for interacting with Uniswap V2 | GPL-3.0 | 1266 | [Blockchains/v2-periphery](https://github.com/Blockchains/v2-periphery/tree/master) | [Codespaces](https://codespaces.new/Blockchains/v2-periphery?quickstart=1) |
| [uniswap-python](https://github.com/uniswap-python/uniswap-python) | 🦄 The unofficial Python client for the Uniswap exchange. | MIT | 1019 | [Blockchains/uniswap-python](https://github.com/Blockchains/uniswap-python/tree/master) | [Codespaces](https://codespaces.new/Blockchains/uniswap-python?quickstart=1) |
| [v4-periphery](https://github.com/Uniswap/v4-periphery) | 🦄 🦄 🦄 🦄 Peripheral smart contracts for interacting with Uniswap v4 | MIT | 907 | [Blockchains/v4-periphery](https://github.com/Blockchains/v4-periphery/tree/main) | [Codespaces](https://codespaces.new/Blockchains/v4-periphery?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/uniswap-v4-hook) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/v4-periphery.json) (69) |
| [morpho-blue](https://github.com/morpho-org/morpho-blue) | Morpho's variable rate markets protocol | GPL-2.0 | 361 | [Blockchains/morpho-blue](https://github.com/Blockchains/morpho-blue/tree/main) | [Codespaces](https://codespaces.new/Blockchains/morpho-blue?quickstart=1) |
| [v4-template](https://github.com/Uniswap/v4-template) | Template repository for writing Uniswap v4 Hooks | MIT | 340 | [Blockchains/v4-template](https://github.com/Blockchains/v4-template/tree/main) | [Codespaces](https://codespaces.new/Blockchains/v4-template?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/v4-template.json) (1) |
| [uniswap-hooks](https://github.com/OpenZeppelin/uniswap-hooks) | Solidity library for secure and modular Uniswap hooks. | MIT | 127 | [Blockchains/uniswap-hooks](https://github.com/Blockchains/uniswap-hooks/tree/master) | [Codespaces](https://codespaces.new/Blockchains/uniswap-hooks?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/uniswap-v4-hook) |

## Developer tooling

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [foundry](https://github.com/foundry-rs/foundry) | Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust. | Apache-2.0 | 10633 | [Blockchains/foundry](https://github.com/Blockchains/foundry/tree/master) | [Codespaces](https://codespaces.new/Blockchains/foundry?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/foundry-oz-tokens) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/foundry.json) (49) |
| [ethers.js](https://github.com/ethers-io/ethers.js) | Complete Ethereum library and wallet implementation in JavaScript. | MIT | 8710 | [Blockchains/ethers.js](https://github.com/Blockchains/ethers.js/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ethers.js?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/ethers-js.json) (1) |
| [hardhat](https://github.com/NomicFoundation/hardhat) | Hardhat is a development environment to compile, deploy, test, and debug your Ethereum software. | MIT (per package) | 8509 | [Blockchains/buidler](https://github.com/Blockchains/buidler/tree/upstream-main) | [Codespaces](https://codespaces.new/Blockchains/buidler?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/buidler.json) (61) |
| [wagmi](https://github.com/wevm/wagmi) | Reactive primitives for Ethereum apps | MIT | 6754 | [Blockchains/wagmi](https://github.com/Blockchains/wagmi/tree/main) | [Codespaces](https://codespaces.new/Blockchains/wagmi?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/wagmi-rainbowkit-dapp) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/wagmi.json) (11) |
| [web3.py](https://github.com/ApeWorX/web3.py) | A python interface for interacting with the Ethereum blockchain and ecosystem. | MIT | 5538 | [Blockchains/web3.py](https://github.com/Blockchains/web3.py/tree/main) | [Codespaces](https://codespaces.new/Blockchains/web3.py?quickstart=1) |
| [web3j](https://github.com/LFDT-web3j/web3j) | Lightweight Java and Android library for integration with Ethereum clients | Apache-2.0 | 5403 | [Blockchains/web3j](https://github.com/Blockchains/web3j/tree/main) | [Codespaces](https://codespaces.new/Blockchains/web3j?quickstart=1) |
| [viem](https://github.com/wevm/viem) | TypeScript Interface for Ethereum | MIT | 3571 | [Blockchains/viem](https://github.com/Blockchains/viem/tree/main) | [Codespaces](https://codespaces.new/Blockchains/viem?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/wagmi-rainbowkit-dapp) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/viem.json) (19) |
| [remix-project](https://github.com/remix-project-org/remix-project) | Remix is a browser-based compiler and IDE that enables users to build Ethereum contracts with Solidity language and to debug transactions. | Apache-2.0 | 3061 | [Blockchains/remix-project](https://github.com/Blockchains/remix-project/tree/master) | [Codespaces](https://codespaces.new/Blockchains/remix-project?quickstart=1) |
| [brownie](https://github.com/eth-brownie/brownie) | A Python-based development and testing framework for smart contracts targeting the Ethereum Virtual Machine. | MIT | 2722 | [Blockchains/brownie](https://github.com/Blockchains/brownie/tree/upstream-master) | [Codespaces](https://codespaces.new/Blockchains/brownie?quickstart=1) |
| [Nethereum](https://github.com/Nethereum/Nethereum) | Ethereum .Net cross platform integration library | MIT | 2259 | [Blockchains/Nethereum](https://github.com/Blockchains/Nethereum/tree/master) | [Codespaces](https://codespaces.new/Blockchains/Nethereum?quickstart=1) |
| [scaffold-eth-2](https://github.com/scaffold-eth/scaffold-eth-2) | Open source forkable Ethereum dev stack | MIT | 2054 | [Blockchains/scaffold-eth-2](https://github.com/Blockchains/scaffold-eth-2/tree/main) | [Codespaces](https://codespaces.new/Blockchains/scaffold-eth-2?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/scaffold-eth-2.json) (2) |
| [go-stellar-sdk](https://github.com/stellar/go-stellar-sdk) | Stellar's Go SDK | Apache-2.0 | 1384 | [Blockchains/go-stellar-sdk](https://github.com/Blockchains/go-stellar-sdk/tree/main) | [Codespaces](https://codespaces.new/Blockchains/go-stellar-sdk?quickstart=1) |
| [alloy](https://github.com/alloy-rs/alloy) | Transports, Middleware, and Networks for the Alloy project | Apache-2.0 | 1334 | [Blockchains/alloy](https://github.com/Blockchains/alloy/tree/main) | [Codespaces](https://codespaces.new/Blockchains/alloy?quickstart=1) |
| [hardhat-deploy](https://github.com/wighawag/hardhat-deploy) | hardhat deployment plugin | MIT | 1267 | [Blockchains/hardhat-deploy](https://github.com/Blockchains/hardhat-deploy/tree/main) | [Codespaces](https://codespaces.new/Blockchains/hardhat-deploy?quickstart=1) |
| [starknet.js](https://github.com/starknet-io/starknet.js) | JavaScript library for Starknet | MIT | 1254 | [Blockchains/starknet.js](https://github.com/Blockchains/starknet.js/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/starknet.js?quickstart=1) |
| [whatsabi](https://github.com/shazow/whatsabi) | Extract the ABI (and resolve proxies, and get other metadata) from Ethereum bytecode, even without source code. | MIT | 1162 | [Blockchains/whatsabi](https://github.com/Blockchains/whatsabi/tree/main) | [Codespaces](https://codespaces.new/Blockchains/whatsabi?quickstart=1) |
| [forge-std](https://github.com/foundry-rs/forge-std) | A collection of helpful contracts and libraries for use with Forge and Foundry | Apache-2.0 | 1058 | [Blockchains/forge-std](https://github.com/Blockchains/forge-std/tree/master) | [Codespaces](https://codespaces.new/Blockchains/forge-std?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/foundry-oz-tokens) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/forge-std.json) (45) |
| [ape](https://github.com/ApeWorX/ape) | Build and explore on-chain with Python | Apache-2.0 | 1054 | [Blockchains/ape](https://github.com/Blockchains/ape/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ape?quickstart=1) |

## Enterprise ledgers

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [fabric](https://github.com/hyperledger/fabric) | Hyperledger Fabric is an enterprise-grade permissioned distributed ledger framework for developing solutions and applications. Its modular a | Apache-2.0 | 16735 | [Blockchains/fabric](https://github.com/Blockchains/fabric/tree/main) | [Codespaces](https://codespaces.new/Blockchains/fabric?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/fabric.json) (154) |
| [fabric-samples](https://github.com/hyperledger/fabric-samples) | Samples for Hyperledger Fabric | Apache-2.0 | 3020 | [Blockchains/fabric-samples](https://github.com/Blockchains/fabric-samples/tree/main) | [Codespaces](https://codespaces.new/Blockchains/fabric-samples?quickstart=1) |
| [FISCO-BCOS](https://github.com/FISCO-BCOS/FISCO-BCOS) | FISCO BCOS（发音为/ˈfɪskl bi:ˈkɒz/）是一个稳定、高效、安全的许可区块链平台，已被广泛应用于现实的行业应用。截至目前，已拥有5000多家企事业单位，400多个产业数字化标杆应用，涵盖文化版权、司法服务、政府服务、物联网、金融、智慧社区、房地产建设、社区治理 | Apache-2.0 | 2608 | [Blockchains/FISCO-BCOS](https://github.com/Blockchains/FISCO-BCOS/tree/master) | [Codespaces](https://codespaces.new/Blockchains/FISCO-BCOS?quickstart=1) |

## Ethereum & EVM specs

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [EIPs](https://github.com/ethereum/EIPs) | The Ethereum Improvement Proposal repository | CC0-1.0 | 13993 | [Blockchains/EIPs](https://github.com/Blockchains/EIPs/tree/master) | [Codespaces](https://codespaces.new/Blockchains/EIPs?quickstart=1) |
| [ethereum-org-website](https://github.com/ethereum/ethereum-org-website) | Ethereum.org is a primary online resource for the Ethereum community. | MIT | 5976 | [Blockchains/ethereum-org-website](https://github.com/Blockchains/ethereum-org-website/tree/dev) | [Codespaces](https://codespaces.new/Blockchains/ethereum-org-website?quickstart=1) |
| [PoWFaucet](https://github.com/pk910/PoWFaucet) | Modularized faucet for EVM chains with different protection methods (Captcha, Mining, IP, Mainnet Balance, Gitcoin Passport and more) | AGPL-3.0 | 5631 | [Blockchains/PoWFaucet](https://github.com/Blockchains/PoWFaucet/tree/master) | [Codespaces](https://codespaces.new/Blockchains/PoWFaucet?quickstart=1) |
| [consensus-specs](https://github.com/ethereum/consensus-specs) | Ethereum Consensus Specifications | CC0-1.0 | 3966 | [Blockchains/consensus-specs](https://github.com/Blockchains/consensus-specs/tree/master) | [Codespaces](https://codespaces.new/Blockchains/consensus-specs?quickstart=1) |
| [remix-ide](https://github.com/remix-project-org/remix-ide) | Documentation for Remix IDE | Apache-2.0 | 2352 | [Blockchains/remix-ide](https://github.com/Blockchains/remix-ide/tree/master) | [Codespaces](https://codespaces.new/Blockchains/remix-ide?quickstart=1) |
| [execution-specs](https://github.com/ethereum/execution-specs) | Specification for the Execution Layer. Tracking network upgrades. | CC0-1.0 | 1194 | [Blockchains/execution-specs](https://github.com/Blockchains/execution-specs/tree/forks/amsterdam) | [Codespaces](https://codespaces.new/Blockchains/execution-specs?quickstart=1) |
| [execution-apis](https://github.com/ethereum/execution-apis) | Collection of APIs provided by Ethereum execution layer clients | CC0-1.0 | 1136 | [Blockchains/execution-apis](https://github.com/Blockchains/execution-apis/tree/main) | [Codespaces](https://codespaces.new/Blockchains/execution-apis?quickstart=1) |
| [intellij-solidity](https://github.com/intellij-solidity/intellij-solidity) | Solidity plugin for IntelliJ | MIT | 1099 | [Blockchains/intellij-solidity](https://github.com/Blockchains/intellij-solidity/tree/master) | [Codespaces](https://codespaces.new/Blockchains/intellij-solidity?quickstart=1) |

## Hedera / Hiero

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [standards-sdk](https://github.com/hashgraph-online/standards-sdk) | The official HOL Standards SDK, implementing the standards found in https://hol.org/docs/standards | Apache-2.0 | 1240 | [Blockchains/standards-sdk](https://github.com/Blockchains/standards-sdk/tree/main) | [Codespaces](https://codespaces.new/Blockchains/standards-sdk?quickstart=1) |
| [hiero-consensus-node](https://github.com/hiero-ledger/hiero-consensus-node) | Crypto, token, consensus, file, and smart contract services for a Hiero based network | Apache-2.0 | 410 | [Blockchains/hiero-consensus-node](https://github.com/Blockchains/hiero-consensus-node/tree/main) | [Codespaces](https://codespaces.new/Blockchains/hiero-consensus-node?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/hiero-consensus-node.json) (424) |
| [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) | A JavaScript/TypeScript SDK for Hiero: A Javascript toolkit for creating, updating, and interacting with on-ledger assets and smart contract | Apache-2.0 | 330 | [Blockchains/hiero-sdk-js](https://github.com/Blockchains/hiero-sdk-js/tree/main) | [Codespaces](https://codespaces.new/Blockchains/hiero-sdk-js?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/hedera-token-sdk) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/hiero-sdk-js.json) (5) |
| [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node) | Hiero Mirror Node archives data from consensus nodes and serves it via an API | Apache-2.0 | 186 | [Blockchains/hiero-mirror-node](https://github.com/Blockchains/hiero-mirror-node/tree/main) | [Codespaces](https://codespaces.new/Blockchains/hiero-mirror-node?quickstart=1) |
| [hiero-json-rpc-relay](https://github.com/hiero-ledger/hiero-json-rpc-relay) | Implementation of Ethereum JSON-RPC APIs for Hedera | Apache-2.0 | 92 | [Blockchains/hiero-json-rpc-relay](https://github.com/Blockchains/hiero-json-rpc-relay/tree/main) | [Codespaces](https://codespaces.new/Blockchains/hiero-json-rpc-relay?quickstart=1) |
| [hedera-smart-contracts](https://github.com/hashgraph/hedera-smart-contracts) | Contains Hedera Smart Contract Service supporting files | Apache-2.0 | 64 | [Blockchains/hedera-smart-contracts](https://github.com/Blockchains/hedera-smart-contracts/tree/main) | [Codespaces](https://codespaces.new/Blockchains/hedera-smart-contracts?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/hedera-token-sdk) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/hedera-smart-contracts.json) (164) |

## Identity

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [amethyst](https://github.com/vitorpamplona/amethyst) | Nostr client for Android | MIT | 1607 | [Blockchains/amethyst](https://github.com/Blockchains/amethyst/tree/main) | [Codespaces](https://codespaces.new/Blockchains/amethyst?quickstart=1) |
| [semaphore](https://github.com/semaphore-protocol/semaphore) | A zero-knowledge protocol for anonymous interactions. | MIT | 1088 | [Blockchains/semaphore](https://github.com/Blockchains/semaphore/tree/main) | [Codespaces](https://codespaces.new/Blockchains/semaphore?quickstart=1) |

## Indexing & data

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [graph-node](https://github.com/graphprotocol/graph-node) | Graph Node indexes data from blockchains such as Ethereum and serves it over GraphQL | Apache-2.0 | 3153 | [Blockchains/graph-node](https://github.com/Blockchains/graph-node/tree/master) | [Codespaces](https://codespaces.new/Blockchains/graph-node?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/graph-node.json) (20) |
| [squid-sdk](https://github.com/subsquid/squid-sdk) | TypeScript ETL toolkit for indexing Ethereum, Solana, and Substrate data, sourced from SQD Network. | Apache-2.0 | 1339 | [Blockchains/squid-sdk](https://github.com/Blockchains/squid-sdk/tree/master) | [Codespaces](https://codespaces.new/Blockchains/squid-sdk?quickstart=1) |
| [ponder](https://github.com/ponder-sh/ponder) | The backend framework for crypto apps | MIT | 1147 | [Blockchains/ponder](https://github.com/Blockchains/ponder/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ponder?quickstart=1) |
| [trueblocks-core](https://github.com/TrueBlocks/trueblocks-core) | The main repository for the TrueBlocks system | GPL-3.0 | 1095 | [Blockchains/trueblocks-core](https://github.com/Blockchains/trueblocks-core/tree/main) | [Codespaces](https://codespaces.new/Blockchains/trueblocks-core?quickstart=1) |
| [graph-tooling](https://github.com/graphprotocol/graph-tooling) | Monorepo for various tools used by subgraph developers. | Apache-2.0 | 424 | [Blockchains/graph-tooling](https://github.com/Blockchains/graph-tooling/tree/main) | [Codespaces](https://codespaces.new/Blockchains/graph-tooling?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/graph-tooling.json) (2) |

## L2s & rollups

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [optimism](https://github.com/ethereum-optimism/optimism) | Optimism is Ethereum, scaled. | MIT | 6476 | [Blockchains/optimism](https://github.com/Blockchains/optimism/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/optimism?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/optimism.json) (485) |
| [taiko-mono](https://github.com/taikoxyz/taiko-mono) | A based rollup protocol for Ethereum🥁 | MIT | 4557 | [Blockchains/taiko-mono](https://github.com/Blockchains/taiko-mono/tree/main) | [Codespaces](https://codespaces.new/Blockchains/taiko-mono?quickstart=1) |
| [zksync-era](https://github.com/matter-labs/zksync-era) | zkSync era | Apache-2.0 | 3236 | [Blockchains/zksync-era](https://github.com/Blockchains/zksync-era/tree/main) | [Codespaces](https://codespaces.new/Blockchains/zksync-era?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/zksync-era.json) (175) |
| [arbitrum-classic](https://github.com/OffchainLabs/arbitrum-classic) | Powers fast, private, decentralized applications | Apache-2.0 | 2002 | [Blockchains/arbitrum-classic](https://github.com/Blockchains/arbitrum-classic/tree/master) | [Codespaces](https://codespaces.new/Blockchains/arbitrum-classic?quickstart=1) |
| [simple-taiko-node](https://github.com/taikoxyz/simple-taiko-node) | Start your Taiko node with a single command.  🌐 | MIT | 1110 | [Blockchains/simple-taiko-node](https://github.com/Blockchains/simple-taiko-node/tree/main) | [Codespaces](https://codespaces.new/Blockchains/simple-taiko-node?quickstart=1) |
| [stylus-sdk-rs](https://github.com/OffchainLabs/stylus-sdk-rs) | Rust Smart Contracts on Arbitrum | Apache-2.0 OR MIT | 325 | [Blockchains/stylus-sdk-rs](https://github.com/Blockchains/stylus-sdk-rs/tree/main) | [Codespaces](https://codespaces.new/Blockchains/stylus-sdk-rs?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/stylus-sdk-rs.json) (19) |

## Languages & compilers

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [solidity](https://github.com/argotorg/solidity) | Solidity, the Smart Contract Programming Language | GPL-3.0 | 25745 | [Blockchains/solidity](https://github.com/Blockchains/solidity/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/solidity?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/solidity.json) (0) |
| [vyper](https://github.com/vyperlang/vyper) | Pythonic Smart Contract Language for the EVM | Apache-2.0 | 5184 | [Blockchains/vyper](https://github.com/Blockchains/vyper/tree/master) | [Codespaces](https://codespaces.new/Blockchains/vyper?quickstart=1) |
| [cairo](https://github.com/starkware-libs/cairo) | Cairo is the first Turing-complete language for creating provable programs for general computation. | Apache-2.0 | 1908 | [Blockchains/cairo](https://github.com/Blockchains/cairo/tree/main) | [Codespaces](https://codespaces.new/Blockchains/cairo?quickstart=1) |
| [fe](https://github.com/argotorg/fe) | Emerging smart contract language for the Ethereum blockchain. | Apache-2.0 | 1732 | [Blockchains/fe](https://github.com/Blockchains/fe/tree/master) | [Codespaces](https://codespaces.new/Blockchains/fe?quickstart=1) |
| [plutus](https://github.com/IntersectMBO/plutus) | The Plutus language implementation and tools | Apache-2.0 | 1632 | [Blockchains/plutus](https://github.com/Blockchains/plutus/tree/master) | [Codespaces](https://codespaces.new/Blockchains/plutus?quickstart=1) |
| [solc-js](https://github.com/argotorg/solc-js) | Javascript bindings for the Solidity compiler | MIT | 1508 | [Blockchains/solc-js](https://github.com/Blockchains/solc-js/tree/master) | [Codespaces](https://codespaces.new/Blockchains/solc-js?quickstart=1) |
| [solang](https://github.com/hyperledger-solang/solang) | Solidity Compiler for Solana, Polkadot and Stellar | Apache-2.0 | 1383 | [Blockchains/solang](https://github.com/Blockchains/solang/tree/main) | [Codespaces](https://codespaces.new/Blockchains/solang?quickstart=1) |

## Move (Sui/Aptos)

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [sui](https://github.com/MystenLabs/sui) | Sui, a next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Mov | Apache-2.0 | 7763 | [Blockchains/sui](https://github.com/Blockchains/sui/tree/main) | [Codespaces](https://codespaces.new/Blockchains/sui?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/sui.json) (556) |
| [starcoin](https://github.com/starcoinorg/starcoin) | Starcoin - A Move smart contract blockchain network that scales by layering | Apache-2.0 | 1152 | [Blockchains/starcoin](https://github.com/Blockchains/starcoin/tree/dual-verse-dag) | [Codespaces](https://codespaces.new/Blockchains/starcoin?quickstart=1) |

## NFTs

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [seaport](https://github.com/ProjectOpenSea/seaport) | Seaport is a marketplace protocol for safely and efficiently buying and selling NFTs. | MIT | 2256 | [Blockchains/seaport](https://github.com/Blockchains/seaport/tree/main) | [Codespaces](https://codespaces.new/Blockchains/seaport?quickstart=1) |

## Oracles

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [chainlink](https://github.com/smartcontractkit/chainlink) | node of the decentralized oracle network, bridging on and off-chain computation | MIT (portions BUSL-1.1: CCIP, workflows; see LICENSE) | 8248 | [Blockchains/chainlink](https://github.com/Blockchains/chainlink/tree/upstream-develop) | [Codespaces](https://codespaces.new/Blockchains/chainlink?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/chainlink-price-feed) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/chainlink.json) (160) |
| [chainlink-evm](https://github.com/smartcontractkit/chainlink-evm) |  | MIT (portions other licences; see LICENSE) | 83 | [Blockchains/chainlink-evm](https://github.com/Blockchains/chainlink-evm/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/chainlink-evm?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/chainlink-price-feed) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/chainlink-evm.json) (432) |

## P2P & storage

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [kubo](https://github.com/ipfs/kubo) | IPFS implementation in Go: a daemon that stores and serves content-addressed data, with a CLI, HTTP Gateway, and RPC API | MIT OR Apache-2.0 | 17146 | [Blockchains/kubo](https://github.com/Blockchains/kubo/tree/master) | [Codespaces](https://codespaces.new/Blockchains/kubo?quickstart=1) |
| [go-libp2p](https://github.com/libp2p/go-libp2p) | libp2p implementation in Go | MIT | 6885 | [Blockchains/go-libp2p](https://github.com/Blockchains/go-libp2p/tree/master) | [Codespaces](https://codespaces.new/Blockchains/go-libp2p?quickstart=1) |
| [ipfs-desktop](https://github.com/ipfs/ipfs-desktop) | An unobtrusive and user-friendly desktop application for IPFS on Windows, Mac and Linux. | MIT | 6591 | [Blockchains/ipfs-desktop](https://github.com/Blockchains/ipfs-desktop/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ipfs-desktop?quickstart=1) |
| [rust-libp2p](https://github.com/libp2p/rust-libp2p) | The Rust Implementation of the libp2p networking stack. | MIT | 5616 | [Blockchains/rust-libp2p](https://github.com/Blockchains/rust-libp2p/tree/master) | [Codespaces](https://codespaces.new/Blockchains/rust-libp2p?quickstart=1) |
| [lotus](https://github.com/filecoin-project/lotus) | Reference implementation of the Filecoin protocol, written in Go | MIT OR Apache-2.0 | 2987 | [Blockchains/lotus](https://github.com/Blockchains/lotus/tree/master) | [Codespaces](https://codespaces.new/Blockchains/lotus?quickstart=1) |
| [js-libp2p](https://github.com/libp2p/js-libp2p) | A JavaScript Implementation of libp2p networking stack. | Apache-2.0 | 2580 | [Blockchains/js-libp2p](https://github.com/Blockchains/js-libp2p/tree/main) | [Codespaces](https://codespaces.new/Blockchains/js-libp2p?quickstart=1) |
| [ipfs-companion](https://github.com/ipfs/ipfs-companion) | Browser extension that routes ipfs:// addresses and content-addressed websites through your own local IPFS node | CC0-1.0 | 2162 | [Blockchains/ipfs-companion](https://github.com/Blockchains/ipfs-companion/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ipfs-companion?quickstart=1) |
| [ipfs-webui](https://github.com/ipfs/ipfs-webui) | A frontend for an IPFS Kubo and IPFS Desktop | MIT | 1633 | [Blockchains/ipfs-webui](https://github.com/Blockchains/ipfs-webui/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ipfs-webui?quickstart=1) |
| [bee](https://github.com/ethersphere/bee) | Bee is a Swarm client implemented in Go. It’s the basic building block for the Swarm network: a private; decentralized; and self-sustaining  | BSD-3-Clause | 1483 | [Blockchains/bee](https://github.com/Blockchains/bee/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bee?quickstart=1) |
| [holochain](https://github.com/holochain/holochain) | The current, performant & industrial strength version of Holochain on Rust. | CAL-1.0 (OSI-approved) | 1395 | [Blockchains/holochain](https://github.com/Blockchains/holochain/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/holochain?quickstart=1) |
| [helia](https://github.com/ipfs/helia) | An implementation of IPFS in TypeScript | Apache-2.0 | 1352 | [Blockchains/helia](https://github.com/Blockchains/helia/tree/main) | [Codespaces](https://codespaces.new/Blockchains/helia?quickstart=1) |

## Payments

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [btcpayserver](https://github.com/btcpayserver/btcpayserver) | Accept Bitcoin payments. Free, open-source & self-hosted, Bitcoin payment processor. | MIT | 7783 | [Blockchains/btcpayserver](https://github.com/Blockchains/btcpayserver/tree/master) | [Codespaces](https://codespaces.new/Blockchains/btcpayserver?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/btcpayserver.json) (0) |

## Polkadot / Substrate

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [polkadot-sdk](https://github.com/paritytech/polkadot-sdk) | The Parity Polkadot Blockchain SDK | Apache-2.0 / GPL-3.0-with-Classpath (per crate) | 2811 | [Blockchains/polkadot-sdk](https://github.com/Blockchains/polkadot-sdk/tree/master) | [Codespaces](https://codespaces.new/Blockchains/polkadot-sdk?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/polkadot-sdk.json) (404) |
| [apps](https://github.com/polkadot-js/apps) | Basic Polkadot/Substrate UI for interacting with a Polkadot and Substrate node. This is the main user-facing application, allowing access to | Apache-2.0 | 1822 | [Blockchains/apps](https://github.com/Blockchains/apps/tree/master) | [Codespaces](https://codespaces.new/Blockchains/apps?quickstart=1) |
| [api](https://github.com/polkadot-js/api) | Promise and RxJS APIs around Polkadot and Substrate based chains via RPC calls. It is dynamically generated based on what the Substrate runt | Apache-2.0 | 1111 | [Blockchains/api](https://github.com/Blockchains/api/tree/master) | [Codespaces](https://codespaces.new/Blockchains/api?quickstart=1) |
| [extension](https://github.com/polkadot-js/extension) | Simple browser extension for managing Polkadot and Substrate network accounts in a browser. Allows the signing of extrinsics using these acc | Apache-2.0 | 1019 | [Blockchains/extension-1](https://github.com/Blockchains/extension-1/tree/master) | [Codespaces](https://codespaces.new/Blockchains/extension-1?quickstart=1) |

## Security & analysis

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) | Reproduce DeFi hacked incidents using Foundry. | Apache-2.0 | 6803 | [Blockchains/DeFiHackLabs](https://github.com/Blockchains/DeFiHackLabs/tree/main) | [Codespaces](https://codespaces.new/Blockchains/DeFiHackLabs?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/defihacklabs.json) (1) |
| [slither](https://github.com/crytic/slither) | Static Analyzer for Solidity and Vyper | AGPL-3.0 | 6375 | [Blockchains/slither](https://github.com/Blockchains/slither/tree/master) | [Codespaces](https://codespaces.new/Blockchains/slither?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/slither.json) (7) |
| [echidna](https://github.com/crytic/echidna) | Ethereum smart contract fuzzer | AGPL-3.0 | 3185 | [Blockchains/echidna](https://github.com/Blockchains/echidna/tree/master) | [Codespaces](https://codespaces.new/Blockchains/echidna?quickstart=1) |
| [ethernaut](https://github.com/OpenZeppelin/ethernaut) | Web3/Solidity based wargame | AGPL-3.0 | 2337 | [Blockchains/ethernaut](https://github.com/Blockchains/ethernaut/tree/master) | [Codespaces](https://codespaces.new/Blockchains/ethernaut?quickstart=1) |
| [reentrancy-attacks](https://github.com/pcaversaccio/reentrancy-attacks) | A chronological and (hopefully) complete list of reentrancy attacks to date. | AGPL-3.0 | 1629 | [Blockchains/reentrancy-attacks](https://github.com/Blockchains/reentrancy-attacks/tree/main) | [Codespaces](https://codespaces.new/Blockchains/reentrancy-attacks?quickstart=1) |
| [heimdall-rs](https://github.com/Jon-Becker/heimdall-rs) | Heimdall is an advanced EVM smart contract toolkit specializing in bytecode analysis and extracting information from unverified contracts. | MIT | 1619 | [Blockchains/heimdall-rs](https://github.com/Blockchains/heimdall-rs/tree/main) | [Codespaces](https://codespaces.new/Blockchains/heimdall-rs?quickstart=1) |
| [solhint](https://github.com/protofire/solhint) | Solhint is an open-source project to provide a linting utility for Solidity code. | MIT | 1127 | [Blockchains/solhint](https://github.com/Blockchains/solhint/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/solhint?quickstart=1) |

## Smart-contract libraries

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | OpenZeppelin Contracts is a library for secure smart contract development. | MIT | 27265 | [Blockchains/openzeppelin-contracts](https://github.com/Blockchains/openzeppelin-contracts/tree/master) | [Codespaces](https://codespaces.new/Blockchains/openzeppelin-contracts?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/foundry-oz-tokens) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/openzeppelin-contracts.json) (268) |
| [solady](https://github.com/Vectorized/solady) | Optimized Solidity snippets. | MIT | 3379 | [Blockchains/solady](https://github.com/Blockchains/solady/tree/main) | [Codespaces](https://codespaces.new/Blockchains/solady?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/solady.json) (149) |
| [safe-smart-account](https://github.com/safe-fndn/safe-smart-account) | Safe allows secure management of blockchain assets. | LGPL-3.0 | 2182 | [Blockchains/safe-smart-account](https://github.com/Blockchains/safe-smart-account/tree/main) | [Codespaces](https://codespaces.new/Blockchains/safe-smart-account?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/safe-smart-account.json) (66) |
| [openzeppelin-contracts-upgradeable](https://github.com/OpenZeppelin/openzeppelin-contracts-upgradeable) | Upgradeable variant of OpenZeppelin Contracts, meant for use in upgradeable contracts. | MIT | 1176 | [Blockchains/openzeppelin-contracts-upgradeable](https://github.com/Blockchains/openzeppelin-contracts-upgradeable/tree/master) | [Codespaces](https://codespaces.new/Blockchains/openzeppelin-contracts-upgradeable?quickstart=1) |
| [prb-math](https://github.com/PaulRBerg/prb-math) | Solidity library for advanced fixed-point math | MIT | 1008 | [Blockchains/prb-math](https://github.com/Blockchains/prb-math/tree/main) | [Codespaces](https://codespaces.new/Blockchains/prb-math?quickstart=1) |

## Solana

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [anchor](https://github.com/otter-sec/anchor) | ⚓ Solana Program Framework | Apache-2.0 | 5141 | [Blockchains/anchor](https://github.com/Blockchains/anchor/tree/master) | [Codespaces](https://codespaces.new/Blockchains/anchor?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/anchor.json) (54) |
| [solana-web3.js](https://github.com/solana-foundation/solana-web3.js) | Solana JavaScript SDK | MIT | 2765 | [Blockchains/solana-web3.js](https://github.com/Blockchains/solana-web3.js/tree/main) | [Codespaces](https://codespaces.new/Blockchains/solana-web3.js?quickstart=1) |
| [wallet-adapter](https://github.com/anza-xyz/wallet-adapter) | Modular TypeScript wallet adapters and components for Solana applications. | Apache-2.0 | 2030 | [Blockchains/wallet-adapter](https://github.com/Blockchains/wallet-adapter/tree/master) | [Codespaces](https://codespaces.new/Blockchains/wallet-adapter?quickstart=1) |
| [pay](https://github.com/solana-foundation/pay) | CLI for Agentic payments (x402, MPP, AP2). | MIT | 1785 | [Blockchains/pay](https://github.com/Blockchains/pay/tree/main) | [Codespaces](https://codespaces.new/Blockchains/pay?quickstart=1) |
| [solana-go](https://github.com/solana-foundation/solana-go) | Go SDK library and RPC client for the Solana Blockchain | Apache-2.0 | 1591 | [Blockchains/solana-go](https://github.com/Blockchains/solana-go/tree/main) | [Codespaces](https://codespaces.new/Blockchains/solana-go?quickstart=1) |
| [firedancer](https://github.com/firedancer-io/firedancer) | Firedancer is Jump Crypto's Solana validator software. | Apache-2.0 | 1525 | [Blockchains/firedancer](https://github.com/Blockchains/firedancer/tree/main) | [Codespaces](https://codespaces.new/Blockchains/firedancer?quickstart=1) |
| [solana-py](https://github.com/michaelhly/solana-py) | Solana Python SDK | MIT | 1446 | [Blockchains/solana-py](https://github.com/Blockchains/solana-py/tree/master) | [Codespaces](https://codespaces.new/Blockchains/solana-py?quickstart=1) |
| [program-examples](https://github.com/solana-foundation/program-examples) | A repository of Solana program examples | MIT | 1427 | [Blockchains/program-examples](https://github.com/Blockchains/program-examples/tree/main) | [Codespaces](https://codespaces.new/Blockchains/program-examples?quickstart=1) |
| [yellowstone-grpc](https://github.com/rpcpool/yellowstone-grpc) | Triton's Dragon's Mouth Yellowstone gRPC service for high-performance Solana streaming | AGPL-3.0 | 1008 | [Blockchains/yellowstone-grpc](https://github.com/Blockchains/yellowstone-grpc/tree/master) | [Codespaces](https://codespaces.new/Blockchains/yellowstone-grpc?quickstart=1) |

## Wallets

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [electrum](https://github.com/spesmilo/electrum) | Electrum Bitcoin Wallet | MIT | 8609 | [Blockchains/electrum](https://github.com/Blockchains/electrum/tree/master) | [Codespaces](https://codespaces.new/Blockchains/electrum?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/electrum.json) (0) |
| [rainbow](https://github.com/rainbow-me/rainbow) | 🌈‒ the Ethereum wallet that lives in your pocket | GPL-3.0 | 4396 | [Blockchains/rainbow](https://github.com/Blockchains/rainbow/tree/develop) | [Codespaces](https://codespaces.new/Blockchains/rainbow?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/rainbow.json) (1) |
| [wallet](https://github.com/bitpay/wallet) | Bitpay Wallet (formerly Copay) is a secure Bitcoin and other crypto currencies wallet platform for both desktop and mobile devices. | MIT | 3942 | [Blockchains/wallet](https://github.com/Blockchains/wallet/tree/master) | [Codespaces](https://codespaces.new/Blockchains/wallet?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/wallet.json) (1) |
| [wallet-core](https://github.com/trustwallet/wallet-core) | Cross-platform, cross-blockchain wallet library. | Apache-2.0 | 3571 | [Blockchains/wallet-core](https://github.com/Blockchains/wallet-core/tree/master) | [Codespaces](https://codespaces.new/Blockchains/wallet-core?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/wallet-core.json) (118) |
| [BlueWallet](https://github.com/BlueWallet/BlueWallet) | Bitcoin wallet for iOS & Android. Built with React Native | MIT | 3309 | [Blockchains/BlueWallet](https://github.com/Blockchains/BlueWallet/tree/master) | [Codespaces](https://codespaces.new/Blockchains/BlueWallet?quickstart=1) |
| [extension](https://github.com/tahowallet/extension) | Taho, the community owned and operated Web3 wallet. | GPL-3.0 | 3204 | [Blockchains/extension](https://github.com/Blockchains/extension/tree/main) | [Codespaces](https://codespaces.new/Blockchains/extension?quickstart=1) |
| [rainbowkit](https://github.com/rainbow-me/rainbowkit) | The best way to connect a wallet 🌈 🧰 | MIT | 2835 | [Blockchains/rainbowkit](https://github.com/Blockchains/rainbowkit/tree/main) | [Codespaces](https://codespaces.new/Blockchains/rainbowkit?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/wagmi-rainbowkit-dapp) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/rainbowkit.json) (4) |
| [WalletWasabi](https://github.com/WalletWasabi/WalletWasabi) | Open-source, non-custodial, privacy preserving Bitcoin wallet for Windows, Linux, and Mac. | MIT | 2618 | [Blockchains/WalletWasabi](https://github.com/Blockchains/WalletWasabi/tree/master) | [Codespaces](https://codespaces.new/Blockchains/WalletWasabi?quickstart=1) |
| [sparrow](https://github.com/sparrowwallet/sparrow) | Desktop Bitcoin Wallet focused on security and privacy. Free and open source. | Apache-2.0 | 2154 | [Blockchains/sparrow](https://github.com/Blockchains/sparrow/tree/master) | [Codespaces](https://codespaces.new/Blockchains/sparrow?quickstart=1) |
| [cake_wallet](https://github.com/cake-tech/cake_wallet) | The open source repository for Cake Wallet, a noncustodial multi-currency wallet, and Monero.com, a noncustodial Monero-only wallet. Need he | MIT | 1950 | [Blockchains/cake_wallet](https://github.com/Blockchains/cake_wallet/tree/dev) | [Codespaces](https://codespaces.new/Blockchains/cake_wallet?quickstart=1) |
| [coinbase-wallet-sdk](https://github.com/coinbase/coinbase-wallet-sdk) | An open protocol that lets users connect their mobile wallets to your DApp | MIT | 1764 | [Blockchains/coinbase-wallet-sdk](https://github.com/Blockchains/coinbase-wallet-sdk/tree/master) | [Codespaces](https://codespaces.new/Blockchains/coinbase-wallet-sdk?quickstart=1) |
| [MyEtherWallet](https://github.com/MyEtherWallet/MyEtherWallet) | MyEtherWallet (our friends call us MEW) is a free, client-side interface helping you interact with the Ethereum blockchain. | MIT | 1588 | [Blockchains/MyEtherWallet](https://github.com/Blockchains/MyEtherWallet/tree/main) | [Codespaces](https://codespaces.new/Blockchains/MyEtherWallet?quickstart=1) |
| [daedalus](https://github.com/input-output-hk/daedalus) | The open source cryptocurrency wallet for ada, built to grow with the community | Apache-2.0 | 1247 | [Blockchains/daedalus](https://github.com/Blockchains/daedalus/tree/master) | [Codespaces](https://codespaces.new/Blockchains/daedalus?quickstart=1) |
| [bip39](https://github.com/bitcoinjs/bip39) | JavaScript implementation of Bitcoin BIP39: Mnemonic code for generating deterministic keys | ISC | 1182 | [Blockchains/bip39](https://github.com/Blockchains/bip39/tree/master) | [Codespaces](https://codespaces.new/Blockchains/bip39?quickstart=1) |
| [ant-design-web3](https://github.com/ant-design/ant-design-web3) | 🥳 Efficient react components for building dapps easier \| Connect crypto wallets and more Web3 UI components \| Web3 icons \| Supports Ether | MIT | 1147 | [Blockchains/ant-design-web3](https://github.com/Blockchains/ant-design-web3/tree/main) | [Codespaces](https://codespaces.new/Blockchains/ant-design-web3?quickstart=1) |
| [connectkit](https://github.com/family/connectkit) | Connecting a wallet, made simple. | BSD-2-Clause | 1070 | [Blockchains/connectkit](https://github.com/Blockchains/connectkit/tree/main) | [Codespaces](https://codespaces.new/Blockchains/connectkit?quickstart=1) |

## Zero knowledge

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [union](https://github.com/unionlabs/union) | The trust-minimized, zero-knowledge bridging protocol, designed for censorship resistance, extremely high security, and usage in decentraliz | Apache-2.0 | 73779 | [Blockchains/union](https://github.com/Blockchains/union/tree/main) | [Codespaces](https://codespaces.new/Blockchains/union?quickstart=1) |
| [leo](https://github.com/ProvableHQ/leo) | 🦁 The Leo Programming Language. A Programming Language for Formally Verified, Zero-Knowledge Applications | GPL-3.0 | 4822 | [Blockchains/leo](https://github.com/Blockchains/leo/tree/master) | [Codespaces](https://codespaces.new/Blockchains/leo?quickstart=1) |
| [snarkOS](https://github.com/ProvableHQ/snarkOS) | A Decentralized Operating System for ZK Applications | Apache-2.0 | 4528 | [Blockchains/snarkOS](https://github.com/Blockchains/snarkOS/tree/staging) | [Codespaces](https://codespaces.new/Blockchains/snarkOS?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/snarkos.json) (21) |
| [risc0](https://github.com/risc0/risc0) | RISC Zero is a zero-knowledge verifiable general computing platform based on zk-STARKs and the RISC-V microarchitecture. | Apache-2.0 | 2196 | [Blockchains/risc0](https://github.com/Blockchains/risc0/tree/main) | [Codespaces](https://codespaces.new/Blockchains/risc0?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/risc0.json) (74) |
| [mina](https://github.com/MinaProtocol/mina) | Mina is a cryptocurrency protocol with a constant size blockchain, improving scaling while maintaining decentralization and security. | Apache-2.0 | 2123 | [Blockchains/mina](https://github.com/Blockchains/mina/tree/compatible) | [Codespaces](https://codespaces.new/Blockchains/mina?quickstart=1) |
| [snarkjs](https://github.com/iden3/snarkjs) | zkSNARK implementation in JavaScript & WASM | GPL-3.0 | 2041 | [Blockchains/snarkjs](https://github.com/Blockchains/snarkjs/tree/master) | [Codespaces](https://codespaces.new/Blockchains/snarkjs?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/circom-zk-proof) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/snarkjs.json) (1) |
| [sp1](https://github.com/succinctlabs/sp1) | SP1 is a zero‑knowledge virtual machine that proves the correct execution of programs compiled for the RISC-V architecture. | Apache-2.0 | 1739 | [Blockchains/sp1](https://github.com/Blockchains/sp1/tree/main) | [Codespaces](https://codespaces.new/Blockchains/sp1?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/sp1.json) (159) |
| [gnark](https://github.com/Consensys-Incorporated/gnark) | gnark is a fast zk-SNARK library that offers a high-level API to design circuits. The library is open source and developed under the Apache  | Apache-2.0 | 1738 | [Blockchains/gnark](https://github.com/Blockchains/gnark/tree/master) | [Codespaces](https://codespaces.new/Blockchains/gnark?quickstart=1) |
| [circom](https://github.com/iden3/circom) | zkSnark circuit compiler | GPL-3.0 | 1696 | [Blockchains/circom](https://github.com/Blockchains/circom/tree/master) | [Codespaces](https://codespaces.new/Blockchains/circom?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/circom-zk-proof) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/circom.json) (12) |
| [noir](https://github.com/noir-lang/noir) | Noir is a domain specific language for zero knowledge proofs | Apache-2.0 | 1405 | [Blockchains/noir](https://github.com/Blockchains/noir/tree/master) | [Codespaces](https://codespaces.new/Blockchains/noir?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/noir-zk-proof) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/noir.json) (529) |
| [darkfi](https://github.com/darkrenaissance/darkfi) | Anonymous. Uncensored. Sovereign. | AGPL-3.0 | 1373 | [Blockchains/darkfi](https://github.com/Blockchains/darkfi/tree/master) | [Codespaces](https://codespaces.new/Blockchains/darkfi?quickstart=1) |
| [cairo-lang](https://github.com/starkware-libs/cairo-lang) |  | Apache-2.0 | 1368 | [Blockchains/cairo-lang](https://github.com/Blockchains/cairo-lang/tree/master) | [Codespaces](https://codespaces.new/Blockchains/cairo-lang?quickstart=1) |
| [snarkVM](https://github.com/ProvableHQ/snarkVM) | A zkVM for Decentralized Private Computations (DPC) | Apache-2.0 | 1165 | [Blockchains/snarkVM](https://github.com/Blockchains/snarkVM/tree/staging) | [Codespaces](https://codespaces.new/Blockchains/snarkVM?quickstart=1) |
| [jolt](https://github.com/a16z/jolt) | The simplest and most extensible zkVM. Fast and fully open source from a16z crypto and friends. ⚡ | Apache-2.0 | 1047 | [Blockchains/jolt](https://github.com/Blockchains/jolt/tree/main) | [Codespaces](https://codespaces.new/Blockchains/jolt?quickstart=1) |
| [circomlib](https://github.com/iden3/circomlib) | Library of basic circuits for circom | LGPL-3.0 | 750 | [Blockchains/circomlib](https://github.com/Blockchains/circomlib/tree/master) | [Codespaces](https://codespaces.new/Blockchains/circomlib?quickstart=1) · [Starter](https://github.com/Blockchains/blockchainlab-starters/tree/main/starters/circom-zk-proof) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/circomlib.json) (109) |

## Extended
Further Blockchains forks that are indexed in [blockchainlab-index](https://github.com/Blockchains/blockchainlab-index) (`tier: extended`) but sit outside the curated criteria above, usually because they have fewer than 1,000 stars or were last active more than 90 days ago. **What gets in:** blockchain or crypto upstream, an OSI-approved licence, upstream pushed within the last 365 days, not archived.

| Project | What | Licence | ★ | Fork | Use |
|---|---|---|---|---|---|
| [zksync](https://github.com/matter-labs/zksync) | zkSync: trustless scaling and privacy engine for Ethereum | Apache-2.0 | 4923 | [Blockchains/zksync](https://github.com/Blockchains/zksync/tree/master) | [Codespaces](https://codespaces.new/Blockchains/zksync?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/zksync.json) (114) |
| [marketplace](https://github.com/decentraland/marketplace) | 🏛️ Decentraland's NFT Marketplace | Apache-2.0 | 1199 | [Blockchains/marketplace](https://github.com/Blockchains/marketplace/tree/master) | [Codespaces](https://codespaces.new/Blockchains/marketplace?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/marketplace.json) (4) |
| [awesome-nft](https://github.com/gianni-dalerta/awesome-nft) | A curated list of awesome Non Fungible Token (NFT, ERC721) frameworks, libraries and software | MIT | 971 | [Blockchains/awesome-nft](https://github.com/Blockchains/awesome-nft/tree/master) | [Codespaces](https://codespaces.new/Blockchains/awesome-nft?quickstart=1) |
| [defi-sdk](https://github.com/zeriontech/defi-sdk) | DeFi SDK Makes Money Lego Work | LGPL-3.0 | 844 | [Blockchains/defi-sdk](https://github.com/Blockchains/defi-sdk/tree/upstream-router) | [Codespaces](https://codespaces.new/Blockchains/defi-sdk?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/defi-sdk.json) (25) |
| [ampleforth-contracts](https://github.com/fragmentsorg/ampleforth-contracts) | Smart contracts for Ampleforth Protocol (working name uFragments) | GPL-3.0 | 280 | [Blockchains/uFragments](https://github.com/Blockchains/uFragments/tree/master) | [Codespaces](https://codespaces.new/Blockchains/uFragments?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/ufragments.json) (21) |
| [ui](https://github.com/decentraland/ui) | 🦄 Decentraland UI | Apache-2.0 | 212 | [Blockchains/ui](https://github.com/Blockchains/ui/tree/master) | [Codespaces](https://codespaces.new/Blockchains/ui?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/ui.json) (1) |
| [builder](https://github.com/decentraland/builder) | 🍉 Build scenes for Decentraland | Apache-2.0 | 157 | [Blockchains/builder](https://github.com/Blockchains/builder/tree/master) | [Codespaces](https://codespaces.new/Blockchains/builder?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/builder.json) (2) |
| [decentraland-dapps](https://github.com/decentraland/decentraland-dapps) | 🛠 Common modules for dApps | Apache-2.0 | 115 | [Blockchains/decentraland-dapps](https://github.com/Blockchains/decentraland-dapps/tree/master) | [Codespaces](https://codespaces.new/Blockchains/decentraland-dapps?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/decentraland-dapps.json) (1) |
| [catalyst](https://github.com/decentraland/catalyst) | 🐧 Content server for Decentraland | Apache-2.0 | 52 | [Blockchains/catalyst](https://github.com/Blockchains/catalyst/tree/upstream-main) | [Codespaces](https://codespaces.new/Blockchains/catalyst?quickstart=1) |
| [synthetix-assets](https://github.com/Synthetixio/synthetix-assets) | Synthetix Assets | MIT | 10 | [Blockchains/synthetix-assets](https://github.com/Blockchains/synthetix-assets/tree/master) | [Codespaces](https://codespaces.new/Blockchains/synthetix-assets?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/synthetix-assets.json) (1) |
| [Soulbyte](https://github.com/web3devz/Soulbyte) | Autonomous AI Life Simulation | MIT | 2 | [Blockchains/Soulbyte](https://github.com/Blockchains/Soulbyte/tree/main) | [Codespaces](https://codespaces.new/Blockchains/Soulbyte?quickstart=1) · [Components](https://raw.githubusercontent.com/Blockchains/blockchainlab-index/main/components/soulbyte.json) (2) |

<!-- blocks:start -->
## Use as a building block

> **For AI agents and builders:** read [`AGENTS.md`](AGENTS.md) (setup, commands, structure, rules), [`llms.txt`](llms.txt) (doc map) and the machine-readable [`blocks.json`](blocks.json) ([schema](https://github.com/Blockchains/.github/blob/main/docs/BLOCKS-SCHEMA.md)). How all Blockchains blocks fit together: **[Build with Blocks](https://github.com/Blockchains/.github/blob/main/docs/BUILD-WITH-BLOCKS.md)** · org catalogue: [https://blockchains.github.io/blocks.json](https://blockchains.github.io/blocks.json).

**What it exports**

| Export | Type | Install / access |
|---|---|---|
| `forge.json` | file | `https://raw.githubusercontent.com/Blockchains/awesome-blockchainlab/main/forge.json` |
| `README.md` | file | `human-readable list by category` |

**Minimal example** (run on 2026-10-04)

```bash
curl -s https://raw.githubusercontent.com/Blockchains/awesome-blockchainlab/main/forge.json \
  | jq -r '.projects[] | select(.category=="oracles") | "\(.fork) \(.license)"'
```

**Inputs → outputs**

- In: none
- Out: `projects[]` (JSON) slug, name, fork, upstream, category, license, license_note, stars, tier, docs, starters, index {components, repo_index, commit, tags}

**Composes with**

- [Blockchains/fork-sync](https://github.com/Blockchains/fork-sync): keeps every listed fork in sync
- [Blockchains/blockchainlab-index](https://github.com/Blockchains/blockchainlab-index): code index of the same forks (projects[].index links)
- [Blockchains/blockchainlab-starters](https://github.com/Blockchains/blockchainlab-starters): starters built on these forks
- [Blockchains/blockchainlab-compose](https://github.com/Blockchains/blockchainlab-compose): composes projects from them

**Versioning & stability:** `stable`. forge.json fields are additive; `generated_at` marks each regeneration. Archived forks are removed from the list.
<!-- blocks:end -->

## Contributing
Open an issue with the upstream URL. Inclusion is checked against the criteria above. `forge.json` is regenerated from the fork state, and the `Validate` workflow checks it on every push.

## Licence
This list: [CC0-1.0](LICENSE). Each listed project keeps its own licence.
