# class Person:
#     def _init_(self,name,age):
#         self.name = name
#         self.age = age
#         def greet(self):
#             print(f"Hello My Name is {self.name} and I am {self.age} years old. ")
#             person1 = Person("Najrin", 25)
#             person1.greet()
                            
# 2
# class car:
#     def __init__(self, brand, model):
#       self.brand = brand
#       self.model = model
    
#     def display_details(self):
#          print(f"Car Brand:{self.brand} Model {self.model}")
        
# car1 = car("Toyoto", "corolla")
# car1.display_details()

# class BankAccount:
#     def __init__(self, account_name, balance):
#         self.account_name = account_name
#         self.balance = balance



# account1 = BankAccount("1256789053233", 1000)
# print("Account Number:", account1.account_name)
# print("Balance:", account1.balance)


# 1️⃣ Library Management System
# class Book:
#     def __init__(self, title, author, id):
#         self.title = title
#         self.author = author
#         self.id = id
#         self.is_available = True

# class Member:
#     def __init__(self, name, member_id):
#         self.name = name
#         self.member_id = member_id
#         self.borrowed_books = []

# class Library:
#     def __init__(self):
#         self.books = []

#     def show_books(self):
#         for book in self.books:
#             print(book.title + ", " + book.author + ", "+ str(book.id))

#     def add_book(self, book):
#         self.books.append(book)
#         self.show_books()

#     def borrow_book(self, book_id):
#         for book in self.books:
#             if book.book_id == book_id and book.is_available:
#                 book.is_available = False
#                 return "Book Borrowed"
#         return "Book not available"

# member1 = Member("Najrin", 1)
# member2 = Member("chobi", 2)

# book1 = Book("The ekn babu","ekn", 101)
# book2 = Book("I kill my spouse","mistu", 102)

# lib1  = Library()
# lib1.add_book(book1)
# lib1.add_book(book2)

# 2️⃣ Shopping Cart System
# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price


# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add_product(self, product, quantity=1):
#         if product.product_id in self.items:
#             self.items[product.product_id]["quantity"] += quantity
#         else:
#             self.items[product.product_id] = {
#                 "product": product,
#                 "quantity": quantity
#             }

#     def remove_product(self, product_id):
#         if product_id in self.items:
#             del self.items[product_id]

#     def calculate_total(self):   
#         return sum(
#             item["product"].price * item["quantity"]   
#             for item in self.items.values()
#         )  

#     def view_cart(self):
#         for item in self.items.values():
#             product = item["product"]
#             quantity = item["quantity"]
#             print(f"{product.name} x {quantity} = {product.price * quantity}")



# if __name__ == "__main__":
#     p1 = Product(1, "Laptop", 800)
#     p2 = Product(2, "Phone", 500)

#     cart = ShoppingCart()
#     cart.add_product(p1, 1)
#     cart.add_product(p2, 2)

#     cart.view_cart()
#     print("Total:", cart.calculate_total())

# 3️⃣ ATM System
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return "Success"
#         else:
#             return "Insufficient funds"


# class ATM:
#     def __init__(self, account):
#         self.account = account   # ✅ fixed

#     def perform_withdrawal(self, amount):
#         return self.account.withdraw(amount)


# if __name__ == "__main__":
#     account = BankAccount(1000)
#     atm = ATM(account)

#     print(atm.perform_withdrawal(300))
#     print("Remaining Balance:", account.balance)



# 5️⃣ Movie Ticket Booking System
# class Movie:
#     def __init__(self, name, seats):
#         self.name = name
#         self.available_seats = seats

#     def book_ticket(self, count):
#         if count <= self.available_seats:
#             self.available_seats -= count
#             return "Booked"
#         return "Not enough seats"



# if __name__ == "__main__":
#     movie = Movie("Avengers", 100)

#     print(movie.book_ticket(5))
#     print("Remaining seats:", movie.available_seats)



# 6️⃣ Hotel Reservation System
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_booked = False


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self):
        for room in self.rooms:
            if not room.is_booked:
                room.is_booked = True
                return f"Room {room.room_number} booked"
        return "No rooms available"



if __name__ == "__main__":
    hotel = Hotel()


    hotel.add_room(Room(101))
    hotel.add_room(Room(102))
    hotel.add_room(Room(103))

    # Book room
    print(hotel.book_room())
    print(hotel.book_room())
    print(hotel.book_room())
    print(hotel.book_room()) 