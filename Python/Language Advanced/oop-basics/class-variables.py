class Employee:

  raise_amount = 1.04

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

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Jordan', 'Blakey', 123456)
emp_2 = Employee('John', 'Doe', 321654)

# print(emp_1.fullname())
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# Print the namespace for an instance (class and instance attributes)
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05  # Change everywhere
emp_2.raise_amount = 2.00  # change only for the instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
