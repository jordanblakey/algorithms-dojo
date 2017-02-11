// Below we will define what and n-interesting polygon is and your task is to find its area for a given n.
//
// A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim side by side. You can see the 1-, 2- and 3-interesting polygons in the picture below.
//
//
//
// Example
//
// For n = 2, the output should be
// shapeArea(n) = 5;
// For n = 3, the output should be
// shapeArea(n) = 13.
// Input/Output
//
// [time limit] 4000ms (js)
// [input] integer n
//
// Constraints:
// 1 ≤ n < 104.
//
// [output] integer
//
// The area of the n-interesting polygon.

function shapeArea(n) {
    var ncount = 1;
    var i = 1;
    while (n>1){
        n--;
        ncount = ncount + 4*i;
        i++;
    }
    return ncount;
}

shapeArea(3);
