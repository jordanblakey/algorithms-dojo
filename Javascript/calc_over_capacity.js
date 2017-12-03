function enough(cap, on, wait) {
  // Given a buses capacity, people onboard, and people waiting, how many can't fit?
  let load = cap - on - wait 
  return load > 0 ? 0 : Math.abs(load)
}

// Disgustingly compact version
let e=(c,o,w)=>c-o-w>0?0:Math.abs(c-o-w)
