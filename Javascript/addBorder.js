// Given a rectangular matrix of characters, add a border of asterisks(*) to it.
//
// Example
//
// For
//
// picture = ["abc",
//            "ded"]
// the output should be
//
// addBorder(picture) = ["*****",
//                       "*abc*",
//                       "*ded*",
//                       "*****"]
// Input/Output
//
// [time limit] 4000ms (js)
// [input] array.string picture
//
// A non-empty array of non-empty equal-length strings.
//
// Constraints:
// 1 ≤ picture.length ≤ 5,
// 1 ≤ picture[i].length ≤ 5.
//
// [output] array.string
//
// The same matrix of characters, framed with a border of asterisks of width 1.

function addBorder(picture) {
    var rows = picture.length, cols = picture[0].length;
    var border = '*';
    var l = picture.length;
    //Getting information
    console.log('Input Array: '+picture);
    console.log('Rows:'+rows+' Cols:'+cols);

    //Append to beginning and end of each row
    for (var i=0; i<l; i++) {
        picture[i] = '*' + picture[i] + '*';

    }

    //Get new row lengths, set border to this length
    border = border.repeat(picture[0].length);

    //Add row above and row below
    picture.unshift(border);
    picture.push(border);

    for (var j=0; j<picture[0].length-1; j++) {
        console.log(picture[j]);
    }

    return picture;
}

var picture = ["abc",
               "ded"];

addBorder(picture);
