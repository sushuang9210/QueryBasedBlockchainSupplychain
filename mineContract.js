/*
__author__ = 'Shuang Su'
__copyright__ = 'Copyright 2018, Shuang Su'
__version__ = '0.1'
__email__ = 'shuangs@andrew.cmu.edu'
*/
require('./tripleNameIndexContractCompile.js');
const net=require("net");
fs = require('fs');
var Web3=require('web3');
var web3=new Web3(new Web3.providers.HttpProvider('http://10.1.1.8:8042'));
web3.eth.defaultAccount = web3.eth.accounts[0];
var transactionsearchContract = web3.eth.contract(JSON.parse(output.contracts[':TransactionSearch'].interface));
var transactionsearch = transactionsearchContract.new(
{
from: web3.eth.accounts[0],
data: '0x'+output.contracts[':TransactionSearch'].bytecode,
gas: '4700000'
}, function (e, contract){
console.log(e, contract);
if (typeof contract.address !== 'undefined') {
console.log('Contract mined! address: ' +"'"+contract.address + "'"+' transactionHash: ' + contract.transactionHash);}
fs.writeFile('contractAddress.py',"contractAddress="+"'"+contract.address+"'\nabi="+"'"+output.contracts[':TransactionSearch'].interface+"'",function (err) {
    if (err)
        return console.log(err);
    console.log('Contract address written!');
});
fs.writeFile('contractAddress.js',"contractAddress="+"'"+contract.address+"'\nabi="+"'"+output.contracts[':TransactionSearch'].interface+"'",function (err) {
    if (err)
        return console.log(err);
    console.log('Contract address written!');
});
});
