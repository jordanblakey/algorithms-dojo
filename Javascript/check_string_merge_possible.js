function isMerge(s, p1, p2) {
  // Given three strings, return true if the first can be created by interleaving the second and third,
  // without rearranging the characters within either.

  if ((!p1 || 0 === p1.length) && (!p2 || 0 === p2.length)) return true
  if (p1.length + p2.length > s.length || s.length === 0) return false
  
  p1 = p1.split('')
  p2 = p2.split('')
  let f = []

  s.split('').forEach((x, i) => {
    pr1 = -1, pr2 = -1, pix1 = p1.indexOf(x), pix2 = p2.indexOf(x)    
    pix1 >= 0 && pix1 > pr1 ? (pr1 = pix1, f.push(x)) : 
    pix2 >= 0 && pix2 > pr2 ? (pr2 = pix2, f.push(x)) :
    f.push(0)    
  })

  f.indexOf(0) >= 0 ? return false :
  return true
}
