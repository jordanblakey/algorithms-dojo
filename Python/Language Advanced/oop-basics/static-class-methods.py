class Employee:
  num_of_emps = 0
  raise_amt = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + 'last' + '@email.com'
    self.pay = pay

    Employee.num_of_emps += 1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)

  @classmethod  # Recieve the class as 'self' auto instead of the instance
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount  # Even if run from an instance, applies to all

  @classmethod  # Alternative constructor that accepts a string
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @staticmethod  # Static doesn't recieve the instance or class
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True


emp_1 = Employee("John", 'Doe', 50000)
emp_2 = Employee("Sam", 'Smith', 60000)

Employee.set_raise_amt(1.20)
emp_1.set_raise_amt(1.05)  # Even if run from an instance, applies to all

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'Jonah-Doe-70000'
emp_str_2 = 'Sally-Smith-80000'

emp_3 = Employee.from_string(emp_str_1)

print(vars(emp_3))

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
