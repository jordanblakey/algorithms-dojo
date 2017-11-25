from functools import reduce
# Given an integer, recursively sum its digits until a single digit remains. Return this digit.
def digital_root(n):
    while len(str(n)) > 1:
        n = reduce(lambda x, y: x+y, [int(m) for m in str(n)])
    return n
