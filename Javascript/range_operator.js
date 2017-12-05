function range(a,r,n) {
  // Given a starting int, step, and length, return a comma separated string of numbers that matches the parameters.
  arr = ''
  for (i = 0; i < n; i++) {
    i < n - 1 ? arr += a + ', ' :
    arr += a
    a+=r
  }
  return arr
} 
