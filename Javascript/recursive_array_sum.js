const sumNested = arr => {
  // Given any nested list, calculate the sum of it's numeric elements
  arr = arr
    .join()
    .split(',')
    .map(x => parseInt(x))
    .filter(x => !isNaN(x))

  if (arr.length==0) return 0
  arr = arr.reduce((acc,x) => acc + x)
  return arr
};
