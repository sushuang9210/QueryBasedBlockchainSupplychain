import json
import web3
from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from contractAddress import abi
from contractAddress import contractAddress
from random import *
ipAddress=['http://10.1.1.8:8042','http://10.1.1.9:8042','http://10.1.1.10:8042','http://10.1.1.12:8042','http://10.1.1.13:8042','http://10.1.1.14:8042','http://10.1.1.17:8042','http://10.1.1.18:8042','http://10.1.1.21:8042','http://10.1.1.22:8042','http://10.1.1.26:8042','http://10.1.1.31:8042','http://10.1.1.38:8042','http://10.1.1.50:8042','http://10.1.1.29:8042','http://10.1.1.32:8042','http://10.1.1.51:8042','http://10.1.1.54:8042']
w=[]
transactionSearch=[]
for i in range(20):
  w.push(Web3(HTTPProvider(ipAddress[i])))
  transactionSearch.push(w.eth.contract(abi=json.loads(abi),address=contractAddress, ContractFactoryClass=ConciseContract))
f=open('data.txt','r')
for line in f:
    stateValue=line[2]
    if stateValue=='1':
        supplier=int(line[9])
        transactionSearch[supplier].setProduceTransaction(int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8]),transact={'from': w.eth.accounts[0],'gas':1000000})
    else:
        supplier=int(line[6])
        transactionSearch[supplier].setProduceTransaction(int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),transact={'from': w.eth.accounts[0],'gas':1000000})
