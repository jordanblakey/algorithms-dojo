function maxRot(n) {
  // given an integer of x digits, rotate the digits to create a maximum number, 
  // while each rotation locks another digit on the left, until no more rotations are possible.
  
  n = n.toString().split(''), m=[], arr=[], i=0
  
  while (n.length > 0) {
    if (n[0] > n[1] && n[0] > n.slice(-1)[0])
      {console.log('You should not rotate.')}
    else if (n[1] > n.slice(-1)[0] || (n.length == 2 && n[0] < n[1]))
      {console.log('You should rotate left.'); rot(n, 'left')}
    else if (n[1] < n.slice(-1)[0])
      {console.log('You should rotate right.'); rot(n, 'right')}
    else {console.log('couldn\'t rotate.')}
    
    m.push(n.shift())
    arr.push(m.concat(n).join())
    arr[arr.length-1] = arr[arr.length-1].replace(/,/g,'')
    console.log(arr[arr.length-1])
    console.log(m.join(),'|', n.join(), '|', n.length)
  }
  arr = arr.sort()  
  console.log(arr)
  
  
  return parseInt(arr[0])
}
