// Given the string, check if it is a palindrome.
//
// Example
//
// For inputString = "aabaa", the output should be
// checkPalindrome(inputString) = true;
// For inputString = "abac", the output should be
// checkPalindrome(inputString) = false.
// Input/Output
//
// [time limit] 4000ms (js)
// [input] string inputString
//
// A non-empty string consisting of lowercase characters.
//
// Constraints:
// 1 ≤ inputString.length ≤ 10.
//
// [output] boolean
//
// true if inputString is a palindrome, false otherwise.

function checkPalindrome(inputString) {
  return inputString === inputString.split('').reverse().join('');
}

checkPalindrome('madam');
checkPalindrome('notapalindrome');
