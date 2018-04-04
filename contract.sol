/*
__author__ = 'Shuang Su'
__copyright__ = 'Copyright 2018, Shuang Su'
__version__ = '0.1'
__email__ = 'shuangs@andrew.cmu.edu'
*/

pragma solidity ^0.4.2;
contract TransactionSearch
{
    mapping (uint => mapping (uint => mapping(uint => uint))) ChainData;
    struct latestInfo{uint state;uint time;}
    mapping (uint => mapping (uint => latestInfo)) latestState;
    mapping (uint => uint[]) stateTransition;
    mapping (uint => mapping (uint => uint)) destination;
    mapping (address => uint) owner;

    function TransactionSearch(){
        stateTransition[1]=[2,4,5];
        stateTransition[2]=[3];
        stateTransition[4]=[2,5];
	owner[0xfe94e15661e44d0fd6189adf2d3998d0c61ff201]=1;
	owner[0x2e42c0a3731788b51c195bd19b5eb0f0d7edbebd]=2;
	owner[0xf654a89e43c5b070ea8d3688e80396684f5d8856]=3;
	owner[0x5d0648c10835363e97955ded87dd76f53b78de1a]=4;
	owner[0xa7ca014dae980f9ac0ae8d56d4cb15691a1742ed]=5;
	owner[0x70693f87a678fcc6281f4a5918e7d21144d62d00]=6;
	owner[0x8fb2e18654fcd28ee04fa138a57b63584d3314e7]=7;
	owner[0x46b27e75b1a7a1863e2ed3b068f7edd7cf4fe3ae]=8;
	owner[0x055a55b9b74229e00e667c61ab9f9d9f31a38e12]=9;
	owner[0x08ef7aafd2947b65bc0514b1ed3278db0c28e67f]=10;
	owner[0x99f0d9c356f06f89b8ce421d987b76198827a5c8]=11;
	owner[0xfd9feafdeba6d95f243f2cf98dc22ba360787520]=12;
	owner[0xea90223b31b433b85eae2ac1e269aa7d4e7b0734]=13;
	owner[0xdef594b0a39dc8a586dd60c5ee490973fdb8a00d]=14;
	owner[0x992f3770274100994a82a8e94edbe2b67664b315]=15;
	owner[0xe490babe2dd10c6af9f90eaa9827e3ae37ba69a4]=16;
	owner[0x9002b6ae5a987c038a8903c41ef2cd6d713498df]=17;
	owner[0x24d29c6a68f593b7757f747966dc1a64ad143d53]=18;
	owner[0x4cce4d7ac65b04850277aedc6e0c2816fd454f58]=19;
	owner[0xde221147b4a1242b0b6b6d535b5e2b37e8683809]=20;
    }

    function setProductInfoAtom(uint _name,uint _id, uint _state, uint _time, uint _info)
    {
	      ChainData[_name][_id][_state]=_info*100000000+_time;
        latestState[_name][_id]=latestInfo({state:_state,time:_time});
    }

     function setProduceProductInfo(uint _name, uint _id, uint _state, uint _time, uint _weight, uint _pType1, uint _pId1, uint _pType2, uint _pId2)
    {
	if(owner[msg.sender]==_name){
         if(ChainData[_name][_id][_state]==0){
                if(_state==1)
               {
		    var _info=_weight*10000000000+_pType1*100000000+_pId1*100000+_pType2*1000+_pId2;
		    if(_pType1==6) setProductInfoAtom(_name, _id, _state, _time, _info);
                    else if(latestState[_pType1][_pId1].state==3){
                    if(_pType2==6) {setProductInfoAtom(_name, _id, _state, _time, _info);setProductInfoAtom(_pType1, _pId1, 5, _time, _info);}
		    else if(latestState[_pType2][_pId2].state==3){setProductInfoAtom(_name, _id, _state, _time, _info);setProductInfoAtom(_pType1, _pId1, 5, _time, _info);setProductInfoAtom(_pType2, _pId2, 5, _time, _info);}
                }
        }}
     }
}

    function setProductInfo(uint _name, uint _id, uint _state, uint _time, uint _check, uint _info)
    {
         if(ChainData[_name][_id][_state]==0){
           for(uint i=0;i<stateTransition[uint(latestState[_name][_id].state)].length;i++){
              if(stateTransition[uint(latestState[_name][_id].state)]==_state)
                {
                if(_time>latestState[_time][_id].time){
                        if(_state==3){
                                if(owner[msg.sender]==destination[_name][_id])
                                        {setProductInfoAtom(_name, _id, _state, _time, _info*100+_check);}}
                        else{
			if(owner[msg.sender]==_name){
			if(_state==2)
				{setProductInfoAtom(_name, _id, _state, _time, _info*100+_check);destination[_name][_id]=_check;}
                        else{ setProductInfoAtom(_name, _id, _state, _time, _info);}}}
                }
                }
              }
        }
}

function getProductInfo(uint _name, uint _id, uint _state) view public returns (uint)
    {   return ChainData[_name][_id][_state];
    }
}
