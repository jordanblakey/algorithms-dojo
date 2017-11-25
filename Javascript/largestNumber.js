//  Given an integer n, return the largest number that contains exactly n digits.
//
//  Example
//
//  For n = 2, the output should be
//  largestNumber(n) = 99.
//
//  Input/Output
//
//  [time limit] 4000ms (js)
//  [input] integer n
//
//  Constraints:
//  1 ≤ n ≤ 7.
//
//  [output] integer
//
//  The largest integer of length n.


function largestNumber(n){
    var nabs = Math.abs(n);
    var place = 1;
    var total = 0;
    while (nabs !== 0){
        total += place;
        place *= 10;
        nabs --;
        console.log('running total: ' + total);
    }
    total = total * 9;
    console.log('total: '+total);
    return total;
}

largestNumber(4444);
