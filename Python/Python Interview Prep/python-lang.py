
#######################################################
# LOOPS
#######################################################
for i in range(1, 11):
  print i

i = 1
while i <= 10:
  print i
  i += 1

a = 10
b = 20
if a < b:
  print "{} is less than {}".format(a, b)
elif a == 20:
  print "{} is equal to {}".format(a, b)
else:
  print "{} is greater than {}".format(a, b)

# for i in range(1, 11):
#   print i

# i = 1
# while i <= 10:
#   print i
#   i += 1

# a, b = 10, 20

# for i in range(0, 30):
#   if a < b:
#     print "{} is less than {}".format(a, b)
#   elif a == b:
#     print "{} is equal to {}".format(a, b)
#   else:
#     print "{} is greater than {}".format(a, b)
#   a += 1


#######################################################
# LISTS
#######################################################
my_list = [10, 20, 30, 40, 50]
for i in my_list:
  print i

# my_list = [1, 2, 3, 4, 5]

#######################################################
# TUPLES
#######################################################

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in my_tuple:
  print i

# my_tuple = (1, 2, 3, 4, 5)

#######################################################
# DICT
#######################################################
my_dictionary = {'name': 'Bronx', 'age': '2', 'occupation': 'Corey\'s Dog'}
for key, val in my_dictionary.iteritems():
  print "my {} is {}".format(key, val)

# my_dict = {'key1': 1, 'key2': 2, 'key3': 3}

#######################################################
# SET
#######################################################
my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
for i in my_set:
  print i

# my_set = {1, 1, 2, 2, 3, 3}

#######################################################
# CLASSES AND OOP BASICS
#######################################################

# This basically says "class Person extends class object"


class Person(object):
  # __init is the constructor method auto called on init
  def __init__(self, name):
    # self is equivalent to 'this' instance. So, self.name = name assigns a
    # property name equal to the first argument to the instance
    self.name = name

  # this is a class method where self refers to the instance
  def reveal_identity(self):
    # this is a string which calls the string method .format to
    # interpolate arguments in order against {} sets in the string body.
    print "My name is {}".format(self.name)


# Class Superhero extends class Person
class SuperHero(Person):
  # define the constructor method with the instance and 2 arguments
  def __init__(self, name, hero_name):
    # inherit the constructor method from the extended class and
    # map arg 'name' to the inherited constructor
    super(SuperHero, self).__init__(name)
    # map argument hero_name as a property of the instance.
    self.hero_name = hero_name

  def reveal_identity(self):
    super(SuperHero, self).reveal_identity()
    print "...And I am {}".format(self.hero_name)


# class Person(object):
#   def __init__(self, name):
#     self.name = name

#   def reveal_identity(self):
#     print "my name is {}".format(self.name)


# class SuperHero(Person):
#   def __init__(self, name, hero_name):
#     super(SuperHero, self).__init__(name)
#     self.hero_name = hero_name

#   def reveal_identity(self):
#     super(SuperHero, self).reveal_identity()
#     print "...And I am {}".format(self.hero_name)
