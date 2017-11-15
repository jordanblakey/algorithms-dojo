def solution(roman):
  # Given any roman numeral, return an integer of equivalent value
  dict = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'IX':9,
    'V':5,
    'IV':4,
    'III':3,
    'II':2,
    'I':1
  }
  roman = list(roman)
  for numeral in roman:
      if numeral in 'I':
        roman[roman.index(numeral):] = [''.join(roman[roman.index(numeral):])]
  
  return sum([dict[x] for x in roman])
