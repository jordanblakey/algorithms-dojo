// Given a sequence of integers, check whether it is possible to obtain a strictly increasing sequence by erasing no more than one element from it.
//
// Example
//
// For sequence = [1, 3, 2, 1], the output should be
// almostIncreasingSequence(sequence) = false;
// For sequence = [1, 3, 2], the output should be
// almostIncreasingSequence(sequence) = true.
// Input/Output
//
// [time limit] 4000ms (js)
// [input] array.integer sequence
//
// Constraints:
// 2 ≤ sequence.length ≤ 105,
// -105 ≤ sequence[i] ≤ 105.
//
// [output] boolean
//
// true if it is possible, false otherwise.

function almostIncreasingSequence(sequence) {
    var sl = sequence.length;
    for (var i=0; i < sl; i++){
        var tseq = sequence.slice();
        tseq.splice(i,1);
        for (var j=0; j<sl-1; j++){
            if (tseq[j] >= tseq[j+1]){
                break;
            }
            else if(sl-1 === 1 || j === sl-3){
                return true;
            }
        }
    }
    return false;
}

var sequence = [1, 3, 2, 1];
almostIncreasingSequence(sequence);
