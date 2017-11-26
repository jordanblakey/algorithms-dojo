def find_difference(a, b):
    # Given two lists representing the dimensions of cuboids, return the difference in their volumes.
    def vol(l):
      v = 1
      for x in l: v *= x
      return v
    return abs(vol(a) - vol(b))


# Using operator.mul:
from operator import mul
def find_difference2(a, b):
    def vol(l): return reduce(mul, l)
    return abs(vol(a) - vol(b))


# Using reduce & a lambda function:
def find_difference3(a, b):      
    def p(l): return reduce(lambda x,y: x*y, l)
    return abs(p(a)-p(b))


# Using numpy.product:
from numpy import product as p
def vd(a,b): return abs(p(a)-p(b))


# Native Python one-liner:
def find_difference(a, b): return abs((a[0]*a[1]*a[2])-b[0]*b[1]*b[2])
