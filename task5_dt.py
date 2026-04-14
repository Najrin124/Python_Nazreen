# Swap two variables without using a third variable
# a = 10
# b = 20
# a, b = b, a
# print(a, b)

# Assign multiple variables in one line and print their sum
# x, y, z  = 5, 10, 15
# total = x + y + z
# print(total)

# Create variables dynamically from a list of keys
# key = ["name", "age"]
# value = ["John", 25]

# for k, v in zip(key, value):
#     globals()[k] = v
# print(name, age)    

# Check the type of a variable at runtime
# x = 10.5
# print(type(x))

# if isinstance(x, float):
#     print("variable is float")

# Convert string "123" into integer and float

# s = "123"
# num_int = int(s)
# num_float = float(s)
# print(num_int)
# print(num_float)

# Data Types
# Convert float into integer without using int()
# num = 10.75
# integer_value = num // 1
# print(integer_value)

# Check if variable is numeric (int/float)
# value = 25.5
# if isinstance (value, (int, float)):
#     print("Numeric")
# else:
#     print("Not Numeric")    

# Convert list of strings into integers
# str_list = ["1", "2", "3"]
# int_list = [int(x) for x in str_list]
# print(int_list)

# Find memory size of different data types
# import sys

# a = 10
# b = 10.5
# c = "Hello"
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))

# Convert boolean into string "True"/"False"
# flag = True
# result = str(flag)
# print(result)

# Format string using f-string
# name = "Jhon"
# age = 25
# result = (f"Name: {name}, Age: {age}")
# print(result)

# Print float value up to 2 decimal places
# num = 12.34567
# print(f"{num : .2f}")

# Format number with commas
# num = 1000000
# print(f"{num: ,}")

# Align text left, right, center
# text = "python"
# print(f"{text:<10}") #left
# print(f"{text:>10}") #right
# print(f"{text:^10}") #center

# # Format date into DD-MM-YYYY
# from datetime import datetime
# today = datetime.now()
# formatted = today.strftime("%d-%m-%y")
# print(formatted)

# Remove duplicates from list
# nums = [1, 2, 2, 3, 4, 4]
# # unique = list(set(nums)) 
# unique = list(dict.fromkeys(nums))
# print(unique)

# Find second largest number
# nums = [10, 44, 67, 34, 25, 40]
# nums = list(set(nums))
# nums.sort
# print(nums[-2])
# nums = [10, 20, 5, 40, 25]
# nums = list(set(nums))
# nums.sort()
# print(nums[-2])

# Reverse list without reverse()
# nums = [1, 2, 3, 4]
# reverse_list = nums [:: -1]
# print(reverse_list)

# Flatten nested list
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)

# from collections import Counter
# nums = [1, 2, 2, 3, 3, 3]
# freq = Counter(nums)
# print(freq)

# Find common elements
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# common = list(set(a) & set(b))
# print(common)

# Sort list of tuples by second value
# data = [(1, 3), (2, 1), (4, 2)]
# sorted_data = sorted(data, key = lambda x: x[1])
# print(sorted_data)

# Rotate list by k positions
# nums = [1, 2, 3, 4, 5]
# k = 2
# rotate = nums[-k:] + nums[:-k]
# print(rotate)

# Find missing number (1–100)
# nums = list(range(1, 101))
# nums.remove(57)
# total_sum = 100 * 101 // 2
# missing = total_sum - sum(nums)
# print(missing)

# Merge two sorted lists
# a = [1, 3, 5]
# b = [2, 4, 6]

# merged = []
# i = j = 0

# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         merged.append(a[i])
#         i += 1
#     else:
#         merged.append(b[j])
#         j += 1

# merged += a[i:]
# merged += b[j:]

# print(merged)

# Convert tuple to list and modify it
# t = (1, 2, 3)
# lst = list(t)
# lst.append(4)
# t = tuple(lst)
# print(t)

# Count occurrences in tuple
# t = 1, 2, 2, 3, 2
# count = t.count(2)
# print(count)

