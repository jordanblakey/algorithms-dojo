function getAgeFromString(inputString){
  // Given a string containing a single number, return that number as an int
  return inputString
    .split(' ')
    .map(x => parseInt(x))
    .filter(Number)[0]
}
