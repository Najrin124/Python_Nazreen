
# with open("test3.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open ("test3.txt", "r") as file:
#  file.write("Hello, this a test file.\n")
#  file.write("This file is use for demostraing file handleing in python.\n")

# with open ("test3.txt", "r") as file:
#     file.write("\n Hello this append line \n")
#     file.write("This file is use for demostraing file handleing in python.\n")

import datetime
# date = datetime.date(2024, 7 ,1)
# print(date)

# now = datetime.datetime.now()
# print(now)

# today = datetime.date.today()
# print(today)

# today_time = datetime.datetime.today()
# print(today_time)


date_str = "2024-06-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d") 
print(date_obj) 

# date_obj = datetime.datetime(25, 2, 11)
# date_str = date_obj.strftime("%Y-%m-%d") 
# print(date_str)

# from datetime import datetime, timedelta
# delta = timedelta(days = 5)
# print(delta)

# now = datetime.now()
# future = now + timedelta(days = 7, hours = 2)
# print(future)

# past = now - timedelta(weeks=2)
# print(f"passtime: {past}")


# date1 = datetime(23, 10, 6) 
# date2 = datetime(23, 10, 10) 
# difference = date2 - date1
# print(f"Difference: {difference}")
# print(f"Total days: {difference.days} ")


# negative_delta = timedelta(days = -3)
# adjusted = now + negative_delta
# print(f"Adjusted time:  {adjusted}")

# short_delta = timedelta(seconds=3600, minutes=30)
# print(f"Short delta: {short_delta}")