function isValidIP(str) {
  // Given a string, check that it is a valid IP address
  if (str.indexOf(' ') !== -1){return false}
  str = str.split('.')
  if (str.length != 4) {return false}
  str = str.map(x => parseInt(x))
  if (str.reduce((acc, x) => acc + x) === 0) {return true}
  for (x in str) {
    if (isNaN(str[x])) { return false }
    else if (!(str[x] >= 0) || !(str[x] <= 255)) { return false }
    else if (str[x].length === 3 && str[x] < 100) { return false }
  }
  return true
}
