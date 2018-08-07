def fib(num):
  a, b = 0, 1
  for i in xrange(0, num):
    yield "{} : {}".format(i + 1, a)
    a, b = b, a + b


for item in fib(10):
  print item


# def fib(num):
#   a, b = 0, 1
#   for i in xrange(0, 10)
#     yield "{} : {}".format(i + 1, a)
#     a, b = b, a + b

# for item in fib(10)
#   print item