# Find index of element
# t = (10, 20, 30, 40)
# index = t.index(30)
# print(index)

# Unpack tuple into variables
# t = (100, 200, 300)

# a, b, c = t

# print(a, b, c)

# Check if tuple is palindrome
# t = (1, 2, 3, 2, 1)
# if t == t[:: -1]:
#     print("palindrome")
# else:
#     print("not palindrome")    


# Remove duplicates using set
# nums = [1, 2, 2, 3, 4, 4]
# unique = set(nums)
# print(unique)

# Union & Intersection
# a = {1, 2, 3}
# b = {4, 5, 6, 3}
# print(a | b)
# print(a & b)


# Difference between sets
# a = {1, 2, 3}
# b = {3, 2, 4}
# print(a - b)

# Check subset
# a = {1, 2}
# b = {1, 2, 3, 4, 5}
# print(a.issubset(b))

# Remove all elements without clear()
# s = {1, 2, 3}
# s = set()
# print(s)

# Merge two dictionaries
# d1 = {"a":1}
# d2 = {"b":2}
# merge = {**d1, **d2}
# print(merge)

# Sort dictionary by values
# d = {"a":3, "b":2, "c":1}
# sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
# print(sorted_d)

# Count character frequency
# text = "hello"
# freq = {}
# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1
#     print(freq)

# Invert dictionary
# d = {"a":1, "b":2}
# invert = {v: k for k, v in d.items() }
# print(invert)

# Find key with maximum value
# d = {"a":10, "b":25, "c":15}
# max_key = max(d, key=d.get)
# print(max_key)

# Group words by first letter
# words = ["apple", "ant", "bat", "ball"]
# group = {}
# for word in words:
#     key = word[0]
#     group.setdefault(key, []).append(word)
#     print(group)


# Create dictionary from two lists
# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# d = dict(zip(keys, values))
# print(d)

# Remove key safely
# d = {"a":1, "b":2}
# d.pop("c", None)
# print(d)

# Access nested dictionary
# data = {"user": {"name":"Jhon", "age":26}}
# print(data["user"]["age"])
# print(data["user"]["name"])

#Convert dictionary to list of tuples
# d = {"a":1, "b":2}
# result = list(d.items())
# print(result)

# Conditional Statements/Even or Odd
# num = 10
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")    

# Check leap year
# year = 2024
# if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
#     print("leap year")
# else:
#     print("Not leap year")    

# Largest of 3 numbers
# a, b, c = 10, 24, 32
# largest = max(a, b, c)
# print(largest)

# Grade system
# marks = 85
# if marks >= 90:
#     print("A")
# elif marks >=75:
#     print("b")
# else:
#     print("Fail")    

# Check string palindrome
# text = "madam"
# if text == text[:: 1]:
#     print("palindrome")
# else:
#     print("Not palindrome")

# Function to calculate factorial
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(5))

# Function to check prime number
# def is_prime(n):
#     if n<= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#        if n % i == 0:
#            return False
#        return True
# print(is_prime(7))


# Function returning multiple values
# def calculate(a,b):
#     return a + b, a - b
# sum_val, diff_val = calculate(10, 5)
# print(sum_val, diff_val)


# Recursive Fibonacci
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6)) 

# Function with default arguments
# def greet(name = "Guest"):
#     print("Hello", name)
# greet()   
# greet("Jhon")

# Function with *args
# def add(*args):
#     return sum (args)
# print(add(1, 2, 3, 4))

# Function with **kwargs
# def display(**kwargs):
#     for key, value in kwargs.items():
#      print(key, value)
# display(name = "Jhon", age = 25)

# Function to calculate sum of list
# def list_sum(lst):
#     total = 0
#     for sum in lst:
#         total += sum 
#         return total
# print(list_sum([1, 2, 3, 4]))

# Decorator to log function calls
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print("function cll")
#         return func(*args, **kwargs)
#     return wrapper
# @logger
# def greet():
#     print("Hello")
# greet()

# Lambda inside function
# def multipler(n):
#     return lambda x: x*n
# double = multipler(2)
# print(double(5))

