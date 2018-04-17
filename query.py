import threading
import json
import web3
import time
import numpy
from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from web3.contract import ConciseContract
from contractAddress import abi
from contractAddress import contractAddress
from random import *
address=['http://10.1.1.8:8042','http://10.1.1.9:8042','http://10.1.1.10:8042','http://10.1.1.12:8042','http://10.1.1.13:8042','http://10.1.1.14:8042','http://10.1.1.17:8042','http://10.1.1.18:8042','http://10.1.1.21:8042','http://10.1.1.22:8042','http://10.1.1.26:8042','http://10.1.1.29:8042','http://10.1.1.31:8042','http://10.1.1.32:8042','http://10.1.1.38:8042','http://10.1.1.2:8042','http://10.1.1.42:8042','http://10.1.1.50:8042','http://10.1.1.51:8042','http://10.1.1.54:8042']
result={}
start=0
class SingleThread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
	self.index=i

    def run(self):
        w = Web3(HTTPProvider(address[self.index]))
        transactionSearch=w.eth.contract(json.loads(abi), contractAddress, ContractFactoryClass=ConciseContract)
        e.wait()
        time1=time.time()
        result.append(Web3.toInt(transactionSearch.getTransactions(pType,pId,pState)))
        retrieveTime.append(time.time()-start)
        connectTime.append(time1-start)

connectTimeTotal=[]
retrieveTimeTotal=[]
timeTotal=[]
numExp=10000
for j in range(numExp):
    pType=randint(1,20)
    pId=randint(1,2000)
    pState=randint(1,5)
    num=12
    q=sample(range(0,15),num)
    result=[]
    connectTime=[]
    retrieveTime=[]
    e=threading.Event()
    for i in range(num):
        s = SingleThread(q[i])
        s.start()
    start=time.time()
    e.set()
    while len(result)<num:
         a=1
    result_j=max(set(result),key=result.count)
    timeTotal.append(time.time()-start)
    connectTimeTotal.append(connectTime)
    retrieveTimeTotal.append(retrieveTime)
    print j,numpy.mean(numpy.array(retrieveTimeTotal),axis=0),retrieveTimeTotal[j]
print numpy.mean(timeTotal), numpy.mean(numpy.array(connectTimeTotal),axis=0),numpy.mean(numpy.array(retrieveTimeTotal),axis=0)
