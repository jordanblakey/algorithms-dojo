'''
#Build Tower by the following given argument:
#number of floors (integer and always greater than 0).

#Tower block is represented as *

for example, a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]

and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
'''

def tower_builder(n_floors):
  '''Takes a n_floors integer. Returns a list of n_floors Strings
  with length n_floors, that represents a tower'''

  tower = []
  padding = ' '
  base = n_floors + n_floors - 1
  floor = '*' * base
  
  while n_floors > 0:
    tower.insert(0, floor)
    floor = floor.replace(' ', '')
    floor = floor[:len(floor)-2]
    floor = padding + floor + padding
    padding += ' '
    n_floors -= 1
  
  return tower
