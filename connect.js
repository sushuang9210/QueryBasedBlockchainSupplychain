/*
__author__ = 'Shuang Su'
__copyright__ = 'Copyright 2018, Shuang Su'
__version__ = '0.1'
__email__ = 'shuangs@andrew.cmu.edu'
*/
var Web3=require('web3');
require('./contractAddress.js');
web31=new Web3(new Web3.providers.HttpProvider('http://10.1.1.8:8042'));
web32=new Web3(new Web3.providers.HttpProvider('http://10.1.1.9:8042'));
web33=new Web3(new Web3.providers.HttpProvider('http://10.1.1.10:8042'));
web34=new Web3(new Web3.providers.HttpProvider('http://10.1.1.12:8042'));
web35=new Web3(new Web3.providers.HttpProvider('http://10.1.1.13:8042'));
web36=new Web3(new Web3.providers.HttpProvider('http://10.1.1.14:8042'));
web37=new Web3(new Web3.providers.HttpProvider('http://10.1.1.17:8042'));
web38=new Web3(new Web3.providers.HttpProvider('http://10.1.1.18:8042'));
web39=new Web3(new Web3.providers.HttpProvider('http://10.1.1.21:8042'));
web310=new Web3(new Web3.providers.HttpProvider('http://10.1.1.22:8042'));
web311=new Web3(new Web3.providers.HttpProvider('http://10.1.1.26:8042'));
web312=new Web3(new Web3.providers.HttpProvider('http://10.1.1.29:8042'));
web313=new Web3(new Web3.providers.HttpProvider('http://10.1.1.31:8042'));
web314=new Web3(new Web3.providers.HttpProvider('http://10.1.1.32:8042'));
web315=new Web3(new Web3.providers.HttpProvider('http://10.1.1.38:8042'));
//web316=new Web3(new Web3.providers.HttpProvider('http://10.1.1.40:8042'));
web316=new Web3(new Web3.providers.HttpProvider('http://10.1.1.2:8042'));
web317=new Web3(new Web3.providers.HttpProvider('http://10.1.1.42:8042'));
web318=new Web3(new Web3.providers.HttpProvider('http://10.1.1.50:8042'));
web319=new Web3(new Web3.providers.HttpProvider('http://10.1.1.51:8042'));
web320=new Web3(new Web3.providers.HttpProvider('http://10.1.1.54:8042'));

web31.eth.defaultAccount=web31.eth.coinbase;
web32.eth.defaultAccount=web32.eth.coinbase;
web33.eth.defaultAccount=web33.eth.coinbase;
web34.eth.defaultAccount=web34.eth.coinbase;
web35.eth.defaultAccount=web35.eth.coinbase;
web36.eth.defaultAccount=web36.eth.coinbase;
web37.eth.defaultAccount=web37.eth.coinbase;
web38.eth.defaultAccount=web38.eth.coinbase;
web39.eth.defaultAccount=web39.eth.coinbase;
web310.eth.defaultAccount=web310.eth.coinbase;
web311.eth.defaultAccount=web311.eth.coinbase;
web312.eth.defaultAccount=web312.eth.coinbase;
web313.eth.defaultAccount=web313.eth.coinbase;
web314.eth.defaultAccount=web314.eth.coinbase;
web315.eth.defaultAccount=web315.eth.coinbase;
web316.eth.defaultAccount=web316.eth.coinbase;
web317.eth.defaultAccount=web317.eth.coinbase;
web318.eth.defaultAccount=web318.eth.coinbase;
web319.eth.defaultAccount=web319.eth.coinbase;
web320.eth.defaultAccount=web320.eth.coinbase;

transactionSearch1=web31.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch2=web32.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch3=web33.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch4=web34.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch5=web35.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch6=web36.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch7=web37.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch8=web38.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch9=web39.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch10=web310.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch11=web311.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch12=web312.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch13=web313.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch14=web314.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch15=web315.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch16=web316.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch17=web317.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch18=web318.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch19=web319.eth.contract(JSON.parse(abi)).at(contractAddress);
transactionSearch20=web320.eth.contract(JSON.parse(abi)).at(contractAddress);