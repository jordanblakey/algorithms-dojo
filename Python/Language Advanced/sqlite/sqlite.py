import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')  # Use in-memory database
# conn = sqlite3.connect('employee.db')  # Read or create

c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS employees (
  first text,
  last text,
  pay integer
)
''')

# BASIC QUERIES #######################################################
# Basics using sqlite3 core python module

# # Insert
# c.execute("INSERT INTO employees VALUES ('Mary', 'Smith', '99999')")
# c.execute("INSERT INTO employees VALUES ('Jordan', 'Blakey', '83000')")

# # Write to file
# conn.commit()

# # Select
# c.execute("SELECT * FROM employees WHERE last='Blakey'")
# # Return single row as python object
# print(c.fetchone())


# c.execute("SELECT * FROM employees WHERE pay>999")
# # Return all returned rows as python objects
# print(c.fetchall())

# # Close the DB connection
# # conn.close()

# Creating rows based on class instances ########################
# emp_1 = Employee('John', 'Doe', 80000)
# emp_2 = Employee('Jane', 'Doe', 90000)

# # TUPLE INTERPOLATION ###########################################
# print('{} {}: {}'.format(emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES (?, ?, ?)",
#           (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()
# c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))

# # DICT INTERPOLATION ###########################################
# print('{} {}: {}'.format(emp_2.first, emp_2.last, emp_2.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
#           'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()
# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})


# OOP INCORPORATION #############################################
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)


def insert_emp(emp):
  with conn:  # Using context manager, no need to commit
    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
        'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
  c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
  return c.fetchall()


def update_pay(emp, pay):
  with conn:
    c.execute("""
    UPDATE employees SET pay = :pay
    WHERE first = :first AND last = :last
    """, {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
  with conn:
    c.execute("DELETE from employees WHERE first = :first AND last = :last",
              {'first': emp.first, 'last': emp.last})


insert_emp(emp_1)  # Insert Row
insert_emp(emp_2)  # Insert row
emps = get_emps_by_name('Doe')  # matching rows -> list
print(emps)

update_pay(emp_2, 200000)  # update column pay where first and last match
remove_emp(emp_1)  # delet row where first and last match
emps = get_emps_by_name('Doe')  # matching rows -> list
print(emps)

conn.close()  # close the db connection
