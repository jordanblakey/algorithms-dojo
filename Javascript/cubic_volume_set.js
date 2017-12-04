function findNb(m) {
  // Given a total volume for a stack of cubes, { n^3, (n-1)^3 ... },
  // return the number of cubes needed to match the volume.
  // If the # cannot be expressed as an iteger, return -1
  let cube = (x) => Math.pow(x, 3)  
  let sum = 0, i = 1, log = ''
  
  while (sum < m) {
    sum += cube(i)
    if (sum == m){ return i }
    i += 1
  }

  return (-1)
}

// Refactored (Babel for ** operator)
let findNb = (m) => {
  let n = 0
  while (m > 0) m -= ++n**3
  return m ? -1 : n
}
