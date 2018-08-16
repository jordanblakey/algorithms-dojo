# First-Class Functions: functions treated as first-class citizens.
# Briefly, language allows functions to be treated the same as objects or any other variable.

def square(x):
  return x * x

f = square
i = square(5)

# ability to pass the function itself as a value
print(square)
print(f(5))

# ability to pass an invokation of the function (instance) as a value
print(i) 


# In JS:
# let square = (x) => x * x
# let f = square(5)
# console.log(square, f)
