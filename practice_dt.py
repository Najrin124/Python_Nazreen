# city = "Bangalore"
# temperature_c = 28.5
# bangalore_is_raining = False
# print(f"city :{city}   temperature_c :{temperature_c}   bangalore_is_raining :{bangalore_is_raining}")

# item_name = "Pen"
# price = 20     
# quantity = 3
# Total_cost = price * quantity

# print(f"Item Name: {item_name}  Price: {price}  Quantity: {quantity}  Total Cost: {Total_cost}")



# subjects = ["Math", "Science", "English", "History", "Computer"]
# print("Full List", subjects)
# print("Last Subject:", subjects[-1])
# print("First three subjects:", subjects[:3])
# print("Subjects from index 2 to 4:", subjects[2:4])
# print("Subjects from index -1 to +1:", subjects[-1 : 1])

# # Index:   0        1        2        3        4
# # Value:  Math   Science  English  History  Computer
# # Neg:    -5       -4       -3       -2       -1

# # Python slicing works left → right by default (step = 1).
# # Since -1 comes after 1 in the list, Python cannot move forward from index -1 to 1, so it returns an empty list [].

# print("Subjects from index -3 to 4:", subjects[-3 : 4])
# print("Subjects from index 0 to -3:", subjects[0: -3])
# print("Subjects from index -3 to 1:", subjects[1 : -1])

# marks = [10, 70, 75, 80]

# # Update first value
# marks[0] = 20

# # Update last value
# marks[-1] = 90

# # Print updated list
# print("Updated list:", marks)



# # Tuple of days
# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print("Days of the week:", days)
# # print the second day
# print("Second day:", days[1])
# # printthe middle three days
# print("the middle three days:", days[1:4])


# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell"
# }
# print("Product Name:", product["name"])
# print("Product Price:", product["price"])
# print("Product Brand:", product["brand"])   
# print("Product Keys:", product.keys())
# print("All product Details:",product)

# product =  {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell"
#         }
# product["stock"] = 10
# print("Updated Product Details:", product)

# numbers = [3, 5, 5, 10, 10, 20, 20, 30, 40, 40,50]
# unique_numbers = set(numbers)
# print("Unique numbers:", unique_numbers)

A = {1, 2,  3,  4,  5}
print("Print set A:",A)
B = {4, 5, 6, 7, 8}
print(A.union(B))
#print common elements in A and B
print(A.intersection(B))
# elements in A but not in B
print(A.symmetric_difference(B)) 
print(A.difference(B))

# name = "Rahul"
# course = "Python Programming"
# course_duration = 6
# print(name, "is enrolled in", course, "which has a duration of", course_duration, "months.")
# print(f"ss{name} is enrolled in {course} which has a duration of {course_duration} months.")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("Sum:", num1 + num2)
# print("Difference:", num1 - num2)
# print("Product:", num1 * num2)
# print("Division:", num1 / num2)

# marks = 75
# if marks >=90:
#     print("A Grade")
# elif marks >= 80:
#     print("B Grade")
# else:
#     print("Grade C")

# condition statements - if, elif, else example 
# age = int (input("Enter your age:"))
# if age >= 18:
#     print("You are an adult.")
# elif age >=  13 and age <65:
#     print("You are a teenager.")
# else:  
#     print("You are a senior citizen.")    

# list_1 = [1, 2, 3, 4, 5]
# for num in list_1:  
#      if num % 2 == 0:
#           print(f"{num} is even.")
# else:
#     print(f"{num} is odd:") 

# list_1 = [1, 2, 3, 4, 5]
# index = 0
# while index <  len(list_1):
#  print(list_1[index])
#  index += 1

# try:
#     num1 = int(input("Enter first number: ")) 
#     num2 = int(input("Enter second number: "))
#     rresult = num1 /num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")
# except IndentationError:
#     print("Error: Indentation error in the code.")
# except Exception as e:
#     print("An unexpected error occurred:", str(e))
# finally:
#     print("This block will always execute.")

# try:
#     age = int (input("Enter your age: "))
#     if age <0:
#         raise ValueError("Age cannot be negative.")
#     elif age < 18:
#         print("You are a minor.")
#     elif age >=18 and age < 65:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")
# except ValueError as ve:            
#     print("Error:", ve)
# finally:
#     print("This block will always execute.")    

import numpy as np

# arr_1 = np.array([1, 2, 3, 4, 5])
# print("Array:", arr_1)
# print("Shape:", arr_1.shape)

# arr_2 = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D Array:", arr_2)
# print("Shape:", arr_2.shape)

# arr_3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print("3D Array:", arr_3)
# print("Shape:", arr_3.shape)


# arr_4 = np.array([1, 2, 3, 4, 5])
# print(arr_4 + 10)
# print(arr_4 * 2)
# print(arr_4 ** 2)
# print(np.sqrt(arr_4))
# print(np.sum(arr_4))
# print(np.mean(arr_4))
# print(np.median(arr_4))
# print(np.std(arr_4))
# print(np.var(arr_4))
# print(np.min(arr_4))
# print(np.max(arr_4))
# print(np.argmin(arr_4))
# print(np.argmax(arr_4))

# arr_5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_5[0])
# print(arr_5[1])
# print(arr_5[2])
# print(arr_5[:,0])
# print(arr_5[:,1])
# print(arr_5[:,2])
# print(arr_5[0, 0])
# print(arr_5[1, 1])
# print(arr_5[2, 2])

# print(np.transpose(arr_5))
# print(np.dot(arr_5, arr_5))
# print(np.zeros((2, 3)))
# print(np.ones((2, 3)))
# print(np.eye(3))

# print(np.random.rand(2, 3))
# print(np.random.randint(1, 10, size = (2, 3)))
