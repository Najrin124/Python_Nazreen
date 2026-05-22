--- variables - use to store the data

-- data types
v_str = "najrin"
v_int = 5
v_float = 9.0
v_bool = True

-- print(v_str + " " + str(v_int) + " "+ str(v_bool))
-- print(f"{v_str} {v_int} and {v_bool}") # formated string


--  list variable - it is ordered set where you can store multiple  data types values

-- Tuple - A tuple in Python is an ordered, immutable collection of elements. It can store multiple items of different data types, and once created, its values cannot be changed.


Key points you can mention:
  Ordered → Elements have a fixed position
  Immutable → Cannot modify, add, or remove elements after creation
  Allows duplicates → (1, 1, 2) is valid
  Supports indexing → t[0] gives first element


--- # # dictionary - it stores dta in key value pairs

-- dic_1 = {"name": "najrin", "age": 26, "location": "kolkata"}
--  print(dic_1)
 print(dic_1["age"])
 print(dic_1.keys())
 print(dic_1.values())
 print(dic_1.items())

---- set - unique unordered list of items

 set_1 = {1,2,3,3,3,3,4,5,6}
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

# numpy is a external library in python which is used for numerical computations and data manipulation. It provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

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
print(f"Short delta: {short_delta}")  # Output: 1:30:00 ---


# lets cover oops concepts in python
# oops means object oriented programming system - meaning in layman is to represent real world entities using classes and objects

# concepts of oops
# 1. class - blueprint of object
# 2. object - instance of class
# 3. inheritance - acquiring properties of parent class to child class
# 4. polymorphism - ability to take many forms, meaning one class can have multiple methods with same name but different parameters
# 5. encapsulation - wrapping data and methods into single unit, meaning restricting access to some components
# 6. abstraction - hiding complex implementation details and showing only essential features
# 7. method - function defined inside class
# 8. constructor - special method to initialize object  
# 9. destructor - special method to destroy object and free memory
# 10. attributes - variables defined inside class
# 11. self - represents instance of class
# 12. static method - method that belongs to class rather than
# 13. class method - method that takes class as first argument
# 14. instance method - method that takes instance as first argument
# 15. operator overloading - ability to define custom behavior for operators
# 16. method overloading - ability to define multiple methods with same name but different parameters
# 17. method overriding - ability to redefine method in child class
# 18. multiple inheritance - acquiring properties from multiple parent classes
# 19. multilevel inheritance - acquiring properties from parent class to child class and then to grandchild class
# 20. hierarchical inheritance - multiple child classes inheriting from single parent class
# 21. composition - building complex objects using simpler objects
# 22. aggregation - special form of composition where child can exist independently of parent
# 23. namespace - container that holds a set of identifiers and their corresponding objects
# 24. module - file containing python code
# 25. package - collection of modules
# 26. exception handling - mechanism to handle runtime errors


# lets do practical implementation of oops concepts in python

# example of class and object

# class Person:
#     def __init__(self, name, age):
#         self.name = name # instance variable
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# person1 = Person("Alice", 30)
# print(person1.greet())
# person2 = Person("Bob", 25)
# print(person2.greet())

# inheritance example

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Animal sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# dog = Dog("Buddy")
# print(dog.name + " says " + dog.speak())
# cat = Cat("Whiskers")
# print(cat.name + " says " + cat.speak())

# polymorphism example - same method name but different behavior in different classes

# class Shape:
#     def area(self):
#         return 0
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# circle = Circle(5)
# print("Area of circle: " + str(circle.area()))
# rectangle = Rectangle(4, 6)
# print("Area of rectangle: " + str(rectangle.area()))    

# encapsulation example - restricting access to some components using private variables and methods

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance # private variable

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")

#     def get_balance(self):
#         return self.__balance   
    
# account = BankAccount("Alice", 1000)
# account.deposit(500)
# account.withdraw(200)
# print("Current balance: " + str(account.get_balance()))

