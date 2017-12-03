function reverseLongWords(words){
  // Given a string of words, reverse every word that has more than 5 characters
  words = words.split(' ')
  words.forEach((x, i) => {
    if (x.length > 4) { 
      x = x
        .split('')
        .reverse()
        .join('')        
      words[i] = x
    }
  })
  return words.join(' ')
}

// More succinctly, using map
function rlg(ws){
  return ws.split(' ').map((w) => {
    return (w.length > 4) ? w.split('').reverse().join('') : w;
  }).join(' ');
}
