# Classes & Instances


class Employee:
  # Init method runs automatically. Constructor.
  # specify an instance name, 'self' by convention, then args
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  # Define a method
  def fullname(self):
    return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jordan', 'Blakey', 123456)
emp_2 = Employee('John', 'Doe', 321654)

# print(emp_1)
# print(dir(emp_1))
# print(vars(emp_1))

# CAN SET PROPERTIES MANUALLY
# emp_1.first = 'Jordan'
# emp_1.last = 'Blakey'
# emp_1.email = 'test@test.test'
# emp_1.pay = 123456

# emp_2.first = 'John'
# emp_2.last = 'Doe'
# emp_2.email = 'test2@test.test'
# emp_2.pay = 654321

print(emp_1.email)
print(emp_2.email)

# Passes the instance automatically
print(emp_1.fullname())

# Calling from the class and passing the instance in
print(Employee.fullname(emp_1))