#abstraction example - hiding complex implementation details and showing only essential features
# difference between abstracction and encapsulation in layman is that abstraction focuses on hiding complexity and showing only essential features, while encapsulation focuses on bundling data and methods together and restricting access to some components.

#abstrcation example

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine started."
# class Motorcycle(Vehicle):
#     def start_engine(self):
#         return "Motorcycle engine started."
# car = Car()
# print(car.start_engine())
# motorcycle = Motorcycle()
# print(motorcycle.start_engine())

# attributes and types of attributes - instance attributes, class attributes, static attributes
# lets do example of class attributes and instance attributes

# class Employee:
#     company_name = "Tech Solutions" # class attribute
#     def __init__(self, name, position):
#         self.name = name # instance attribute
#         self.position = position
# employee1 = Employee("Alice", "Software Engineer")
# employee2 = Employee("Bob", "Data Scientist")

# static attribute example

# class MathUtils:
#     pi = 3.14 # static attribute

#     @staticmethod
#     def area_of_circle(radius):
#         return MathUtils.pi * radius ** 2   
# print("Area of circle with radius 5: " + str(MathUtils.area_of_circle(5)))

# method types - instance method, class method, static method

# # instance method example

# class person:
#     def __init__(self, name):
#         self.name = name

#     def instance_method(self):
#         return f"Hello, my name is {self.name}."    
    
# person1 = person("Alice")
# print(person1.instance_method())

# class method example

class Employee:
    company_name = "Tech Solutions" # class attribute
    def __init__(self, name, position):
        self.name = name # instance attribute
        self.position = position
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

employee1 = Employee("Alice", "Software Engineer")
employee2 = Employee("Bob", "Data Scientist")
print("Company name before change: " + Employee.company_name)
Employee.change_company_name("Innovative Tech")
print("Company name after change: " + Employee.company_name)

--- 1. NumPy
NumPy is a Python library used for:


Numerical calculations


Arrays


Matrix operations


Scientific computing


Install:
pip install numpy
Example:
import numpy as nparr = np.array([1, 2, 3, 4])print(arr)print(arr + 10)
Output:
[1 2 3 4][11 12 13 14]
Important NumPy Functions
np.array()np.zeros()np.ones()np.arange()np.mean()np.sum()np.max()np.min()
Example:
import numpy as npnumbers = np.array([10, 20, 30])print("Sum:", np.sum(numbers))print("Average:", np.mean(numbers))

2. Pandas
pandas is used for:


Data analysis


Working with Excel/CSV files


Tables and datasets


Install:
pip install pandas
Example:
import pandas as pddata = {    "Name": ["John", "Alice"],    "Age": [22, 25]}df = pd.DataFrame(data)print(df)
Output:
    Name  Age0   John   221  Alice   25
Read CSV File
import pandas as pddf = pd.read_csv("students.csv")print(df)
Important Pandas Functions
head()tail()info()describe()read_csv()DataFrame()

3. math Module
The Python math module is used for mathematical operations.
No installation needed.
Example:
import mathprint(math.sqrt(25))print(math.factorial(5))print(math.pi)
Output:
5.01203.141592653589793
Common Functions
math.sqrt()math.ceil()math.floor()math.factorial()math.pimath.pow()
Example:
import mathprint(math.ceil(4.2))print(math.floor(4.9))
Output:
54

4. random Module
The Python random module is used to generate random values.
Example:
import randomprint(random.randint(1, 10))
Output:
7
Common Functions
random.randint()random.choice()random.random()random.shuffle()
Example:
import randomcolors = ["red", "blue", "green"]print(random.choice(colors))
Example:
import randomnumbers = [1, 2, 3, 4, 5]random.shuffle(numbers)print(numbers)

Quick Difference
ModuleUsed ForNumPyArrays & numerical computingPandasData analysis & tablesmathMathematical calculationsrandomRandom number generation

Interview Question Example
Q: Difference between NumPy array and Python list?
Answer:


NumPy arrays are faster


Use less memory


Support mathematical operations easily


Example:
import numpy as npa = np.array([1, 2, 3])print(a * 2)
Output:
[2 4 6]


  


