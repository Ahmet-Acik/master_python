'''
class BankAccount:
    # Properties
    account_number
    account_holder
    balance
    
    # Methods
    deposit(amount)
    withdraw(amount)
    get_balance()
'''
class BankAccount:
    
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")
            
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.balance
    
# my_accont = BankAccount("123456789", "Furkan", 1000)
# whitdrwal_amount = my_accont.withdraw(500)
# get_balance = my_accont.get_balance()
# print(get_balance)

# whitdrwal_amount2 = my_accont.withdraw(400)
# get_balance2 = my_accont.get_balance()
# print(get_balance2)


"""
class Car:
    # Properties
    make
    model
    year
    color
    current_speed
    
    # Methods
    start()
    stop()
    accelerate(amount)
    brake(amount)

  self.assertEqual(car.speed, 50)
        self.assertEqual(car.is_moving, True)
        self.assertEqual(car.is_parked, False)
"""

class Car:
    
    def __init__(self, make, model, year, color, current_milage = 0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.current_milage = current_milage
        self.current_speed = 0
        self.is_engine_on = False
        self.is_moving = False
        self.is_parked = True
        
        
    def start(self):
        self.is_engine_on = True
        self.is_moving = False
        self.is_parked = False
        print("The car has been started")
        
    def stop(self):
        self.is_engine_on = False
        self.is_moving = False
        self.is_parked = True
        print("The car has been stopped")
        
    def accelerate(self, amount):
        self.is_moving = True
        self.current_speed += amount
        print(f"The car is going {self.current_speed} km/h")
        
    def brake(self, amount):
        self.current_speed -= amount
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"The car is going {self.current_speed} km/h")
    
            
   
        
# my_car = Car("Toyota", "Corolla", 2020, "Black")  
    
# my_car = Car("BMW", "X5", 2021, "Black", 12000)
# my_car.start()
# my_car.accelerate(50)
# my_car.brake(50)


"""
class Student:
    # Properties
    student_id
    name
    age
    grades
    
    # Methods
    add_grade(grade)
    calculate_average()
    get_details()

"""

class Student:
        
        def __init__(self, student_id, name, age):
            self.student_id = student_id
            self.name = name
            self.age = age
            self.grades = []
            
        def add_grade(self, grade):
            self.grades.append(grade)
            
        def calculate_average(self):
            return sum(self.grades) / len(self.grades)
        
        def get_details(self):
            return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}"
        
# my_student = Student(123456, "Furkan", 25)
# my_student.add_grade(90)
# my_student.add_grade(80)
# my_student.add_grade(70)
# my_student.add_grade(100)
# my_student.add_grade(95)

# average = my_student.calculate_average()
# print(average)

# details = my_student.get_details()
# print(details)


"""
class Employee:
    # Properties
    employee_id
    name
    position
    salary
    
    # Methods
    give_raise(amount)
    display_information()

"""

