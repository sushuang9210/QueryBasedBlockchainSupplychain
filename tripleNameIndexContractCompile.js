/*
__author__ = 'Shuang Su'
__copyright__ = 'Copyright 2018, Shuang Su'
__version__ = '0.1'
__email__ = 'shuangs@andrew.cmu.edu'
*/
const solc = require('solc');
const fs=require('fs');
var input=fs.readFileSync("contract.sol", "utf8");
output=solc.compile(input,1);
console.log(output);
