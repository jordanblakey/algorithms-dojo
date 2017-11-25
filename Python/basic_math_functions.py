# Create functions to represent all basic math operations on 2 arguments in sequence.
def add(a,b): return a + b
def multiply(a,b): return a * b
def divide(a,b): return a / b
def mod(a,b): return a % b
def exponent(a,b): return a ** b
def subt(a,b): return a - b

# As lamba functions.
add2 = lambda a, b: a + b
multiply2 = lambda a, b: a * b
divide2 = lambda a, b: a / b
mod2 = lambda a, b: a % b
exponent2 = lambda a, b: a ** b
subt2 = lambda a, b:a - b

# From built in operator module
from operator import add as add3, mul as multiply3, div as divide3, mod as mod3, pow as exponent3, sub as subt3
