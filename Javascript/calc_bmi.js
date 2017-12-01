function bmi(weight, height) {
  let x = weight/Math.pow(height, 2)
  if (x <= 18.5)
    return 'Underweight'
  else if (x <= 25.0)
    return 'Normal'
  else if (x <= 30.0)
    return 'Overweight'
  else
    return 'Obese'
}

// More succinctly
let bmi = (w, h, bmi = w/h/h) => bmi <= 18.5 ? 'Underweight' : bmi <= 25 ? 'Normal' : bmi <= 30 ? 'Overweight' : 'Obese'
