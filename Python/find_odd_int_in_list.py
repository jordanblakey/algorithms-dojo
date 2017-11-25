def find_it(seq):
  # Given an array, find the first int that appears an odd number of times.
  count = [seq.count(x) for x in seq]
  return seq[[x%2 for x in count].index(1)]
