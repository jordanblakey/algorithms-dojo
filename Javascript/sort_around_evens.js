function sortAroundEvens(array) {
  // Given an array of integers, return a list with asc sorted odds, leaving evens in place
  if (array == []) return array
  let copy = array.slice()

  array = array
    .map(x => parseInt(x))
    .filter(x => x % 2 != 0)
    .sort((x, y) => x - y)
  copy.forEach((x, i) => {
    if (x % 2 == 0) array.splice(i, 0, x)
  })
  
  return array
}
