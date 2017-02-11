// Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
//
// Example
//
// For inputArray = [3, 6, -2, -5, 7, 3], the output should be
// adjacentElementsProduct(inputArray) = 21.
//
// 7 and 3 produce the largest product.
//
// Input/Output
//
// [time limit] 4000ms (js)
// [input] array.integer inputArray
//
// An array of integers containing at least two elements.
//
// Constraints:
// 3 ≤ inputArray.length ≤ 10,
// -50 ≤ inputArray[i] ≤ 1000.
//
// [output] integer
//
// The largest product of adjacent elements.

function adjacentElementsProduct(inputArray) {
    var currentProduct, greatestProduct = Number.NEGATIVE_INFINITY;
    for (var i=0; i<=inputArray.length; i++){
        currentProduct = inputArray[i]*inputArray[i+1];
        if (currentProduct > greatestProduct) {
            greatestProduct = currentProduct;
            console.log('New greatest product! '+greatestProduct);
        }
    }
    return greatestProduct;
}

var inputArray = [3, 6, -2, -5, 7, 3];
adjacentElementsProduct(inputArray);
