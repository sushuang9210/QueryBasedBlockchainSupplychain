#!/bin/bash

geth --identity "miner1" --networkid 42 --datadir "~/ChainSkills/miner1" --nodiscover --mine --rpc --rpcaddr "10.1.1.8" --rpcport "8042" --port "30303" --unlock 0 --password ~/ChainSkills/miner1/password.sec --ipcpath "~/Library/Ethereum/geth.ipc"
