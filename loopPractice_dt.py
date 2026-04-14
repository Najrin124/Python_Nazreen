
# age = int(input("Enter your age:"))

# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")    
    
# nums = [10, 23, 45, 60, 11, 8]

# even_count = 0
# odd_count = 0

# for num in nums:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)


# num = int(input("Enter a number:"))

# for i in range (1 , 11):
#    print(num, "x", i, "=", num * i)
# sum = 0
# i = 1
# while i <= 100:
#     sum = sum + i
#     i = i + 1

# print(sum)   
    
# numbers = [10, 20, 35, 55, 89, 0, 6]
# largest = numbers[0]

# for num in numbers:
#    if (num > largest):
#       largest = num 
#       print("largest number:", largest)

# numbers = [12, 45, 7, 89, 23]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest number:", largest)

# password = input("Enter a number")
# has_number = False

# for ch in password:        
#    if ch.isdigit():
#       has_number = True
#       break


#    if len (password) >= 8 and has_number:
#       print("Enter valid password")
#    else:   
#        print("Enter invalid password")

# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     result = num1 / num2
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter valid numbers.")
  


# data = [1, 2, 6, 50, 20 ,15]    

# try:
#     index = int(input("Enter an index: "))
#     print("Element:", data[index])

# except:
#     print("Error: Index out of range or invalid input.")
 
# finally:
#     print("This block will always execute.") 


# class NegativeNumberError(Exception):
#     pass

# try:
#     num = int(input("Enter a number: "))

#     if num < 0:
#         raise NegativeNumberError("Negative numbers are not allowed")

#     print("You entered:", num)

# except NegativeNumberError as e:
#     print(e)


# class InvalidAgeError(Exception):
#    pass
# try:
#    age = int(input("Enter your age:"))

#    if age < 0:
#       raise InvalidAgeError("Age cannot be negative.")
#    print("Your age is:", age)
# except InvalidAgeError as e:
#    print(e)   

# import numpy as np 

# arr = np.array([1, 2, 3, 4, 5])
# print("Array:", arr)
# print("sum", np.sum(arr))
# print("mean:", np.mean(arr))
# print("standard Derivation", np.std(arr))

# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D Array:", arr2)
# print("Square of the array:", np.square(arr2))

# arr3 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
# row_sum = np.sum(arr3, axis=1)
# print("Row-wise sum:", row_sum)

# column_sum = np.sum(arr3, axis=0)
# print("Column-wise sum:", column_sum )

# max_value = np.max(arr3)
# max_index = np.argmax(arr3)
# print("Maximum value in the array:", max_value)
# print("Index of the maximum value:", max_index)

# arr4 = np.array([[1, 2, 3], [4, 5, 6]])
# transpose_matrix = np.transpose(arr4)
# print("Original Matrix:\n", arr4)
# print("Transpose of the Matrix:\n", transpose_matrix)

# identity_matrix = np.eye(5)
# print("Identity Matrix:\n", identity_matrix)
# arr4 = np.random.rand(3, 3)
# print("Random Matrix:\n", arr4)
# print("mean", np.mean(arr4))
# print("max", np.max(arr4))
# print("min", np.min(arr4))

# middle_row = arr4[1]
# print("middle_row", middle_row)

# arr = np.array([2, 3, 4, 5, 6, 10, 8, 9])
# arr[arr > 5] = 0

# print(arr)

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# result = np.dot(A, B)
# print("Result n/", result)
# arr = np.random.rand(3, 3)
# print("matrix n/", arr)
# print("mean n/", np.mean(arr))
# print("max n/", np.max(arr))
# print("min n/", np.min(arr))     
# print("transpose", arr. T)
# print("sum", np.sum(arr))
# print("Determinant:", np.linalg.det(arr))

# import math 

# print("Square root of 16:", math.sqrt(16))
# print("Factorial of 5:", math.factorial(5))
# print("Power of 2 raised to 3:", math.pow(2,3))
# print("Sine of 30 degrees:", math.sin(math.radians(30)))
# print(math.gcd(12, 15))
# print(math.lcm(12, 15))
# print(math.sin(math.pi/2))
# print(math.cos(math.pi))
# print(math.pi/4)
# print(math.tan(math.pi/4))
# print(math.log(100, 10))
# print(math.exp(1))
# print(math.ceil(2.3))
# print(math.floor(2.7))
# print(math.pi)
# print(math.e)

#import random
# print(random.random())
# print(random.randint(1, 10))
# print(random.choice(['apple', 'banana', 'cherry']))
# print(random.sample([1, 2, 3, 4, 5], k=3))
# print(random.shuffle([1, 2, 3, 4, 5]))
# print(random.uniform(1, 10))
# print(random.gauss(0, 1))
# print(random.seed(42))
# print(random.random())
# print(random.randint(1, 10))


# import pandas as pd

# s = pd.Series([1, 2, 3, 4, 5])
# print(s)

# df = pd.read_csv(r"/home/mistu/Documents/python/data.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.tail())
# print(df.columns())
# print(df.shape)
# print(df.dtypes)
# print(df.isnull().sum())

# import random
# otp = random.randint(1000, 9999)
# print("generated otp:", otp)

# attempts = 3

# while attempts > 0:
#     user_otp = int(input("Enter the OTP:"))
#     if user_otp == otp:
#         print("OTP verified successfully!")
#         break
#     else:
#         attempts -= 1
#         print("Invalid OTP. Attempts left:", attempts)
#     if attempts == 0:
#         print("Account locked")
# def check_password(password):
    
#     has_number = False
#     has_uppercase = False
#     has_special = False

