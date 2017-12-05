function solve(a,b){
  // Given two strings, return a string of all the unique characters between them
  ret = [], a = a.toString().split(''), b = b.toString().split('')
  a.forEach(x => b.indexOf(x) == -1 ? ret.push(x): null)
  b.forEach(x => a.indexOf(x) == -1 ? ret.push(x): null)
  return ret.join('')
};
