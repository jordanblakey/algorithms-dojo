// Return total price where n < 5 = 100, n < 10 = 95, n >= 10 = 90
let sales = n => { return n < 5 ? n * 100 : n < 10 ? n * 95 : n * 90 }
