function animals(heads, legs){
  // There are x legs and y heads, return an array of the actual # of chickens and cows.
  // Musing
  console.log('heads:', heads, 'legs:', legs)
  console.log('max chickens w/ legs avail:', legs / 2)
  console.log('if they were all chickens:', heads * 2, 'legs')
  console.log('max cows w/ legs avail:', legs / 4)
  console.log('if they were all cows:', heads * 4, 'legs')
  
  // Creating the formula
  let cows = (legs/2) - heads
  let chickens = heads - cows
  console.log('Actual cows:', cows)
  console.log('Actual chickens:', chickens)
  
  // Checking edge cases
  if (cows < 0 ||
  chickens < 0 ||
  !Number.isInteger(cows) ||
  !Number.isInteger(chickens) ||
  heads < 0 ||
  legs < 0 )
  
  // Return the result
  return 'No solutions'
  return [chickens, cows]
}


// REFACTORS TO ///////////////////////////////////////

function a(h, l){
  let c = (l/2) - h
  let ch = h - c  
  if (c < 0 ||
    ch < 0 ||
    !Number.isInteger(c) ||
    !Number.isInteger(ch) ||
    h < 0 ||
    l < 0 )  
  return 'Impossible!'
  return [ch, c]
}
