def square_digits(num):
    result = ''
    for i in str(num):
        result += str(int(i)**2)
    return int(result)
    
# Using list comprehensions
def square_digits(num):
  return int(''.join(str(int(x)**2) for x in str(num)))