#     for char in password:
#         if char.isdigit():
#             has_number = True
#         elif char.isupper():
#             has_uppercase = True
#         elif not char.isalnum():
#             has_special = True

#     if len(password) >= 8 and has_number and has_uppercase and has_special:
#         print("Strong Password")
#     else:
#         print("Weak Password")


# user_password = input("Enter your password: ")
# check_password(user_password)

# import pandas as pd

# df = pd.read_csv(r"/home/mistu/Documents/python/data.csv")
# avg_salary = df.groupby('Department')['Salary'].mean()
# print("Avarage salary per department:\n", avg_salary)

# height_paid = df.loc[df['salary'].idxmax()]
# print("Highest paid employee:\n", height_paid)

# overall_avg  = df['salary'].mean()
# above_avg = df[df['salary'] > overall_avg]
# print("Employees with above average salary:\n", above_avg)


# player1 = random.randint(1, 6)
# player2 = random.randint(1, 6)
# print("Player 1 rolled:", player1)
# print("Player 2 rolled:", player2)
# if player1 > player2:
#     print("Player 1 wins!")
# elif player2 > player1:
#     print("Player 2 wins!")
# else:
#     print("It's a tie!") 
   
# logs = [
# "INFO User login",
# "ERROR Database failed",
# "INFO Page loaded",
# "ERROR Timeout"
# ]

# error_count = 0

# for log in logs:
#     if "ERROR" in log:
#         error_count += 1
#         print(log)

# print("Total ERROR messages:", error_count)

from io import StringIO
import random

# employees = [
#     {"name": "Alice", "department": "HR", "salary": 50000},
#     {"name": "Bob", "department": "IT", "salary": 60000},
#     {"name": "Charlie", "department": "Finance", "salary": 55000},
#     {"name": "David", "department": "IT", "salary": 65000},
#     {"name": "Eve", "department": "HR", "salary": 52000}
# ]       


# random.shuffle(employees)
# team1 = employees[:3]
# team2 = employees[3:]   

# print("Team 1:")
# print(team1)
# print("Team 2:")
# print(team2)


# transactions = [200, 450, 300, 150, 600, 250]
# for amount in transactions:
#     if amount > 400:
#         print("High value transaction:", amount)


import pandas as pd

# df = pd.read_csv(r"/home/mistu/Documents/python/employees.csv")
# avg_salary = df.groupby('department')['salary'].mean()
# print("Avarage salary per department:\n", avg_salary)

# height_paid = df.loc[df['salary'].idxmax()]
# print("Highest paid employee:\n", height_paid)

# overall_avg  = df['salary'].mean()
# above_avg = df[df['salary'] > overall_avg]
# print("Employees with above average salary:\n", above_avg)


# data = """name,age,salary
#       John,25,50000
#       Alice,30,60000
#       Bob,22,45000"""

# df = pd.read_csv(r"/home/mistu/Documents/python/employees.csv")
# age_filter = df['age'] > 25

# salary_filter = df['salary'] > 50000
# print("age < 25")
# print(age_filter)
# print("n/ salary > 50000")
# print(salary_filter)

# files = [210, 450, 300, 150, 600, 250]

# largest = max(files)
# smallest = min(files)
# average = sum(files) / len(files)
# print("Largest file size:", largest)
# print("Smallest file size:", smallest)
# print("Average file size:", average)

# users = ["A","B","A","C","B","D"]

# unique_users = set(users)

# from collections import Counter
# visits = Counter(users)

# print("Unique Users:", unique_users)
# print("Visits per user:", visits)

import random
import string

upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special = random.choice(string.punctuation)

remaining = ''.join(random.choice(
    string.ascii_letters + string.digits + string.punctuation
) for _ in range(6))

password_list = list(upper + lower + digit + special + remaining)
random.shuffle(password_list)
password = ''.join(password_list)
print("password:", password)


# products = {
# "laptop":5,
# "mouse":0,
# "keyboard":10
# }

# for product,qty in products.items():
#     if qty == 0:
#         print(f"{product} is out of stock")
# import pandas as pd
# df = pd.read_csv(r"/home/mistu/Documents/python/employees.csv")
# sorted_df = df.sort_values(
#     by = ["salary", "age"],
#     ascending = [False, True]
# )

# print(sorted_df)

# import pandas as pd
# from io import StringIO

# data = """id,name
# 1,John
# 2,Alice
# 3,John
# 4,Bob"""

# df = pd.read_csv(StringIO(data))
# duplicates = df[df.duplicated("name")]

# print(duplicates)

# import random
# candiates = list(range(1, 101))
# selected = random.sample(candiates, 5)
# print("Selected candidates:", selected)

# df["salary_k"] = df["salary"].apply(lambda x: f"{x/1000}k")
# print(df)

# times = [120, 300, 250, 500, 100]
# average = sum(times) / len(times)
# slow = [t for t in times if t > 300]
# print("Average response time:", average)
# print("Slow response times:", slow)

# import pandas as pd


# 1 Load CSV
# df = pd.read_csv(r"/home/mistu/Documents/python/employees.csv")

# # 2 Remove duplicates
# df = df.drop_duplicates()

# # 3 Handle missing values
# df = df.fillna(method="ffill")

# # 4 Calculate average salary
# avg_salary = df["salary"].mean()
# print("Average salary:", avg_salary)

# # 5 Save cleaned dataset
# df.to_csv("cleaned_data.csv", index=False)

# nums = [10, 25, 8, 40, 30]

# largest = second = float('-inf')

# for num in nums:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print("Second largest =", second)

