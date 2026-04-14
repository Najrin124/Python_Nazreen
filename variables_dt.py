#variables - use to store the data

# # data types
# v_str = "najrin"
# v_int = 5
# v_float = 9.0
# v_bool = True
# print(v_str + " " + str(v_int) + " "+ str(v_bool))
# print(f"{v_str} {v_int} and {v_bool}") # formated string

# My fathers age is 50 and My mothers age is 40 and my age is 10

# v_fathers_age = 50
# v_mothers_age = 40
# v_my_age = v_fathers_age - v_mothers_age
# print(f"My fathers age is {v_fathers_age} and My mothers age is {v_mothers_age} and my age is  {v_my_age}")

# list variable - it is ordered set where you can store multiple  data types values

# lst_1 = [1,2,3,4,5]

# print(lst_1)

# print(lst_1[1:3])

# lst_1[0] = 10
# lst_1[1] = 20
# lst_1[2] = 30

# print(lst_1)

# tup_1 = (1,2,3,4,5)

# print(tup_1)

# print(tup_1[1:3])

# tup_1[1] = 20

# # dictionary - it stores dta in key value pairs

# dic_1 = {"name": "najrin", "age": 26, "location": "kolkata"}
# print(dic_1)
# print(dic_1["age"])
# print(dic_1.keys())
# print(dic_1.values())
# print(dic_1.items())

# set - unique unordered list of items

# set_1 = {1,2,3,3,3,3,4,5,6}
# set_2 = {5,7,8,9}
# print(set_1)

# print(set_1.union(set_2))
# print(set_1.intersection(set_2))
# print(set_1.symmetric_difference(set_2))

# lets discuss loops and conditional statemments

# conditionL statements - if, elif, else example

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# # loops - for loop example

# list_1 = [1, 2, 3, 4, 5]
# for num in list_1:
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")

# # while loop example

# lst_1 = [1, 2, 3, 4, 5]
# index = 0
# while index < len(lst_1):
#     print(lst_1[index])
#     index += 1

# lets do exception handling - try, except, finally

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Invalid input. Please enter numbers.")
# except IndentationError:
#     print("Error: Indentation error in the code.")
# except IndexError:
#     print("Error: Index error in the code.")
# finally:
#     print("This block will always execute.")

# lets do one example with custom exceptions - exception handling with custom exceptions

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     elif age < 18:
#         print("You are a minor.")
#     elif age >= 18 and age < 65:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")
# except ValueError as ve:
#     print("Error:", ve)
# finally:
#     print("This block will always execute.")

# lets do numpy completely - execute all commands here

#numpy is a external library in python which is used for numerical computations and data manipulation. It provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

# import numpy as np

# # # create arrays

# # arr_1 = np.array([1, 2, 3, 4, 5]) # 1 dimensional array
# # print(arr_1)

# # arr_2 = np.array([[1, 2, 3], [4, 5, 6]]) # 2 dimensional array
# # print(arr_2)

# # arr_3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # 3 dimensional array
# # print(arr_3)

# # # array operations

# # arr_4 = np.array([1, 2, 3, 4, 5]) # 1 dimensional array
# # print(arr_4 + 10) # add 10 to each element
# # print(arr_4 * 2) # multiply each element by 2
# # print(arr_4 ** 2) # square each element
# # print(np.sqrt(arr_4)) # square root of each element
# # print(np.sum(arr_4)) # sum of all elements
# # print(np.mean(arr_4)) # mean of all elements
# # print(np.median(arr_4)) # median of all elements
# # print(np.std(arr_4)) # standard deviation of all elements   
# # print(np.var(arr_4)) # variance of all elements
# # print(np.min(arr_4)) # minimum element
# # print(np.max(arr_4)) # maximum element
# # print(np.argmin(arr_4)) # index of minimum element
# # print(np.argmax(arr_4)) # index of maximum element

# # # array slicing and indexing

# arr_5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 2 dimensional array
# # print(arr_5[0]) # first row
# # print(arr_5[1]) # second row
# # print(arr_5[2]) # third row
# # print(arr_5[:, 0]) # first column
# # print(arr_5[:, 1]) # second column
# # print(arr_5[:, 2]) # third column
# # print(arr_5[0, 0]) # element at first row and first column
# # print(arr_5[1, 1]) # element at second row and second column
# # print(arr_5[2, 2]) # element at third row and third column

# # lets do more examples/functions with numpy

# print(np.transpose(arr_5)) # transpose of the array
# print(np.dot(arr_5, arr_5)) # dot product of the array with itself
# # print(np.linalg.inv(arr_5)) # inverse of the array
# # print(np.linalg.det(arr_5)) # determinant of the array
# # print(np.linalg.eig(arr_5)) # eigenvalues and eigenvectors of the array
# print(np.zeros((2, 3))) # create a 2x3 array of zeros
# print(np.ones((2,3)))
# print(np.eye(3)) # create a 3x3 identity matrix
# print(np.random.rand(2, 3)) # create a 2x3 array of random numbers between 0 and 1
# print(np.random.randint(1, 10, size = (2, 3))) # create a 2x3 array of random integers between 1 and 10