class Employee:
    
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        
    def give_raise(self, amount):
        self.salary += amount
        
    def display_information(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
    
my_employee = Employee(123456, "Furkan", "Software Developer", 100000)
my_employee.give_raise(10000)
information = my_employee.display_information()
print(information)

"""
class Product:
    # Properties
    product_id
    name
    price
    stock
    
    # Methods
    sell(amount)
    restock(amount)
    get_details()
"""

class Product:
        
        def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
            
        def sell(self, amount):
            if amount <= self.stock:
                self.stock -= amount
            else:
                print("Insufficient stock")
                
        def restock(self, amount):
            self.stock += amount
            
        def get_details(self):
            return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

my_product = Product(123456, "Laptop", 1000, 10)
my_product.sell(5)
my_product.restock(10)
details = my_product.get_details()
print(details)


"""
class Library:
    # Properties
    name
    location
    books
    members
    
    # Methods
    add_book(book)
    remove_book(book)
    register_member(member)
    lend_book(book, member)
    return_book(book, member)

"""
class Library:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
        
    def register_member(self, member):
        self.members.append(member)
        
    def lend_book(self, book, member):
        if book in self.books and member in self.members:
            print(f"{book} has been lent to {member}")
        else:
            print("Book or member not found")
            
    def return_book(self, book, member):
        if book in self.books and member in self.members:
            print(f"{book} has been returned by {member}")
        else:
            print("Book or member not found")
            
my_library = Library("City Library", "New York")
my_library.add_book("Book1")
my_library.add_book("Book2")
my_library.add_book("Book3")
print(my_library.books)
my_library.register_member("Member1")
my_library.register_member("Member2")
print(my_library.members)
my_library.lend_book("Book1", "Member1")
my_library.return_book("Book1", "Member1")


"""
class Smartphone:
    # Properties
    brand
    model
    storage_capacity
    battery_life
    is_on
    
    # Methods
    power_on()
    power_off()
    make_call(number)
    send_message(number, message)

"""
class Smartphone:
        
        def __init__(self, brand, model, storage_capacity, battery_life):
            self.brand = brand
            self.model = model
            self.storage_capacity = storage_capacity
            self.battery_life = battery_life
            self.is_on = False
            
        def power_on(self):
            self.is_on = True
            print("The phone is on")
            
        def power_off(self):
            self.is_on = False
            print("The phone is off")
            
        def make_call(self, number):
            if self.is_on:
                print(f"Calling {number}")
            else:
                print("Phone is off")
                
        def send_message(self, number, message):
            if self.is_on:
                print(f"Sending message to {number}: {message}")
            else:
                print("Phone is off")
                
my_phone = Smartphone("Apple", "iPhone 16", "512GB", "24 hours")
my_phone.power_on()
my_phone.make_call("123456789")
my_phone.send_message("123456789", "Hello")
my_phone.power_off()


"""
class Hotel:
    # Properties
    name
    location
    rooms
    amenities
    
    # Methods
    check_availability()
    book_room(customer)
    cancel_booking(booking_id)
    add_amenity(amenity)
"""

class Hotel:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []
        self.amenities = []
        
    def check_availability(self):
        return len(self.rooms)
    
    def book_room(self, customer):
        if self.check_availability() > 0:
            print(f"{customer} has booked a room")
            self.rooms.pop()
        else:
            print("No rooms available")
            
    def cancel_booking(self, booking_id):
        print(f"Booking {booking_id} has been cancelled")
        
    def add_amenity(self, amenity):
        self.amenities.append(amenity)
        
my_hotel = Hotel("Grand Hotel", "New York")
my_hotel.rooms = ["Room1", "Room2", "Room3"]
print(my_hotel.check_availability())
my_hotel.book_room("Furkan")
my_hotel.cancel_booking("123456")
my_hotel.add_amenity("Swimming pool")
print(my_hotel.amenities)


"""
class ShoppingCart:
    # Properties
    items
    total_price
    
    # Methods
    add_item(item, price)
    remove_item(item)
    calculate_total()
    checkout()
    

"""

class ShoppingCart:
    
    def __init__(self):
        self.items = {}
        self.total_price = 0
        
    def add_item(self, item, price):
        self.items[item] = price
        
    def remove_item(self, item):
        del self.items[item]
        
    def calculate_total(self):
        self.total_price = sum(self.items.values())
        return self.total_price
    
    def checkout(self):
        print(f"Total price: {self.total_price}")   
        
my_cart = ShoppingCart()
my_cart.add_item("Laptop", 1000)
my_cart.add_item("Phone", 500)
my_cart.add_item("Tablet", 300)
print(my_cart.items)
my_cart.remove_item("Phone")
print(my_cart.items)
total = my_cart.calculate_total()
print(total)
my_cart.checkout()


"""
class Bank:

    # Properties
    name
    location
    accounts
    
    # Methods
    add_account(account)
    remove_account(account)
    calculate_total_deposits()
    calculate_total_withdrawals()
    calculate_total_balance()
    
"""
class Bank:
    
        def __init__(self, name, location):
            self.name = name
            self.location = location
            self.accounts = []
            
        def add_account(self, account):
            self.accounts.append(account)
            
        def remove_account(self, account):
            self.accounts.remove(account)
            
        def calculate_total_deposits(self):
            return sum(account.deposits for account in self.accounts)
        
        def calculate_total_withdrawals(self):
            return sum(account.withdrawals for account in self.accounts)
        
        def calculate_total_balance(self):
            return sum(account.balance for account in self.accounts)
        

"""
class school:

    # Properties
    name
    location
    students
    teachers
    
    # Methods
    add_student(student)
    remove_student(student)
    add_teacher(teacher)
    remove_teacher(teacher)
    calculate_average_grade()
    calculate_student_count()
    calculate_teacher_count()
    
"""
class School:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.students = []
        self.teachers = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def remove_student(self, student):
        self.students.remove(student)
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def remove_teacher(self, teacher):
        self.teachers.remove(teacher)
        
    def calculate_average_grade(self):
        return sum(student.grade for student in self.students) / len(self.students)
    
    def calculate_student_count(self):
        return len(self.students)
    
    def calculate_teacher_count(self):
        return len(self.teachers)
    
    
    

"""
class Restaurant:

    # Properties
    name
    location
    menu
    employees
    
    # Methods
    add_dish(dish)
    remove_dish(dish)
    add_employee(employee)
    remove_employee(employee)
    calculate_total_sales()
    calculate_total_expenses()
    calculate_total_profit()
    
"""
class Restaurant:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = []
        self.employees = []
        
    def add_dish(self, dish):
        self.menu.append(dish)
        
    def remove_dish(self, dish):
        self.menu.remove(dish)
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def calculate_total_sales(self):
        return sum(employee.sales for employee in self.employees)
    
    def calculate_total_expenses(self):
        return sum(employee.expenses for employee in self.employees)
    
    def calculate_total_profit(self):
        return self.calculate_total_sales() - self.calculate_total_expenses()
    
    

"""
class Hospital:
    
    # Properties
    name
    location
    patients
    doctors
    
    # Methods
    add_patient(patient)
    remove_patient(patient)
    add_doctor(doctor)
    remove_doctor(doctor)
    calculate_total_patients()
    calculate_total_doctors()
    calculate_average_age()
    
"""
class Hospital:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.patients = []
        self.doctors = []
        
    def add_patient(self, patient):
        self.patients.append(patient)
        
    def remove_patient(self, patient):
        self.patients.remove(patient)
        
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        
    def remove_doctor(self, doctor):
        self.doctors.remove(doctor)
        
    def calculate_total_patients(self):
        return len(self.patients)
    
    def calculate_total_doctors(self):
        return len(self.doctors)
    
    def calculate_average_age(self):
        return sum(patient.age for patient in self.patients) / len(self.patients)       
    
    
    
"""
class Gym:
        
    # Properties
    name
    location
    members
    trainers
    
    # Methods
    add_member(member)
    remove_member(member)
    add_trainer(trainer)
    remove_trainer(trainer)
    calculate_total_members()
    calculate_total_trainers()
    calculate_average_age()
    
"""
class Gym:
        
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.members = []
        self.trainers = []
        
    def add_member(self, member):
        self.members.append(member)
        
    def remove_member(self, member):
        self.members.remove(member)
        
    def add_trainer(self, trainer):
        self.trainers.append(trainer)
        
    def remove_trainer(self, trainer):
        self.trainers.remove(trainer)
        
    def calculate_total_members(self):
        return len(self.members)
    
    def calculate_total_trainers(self):
        return len(self.trainers)
    
    def calculate_average_age(self):
        return sum(member.age for member in self.members) / len(self.members)

        
"""
class Zoo:

        # Properties
        name
        location
        animals
        employees
        
        # Methods
        add_animal(animal)
        remove_animal(animal)
        add_employee(employee)
        remove_employee(employee)
        calculate_total_animals()
        calculate_total_employees()
        calculate_average_age()
        
"""
class Zoo:
            
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = []
        self.employees = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def remove_animal(self, animal):
        self.animals.remove(animal)
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def calculate_total_animals(self):
        return len(self.animals)
    
    def calculate_total_employees(self):
        return len(self.employees)
    
    def calculate_average_age(self):
        return sum(animal.age for animal in self.animals) / len(self.animals)
            
"""
class University:
        
    # Properties
    name
    location
    students
    professors
    
    # Methods
    add_student(student)
    remove_student(student)
    add_professor(professor)
    remove_professor(professor)
    calculate_total_students()
    calculate_total_professors()
    calculate_average_age()
    
"""
class University:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.students = []
        self.professors = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def remove_student(self, student):
        self.students.remove(student)
        
    def add_professor(self, professor):
        self.professors.append(professor)
        
    def remove_professor(self, professor):
        self.professors.remove(professor)
        
    def calculate_total_students(self):
        return len(self.students)
    
    def calculate_total_professors(self):
        return len(self.professors)
    
    def calculate_average_age(self):
        return sum(student.age for student in self.students) / len(self.students)
    

"""
class CoffeeShop:

        # Properties
        name
        location
        menu
        employees
        
        # Methods
        add_item(item)
        remove_item(item)
        add_employee(employee)
        remove_employee(employee)
        calculate_total_sales()
        calculate_total_expenses()
        calculate_total_profit()
        
""" 
class CoffeeShop:
        
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = []
        self.employees = []
        
    def add_item(self, item):
        self.menu.append(item)
        
    def remove_item(self, item):
        self.menu.remove(item)
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def calculate_total_sales(self):
        return sum(employee.sales for employee in self.employees)
    
    def calculate_total_expenses(self):
        return sum(employee.expenses for employee in self.employees)
    
    def calculate_total_profit(self):
        return self.calculate_total_sales() - self.calculate_total_expenses()   