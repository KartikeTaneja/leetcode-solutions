/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let totalGas=0;
    let currentGas=0;
    let start=0;

    for(let i=0;i<gas.length;i++) {
        currentGas+=gas[i]-cost[i];
        totalGas+=gas[i]-cost[i];
        if(currentGas<0) {
            currentGas=0;
            start=i+1;
        }
    }
    if(totalGas<0) return -1;
    return start;
};

// space 0(1)
// time 0(n)