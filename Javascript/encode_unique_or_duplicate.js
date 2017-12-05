function duplicateEncode(word){
  // Given a string, encode unique characters as '(' and recurring characters as ')'  
  word = word.split('')
  count = [], ret = ''
  for (x in word) {
    if (word[x].match(/[a-zA-Z]/g)) {
      word[x] = word[x].toLowerCase()
    }
    console.log(c = word.filter(y => y == word[x]).length)
    c == 1 ? ret += '(' :
    c > 1 ? ret += ')' : null
  }
  return ret
}

// Cleaner, more declarative version using indexOf(), lastIndexOf() to test for character uniqueness.
function duplicateEncode(word){
  return word
    .toLowerCase()
    .split('')
    .map( function (a, i, w) {
      return w.indexOf(a) == w.lastIndexOf(a) ? '(' : ')'
    })
    .join('')
}
