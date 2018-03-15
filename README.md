# QueryBasedBlockchainSupplychain
1. start miner:
cd miner1
./startminer1.sh

2. mine a contract:
node mineContract.js

3. generate supply chain data:
cd dataGenerator
python main.py

4. send supply chain data to blockchain:
node sender.js

5. query:
python query.py

6. smart contract: contract.sol
