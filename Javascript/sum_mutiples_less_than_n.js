function solution(n){
  // Given n, return the sum of multiples of 3 , 5 < n
  x = 1, acc = []
  while (x < n) {
    acc.push(x * 3)
    acc.push(x * 5)
    x++
  }
  acc = acc
  .filter((x) => x < n)
  .sort((x,y) => x - y)
  acc = new Set(acc)
  acc = Array.from(acc)
  if (acc.length == 0) {return 0}
  return acc.reduce((a, x) => a + x)
}