# lets discuss about math module in python

import math

# lets do all math commands here

# print(math.sqrt(16)) # square root
# print(math.pow(2, 3)) # power
# print(math.factorial(5)) # factorial
# print(math.gcd(12, 15)) # greatest common divisor
# print(math.lcm(12, 15)) # least common multiple
# print(math.sin(math.pi/2)) # sine of 90 degrees
# print(math.cos(math.pi)) # cosine of 180 degrees
# print(math.tan(math.pi/4)) # tangent of 45 degrees
# print(math.log(100, 10)) # logarithm base 10 of 100
# print(math.exp(1)) # exponential of 1
# print(math.ceil(2.3)) # ceiling of 2.3
# print(math.floor(2.7)) # floor of 2.7
# print(math.pi) # value of pi
# print(math.e) # value of e

# lets do random module

# import random

# # lets do all random commands here

# print(random.random()) # random float between 0 and 1
# print(random.randint(1, 10)) # random integer between 1 and 10
# print(random.choice(['apple', 'banana', 'cherry'])) # random choice from a list
# print(random.sample([1, 2, 3, 4, 5], k=3)) # random sample of 3 elements from a list
# print(random.shuffle([1, 2, 3, 4, 5])) # shuffle a list in place

# print(random.uniform(1, 10)) # random float between 1 and 10    
# print(random.gauss(0, 1)) # random float from a normal distribution with mean 0 and standard deviation 1    
# print(random.seed(42)) # set the seed for reproducibility
# print(random.random()) # random float between 0 and 1 after setting the seed
# print(random.randint(1, 10)) # random integer between 1 and 10 after setting the seed

# print(random.choice(['apple', 'banana', 'cherry'])) # random choice from a list after setting the seed  

# lets discuss about pandas library and all commands here

import pandas as pd

# lets do all pandas commands here

# pandas store data in the form of series - 1 dimensional data and dataframe - multi dimensional data in the form of rows and columns

# series example

# s = pd.Series([1, 2, 3, 4, 5])
# print(s)



# df = pd.read_csv(r"/home/mistu/Documents/python/data.csv") # read a csv file into a DataFrame
# print(df.head()) # print the first 5 rows of the DataFrame
# print(df.info()) # print the summary of the DataFrame
# print(df.describe()) # print the statistical summary of the DataFrame
# print(df.tail()) # print the last 5 rows of the DataFrame
# print(df.columns) # print the column names of the DataFrame
# print(df.shape) # print the shape of the DataFrame
# print(df.dtypes) # print the data types of the columns in the DataFrame
# print(df.isnull().sum()) # print the number of missing values in each column of the DataFrame


# lets do file handling commands

# with  open("test.txt", "r") as file:
#     content = file.read()
#     print(content)
    
# with  open("test.txt", "w") as file:
#     file.write("Hello, this is a test file.\n")
#     file.write("This file is used for demonstrating file handling in Python.\n")

# with  open("test.txt", "a") as file:
#     file.write("\n Hello this is appended line\n")
#     file.write("This file is used for demonstrating file handling in Python.\n")

# lets do pydantic library and all commands here
# pydantic is a data validation and settings management library for Python. It allows you to define data models with type annotations and provides automatic validation and parsing of data.

# lets discuss datetime module in python
# datetime module provides classes for manipulating dates and times.

import datetime

# lets do all datetime commands here

date = datetime.date(2024, 6, 1) # create a date object
print(date)

now = datetime.datetime.now() # get the current date and time
print(now)

today = datetime.date.today() # get the current date
print(today)

today_time = datetime.datetime.today() # get the current date and time
print(today_time)

# strp abd strftime - string parse time and string format time  

date_str = "2024-06-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d") # convert string to datetime object
print(date_obj) 

date_obj = datetime.datetime(2024, 6, 1)
date_str = date_obj.strftime("%Y-%m-%d") # convert datetime object to string
print(date_str)

from datetime import datetime, timedelta

# Example 1: Create a timedelta representing 5 days
delta = timedelta(days=5)
print(delta)  # Output: 5 days, 0:00:00

# Example 2: Add timedelta to a datetime
now = datetime.now()
future = now + timedelta(days=7, hours=2)
print(f"Current time: {now}")
print(f"Future time: {future}")

# Example 3: Subtract timedelta from a datetime
past = now - timedelta(weeks=1)
print(f"Past time: {past}")

# Example 4: Calculate difference between two dates
date1 = datetime(2023, 10, 1)
date2 = datetime(2023, 10, 10)
difference = date2 - date1
print(f"Difference: {difference}")  # Output: 9 days, 0:00:00
print(f"Total days: {difference.days}")

# Example 5: Timedelta with negative values
negative_delta = timedelta(days=-3)
adjusted = now + negative_delta
print(f"Adjusted time: {adjusted}")

# Example 6: Timedelta with seconds, minutes, etc.
short_delta = timedelta(seconds=3600, minutes=30)
print(f"Short delta: {short_delta}")  # Output: 1:30:00