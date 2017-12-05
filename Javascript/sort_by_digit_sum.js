function sortByDigitSum(str) {
  // Given a string of integers, return a string of the same numbers ordered by the sum of their digits.
  let fin = ''
  if (str === [] || str === '') return ''

  str = str
    .split(' ')
    .map(x => x.split(''))
    .map(x => x.map(y => (y = parseInt(y, 10))))

  let orig = str.slice().map(x => x)

  str = str.map(x => x.reduce((y, z) => y + z))
    .slice()
    .sort((x, y) => x - y)

  str.forEach(x => {
    let cache = []

    orig.forEach(y => {
      let z = y.reduce((za, zb) => za + zb)

      if (z === x) {
        cache.splice(cache.length, 0, parseInt(y.join(''), 10))
        cache.sort()
      }
    })

    fin += cache[0] + ' '
    cache[0]
      ? (cache[0] = cache[0]
          .toString()
          .split('')
          .map(y => parseInt(y, 10)))
      : null

    let alrdyRmvIndx = false
    for (let i = 0; i < orig.length; i++) {
      if (cache[0] !== 'undefined') {
        if (orig[i].join('') === cache[0].join('') && alrdyRmvIndx !== true) {
          orig.splice(i, 1)
          alrdyRmvIndx = true
        }
      }
    }
  })
  return fin.trim()
}