#Multiplication table 
# num = 5
# for i in range(1, 11):
#  print(num, "x", i, "=", num*i)

# Sum using loop
# total = 0
# for i in range(1, 6):
#     total += i
# print(total)    


# Factorial using loop
# n = 5
# fact = 1
# for i in range (1, n + 1):
#     fact *= i
#     print(fact)

# Pyramid pattern
# n = 4
# for i in range(1, n + 1):
#     print(""*(n-i) + "*"*(2*i-1))

# Iterate dictionary
# d = {"a":1, "b":2}
# for key, value in d.items():
#     print(key, value)

# Break example
# for i in range (10):
#  if i == 5:
#   break
#  print(i)

# Continue example
# for i in range (1, 6):
#     if i % 2 == 0:
#         continue
#     print(i)

# Matrix multiplication (simplified)
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# result = [[0, 0], [0, 0]]
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#          result[i][j] += A[i][k] * B[k][j]
# print(result)

# Common elements using loop
# a = [1, 2, 3]
# b = [2, 3, 4]
# common = []
# for i in a:
#     if i in b:
#         common.append(i)
#         print(common)

# Reverse string using loop
# text = "python"
# rev = ""
# for ch in text:
#     rev = ch + rev
#     print(rev)

# Square using lambda
# square = lambda x: x**2
# print(square(5))

# Lambda even/odd
# check = lambda x: "Even" if x%2==0 else "Odd"
# print(check(4))

# Sort using lambda
# data = [(1, 2), (2, 1), (4, 2)]
# print(sorted(data, key = lambda x: x[1]) )

# Lambda multiple arguments
# add = lambda a,b : a + b
# print(add(10, 20))

# Replace normal function with lambda
# def multifly(a,b):
#     return a*b

# multifly = lambda a,b : a * b
# print(multifly(3,4))


# Use map() to square list elements
# nums = [1, 2, 3, 4]
# square = list(map(lambda x: x**2, nums))
# print(square)

# Convert list of strings to uppercase
# words = ["python", "Java", "C"]
# user_words = list(map(str.upper,words))
# print(user_words)

# Add two lists using map
# a = [1, 2, 3]
# b = [4, 5, 6]
# result = list(map(lambda x, y: x + y, a, b))
# print(result)

# Apply function to dictionary values
# d = {"a": 1, "b": 2, "c": 3}

# updated = dict(map(lambda item: (item[0], item[1]*2), d.items()))

# print(updated)

# Combine map + lambda
# nums = [1, 2, 3, 4]
# result = list(map(lambda x: x + 10, nums))
# print(result)

# Create list of squares
# squares = [x**2 for x in range(1, 6)]
# print(squares)

# Filter even numbers
# nums = [1, 2, 3, 4, 5, 6]
# evens = [x for x in nums if x % 2 == 0 ]
# print(evens)

# Flatten nested list
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)

# Replace negative numbers with 0
# nums = [-2, 3, -1, 5]
# update = [x if x > 0 else 0 for x in nums ]
# print(update)

# Generate list of tuples (x, x²)
# pairs = [(x, x**2) for x in range(1, 6)]
# print(pairs)
# import json
# data = {"name":"Najrin", "age":26}

# json_data = json.dumps(data)
# print(json_data)

# Read JSON file
# import json

# with open("data.json", "r") as file:
#     data = json.load(file)

# print(data)

# Parse JSON string
# import json

# json_str = '{"name":"John","age":25}'

# data = json.loads(json_str)

# print(data["name"])

# Write JSON to file
# import json
# data = {"city":"Newyork"}
# with open("output.json", "w") as file:
#     json.dumps(data, file)

# Extract nested JSON value
# data = {
#     "user":{
#         "name":"Najrin",
#         "details":{"age":26}
#     }
# }
# print(data["user"]["details"]["age"])

# Read CSV
import pandas as pd
df = pd.read_csv("data.csv")

# # Display first 5 rows
# print(df.head())

filtered = df[df["age"] > 25]

print(filtered)