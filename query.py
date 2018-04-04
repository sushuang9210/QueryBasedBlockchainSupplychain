"""
__author__ = 'Shuang Su'
__copyright__ = 'Copyright 2018, Shuang Su'
__version__ = '0.1'
__email__ = 'shuangs@andrew.cmu.edu'
"""
import threading
import json
import web3
import time
#import sys
#from io import StringIO

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from web3.contract import ConciseContract
from contractAddress import abi
from contractAddress import contractAddress
address=['http://10.1.1.8:8042','http://10.1.1.9:8042','http://10.1.1.10:8042','http://10.1.1.12:8042','http://10.1.1.13:8042','http://10.1.1.14:8042','http://10.1.1.17:8042','http://10.1.1.18:8042','http://10.1.1.21:8042','http://10.1.1.22:8042','http://10.1.1.26:8042','http://10.1.1.29:8042','http://10.1.1.31:8042','http://10.1.1.32:8042','http://10.1.1.38:8042','http://10.1.1.2:8042','http://10.1.1.42:8042','http://10.1.1.50:8042','http://10.1.1.51:8042','http://10.1.1.54:8042']
result={}
start=0
class SingleThread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
	    self.index=i

    def run(self):
	    w = Web3(HTTPProvider(address[self.index]))
	    transactionSearch = w.eth.contract(json.loads(abi), contractAddress, ContractFactoryClass=ConciseContract)
        print Web3.toInt(transactionSearch.getProductInfo(1,1,1)),time.time()-start

start=time.time()
for i in range(20):
    s = SingleThread(i)
    s.start()
