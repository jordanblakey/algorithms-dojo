// Given numbers 1..n where n >, return a and b, where the product of a and b is equal 
// to the sum of all numbers in the sequence, excluding a and b.

function sum(x) {
  let su = 0
  while (x > 0) {
    su += x--
  }
  return su
}

function less(x) {
  let seq = []
  while (x > 0) {
    seq.push(x)
    x--
  }
  return seq
}

function removeNb(n) {
  let arr = [],
    s = sum(n)
  arr = less(n)
  let res = []

  arr.reduce((acc, x) => {
    arr.reduce((acc2, y) => {
      x * y - x - y === s ? (res = [[x - 2, y - 2], [y - 2, x - 2]]) : null
    })
  })

  return res
}
