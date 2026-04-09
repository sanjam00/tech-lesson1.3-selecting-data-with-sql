
import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# returns all data and all columns
employee_data = pd.read_sql("""
                            SELECT * FROM employees;
                            """, conn)

# returns first and last name only. can change order to firstName, lastName if you want
employee_first_last = pd.read_sql("""
                            SELECT lastName, firstName FROM employees;
                            """, conn)

# the AS keyword will change the label of the column
employee_alias = pd.read_sql("""
                            SELECT firstName AS name FROM employees;
                            """, conn)

# conditional rendering. the ,head() method returns only the first 10 rows- default is 5 rows if no number is passed
employee_conditional = pd.read_sql("""
                            SELECT firstName, lastName, jobTitle,
                            CASE
                            WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
                            ELSE "Not Sales Rep"
                            END AS role
                            FROM employees;
                            """, conn).head(10)

employee_multi_case = pd.read_sql("""
                            SELECT firstName, lastName, officeCode,
                            CASE
                            WHEN officeCode = "1" THEN "San Francisco, CA"
                            WHEN officeCode = "2" THEN "Boston, MA"
                            WHEN officeCode = "3" THEN "New York, NY"
                            WHEN officeCode = "4" THEN "Paris, France"
                            WHEN officeCode = "5" THEN "Tokyo, Japan"
                            END AS office
                            FROM employees;
                            """, conn)


"""STRING MANIPULATION"""

# return the lengths of firstName using length() method
employee_name_lengths = pd.read_sql("""
SELECT length(firstName) AS name_length
  FROM employees;
""", conn).head()

# convert to all caps
upper_employees = pd.read_sql("""
SELECT upper(firstName) AS name_in_all_caps
  FROM employees;
""", conn).head()

# substring
# "1, 1" is the range of what we want to select. 
# in this case, we want a substring to return the first initial, that's just the first character and we stop at the first character
employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) AS first_initial
  FROM employees;
""", conn).head()

# concatenate ||
employees_concatenate = pd.read_sql("""
SELECT substr(firstName, 1, 1) || "." AS first_initial
  FROM employees;
""", conn).head()

# concatenate two collumns
employees_full_names = pd.read_sql("""
SELECT firstName || " " || lastName AS full_name
  FROM employees;
""", conn).head()


# print(employee_data)
# print(employee_first_last)
# print(employee_alias)
# print(employee_conditional)
# print(employee_multi_case)
# print(employee_name_lengths)
# print(upper_employees)
# print(employees_initials)
# print(employees_concatenate)
# print(employees_full_names)


"""BUILT IN SQL FUNCTIONS FOR MATH OPERAIONTS"""

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)

# round a number
rounded_prices = pd.read_sql("""
SELECT round(priceEach) AS rounded_price
  FROM orderDetails;
""", conn)

# CAST will allow convert the type of any value to any other type
cast_prices = pd.read_sql("""
SELECT CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails;
""", conn)

# print(order_details)
# print(rounded_prices)
# print(cast_prices)


"""BASIC MATH OPERATIONS"""

totals = pd.read_sql("""
SELECT priceEach * quantityOrdered AS total_price
  FROM orderDetails;
""", conn)

# print(totals)


"""DATE AND TIME OPERATIONS"""

orders = pd.read_sql("""SELECT * FROM orders;""", conn)

# the difference between requiredDate and orderDate, but this doesnt work. we need a *julianday*
# days_remaining = pd.read_sql("""
# SELECT requiredDate - orderDate
#   FROM orders;
# """, conn)

#julianday function
days_remaining = pd.read_sql("""
SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
  FROM orders;
""", conn)

# adding time onto a date
order_dates = pd.read_sql("""
SELECT orderDate, date(orderDate, "+7 days") AS one_week_later
  FROM orders;
""", conn)

string_order_dates = pd.read_sql("""
SELECT orderDate,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year,
       strftime("%d", orderDate) AS day
  FROM orders;
""", conn)

print(orders)
print(days_remaining)
print(order_dates)
print(string_order_dates)


conn.close()