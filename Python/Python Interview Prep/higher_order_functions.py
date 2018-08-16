##############################################################
# HIGHER ORDER FUNCTIONS
##############################################################

# Python map implementation ##################################

def my_map(func, arg_list):
  result = []
  for i in arg_list:
    result.append(func(i))
  return result

def square(x):
  return x * x

def cube(x):
  return x * x * x
 
squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])
print(squares, cube)


# In JS:
# let square = (x) => x * x
# let cube = (x) => x * x * x
# let my_map = (func, args) => {
#   result = []
#   args.forEach(x => result.push(func(x)))
# }
# let squares = my_map(square, [1, 2, 3, 4, 5])
# console.log(squares)

# Another example: ###########################################
def logger(msg):
  def log_message():
    print('Log:', msg)
  return log_message

log_hi = logger('Hi!')
log_hi()
