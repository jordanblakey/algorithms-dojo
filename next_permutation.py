import itertools
def next_bigger(n):
  # given an int, return the next largest permutation of the same digits.
  d = set(map(int, map(''.join, itertools.islice(itertools.permutations(str(n)), 5000))))
  d = [x for x in d if x < n + 100000]
  d = sorted(d)
  for x in d[d.index(n):]:
    if x > n: return x
  return -1
