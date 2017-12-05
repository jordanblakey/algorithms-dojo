if (!String.prototype.padStart) {
  String.prototype.padStart = function padStart(targetLength,padString) {
      targetLength = targetLength>>0; //floor if number or convert non-number to 0;
      padString = String(padString || ' ');
      if (this.length > targetLength) {
          return String(this);
      }
      else {
          targetLength = targetLength-this.length;
          if (targetLength > padString.length) {
              padString += padString.repeat(targetLength/padString.length); //append to original to ensure we are longer than needed
          }
          return padString.slice(0,targetLength) + String(this);
      }
  };
}

function bigIntAdder(a, b) {
  console.log(typeof a, a, typeof b, b)
  console.time('Checking edge input')
    a === '' ? a = '0' : null
    b === '' ? b = '0' : null
  console.timeEnd('Checking edge input')
  console.time('Padding strings (while)')
  if (a.length < b.length) {a = a.padStart(b.length, '0')}
  if (b.length < a.length) {b = b.padStart(a.length, '0')}

  console.timeEnd('Padding strings (while)')

  console.time('Assignment (split, map, parseInt)')
  let arr1 = a.split('').map(x => parseInt(x, 10))
  let arr2 = b.split('').map(x => parseInt(x, 10))
  let arr3 = []
  let carry = 0
  console.timeEnd('Assignment (split, map, parseInt)')

  console.time('Reversing arrays')
  arr1 = arr1.reverse()
  arr2 = arr2.reverse()
  console.timeEnd('Reversing arrays')

  console.time('main loop')
  // console.log(arr1, arr2)
  for (let i = 0; i < arr1.length; i++) {
    // console.log(arr1[i], arr2[i]) // digits to add

    let sum = arr1[i] + arr2[i] + carry // sum of digits
    // console.log('sum', sum)
    arr3.unshift(sum % 10)

    if (sum > 9) { carry = 1}
    else { carry = 0 }

    // console.log('carry', carry) // number to carry
    // console.log(arr3)
  }
  console.timeEnd('main loop')

  if (carry > 0) {
    arr3.unshift(carry)
  }
  // console.log(arr3)

  for (let i = 0; i < arr3.length; i++ ) {
    //console.log(arr3[i])
    if (arr3[i] === 0) {arr3.splice(i, 1)}
    else {return arr3.join('')}
  }
}
