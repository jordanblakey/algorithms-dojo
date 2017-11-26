function sumStr(a,b) {
  // Given 2 numeric strings, return their sum as a string.
  let ai = parseInt(a), bi = parseInt(b);
  let nan = x => !isNaN(x) ? x : null;
  return (nan(ai) + nan(bi)).toString()
}

// More succinctly:
let sumStr = (a,b) => (+a + +b)+''
