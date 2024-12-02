
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
    
my_accont = BankAccount("123456789", "Furkan", 1000)
whitdrwal_amount = my_accont.withdraw(500)
get_balance = my_accont.get_balance()
print(get_balance)

whitdrwal_amount2 = my_accont.withdraw(400)
get_balance2 = my_accont.get_balance()
print(get_balance2)


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

"""

class Car:
    
    def __init__(self, make, model, year, color, current_milage = 0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.current_milage = current_milage
        self.current_speed = 0
        
        
    def start(self):
        print("The car has been started")
        
    def stop(self):
        print("The car has been stopped")
        
    def accelerate(self, amount):
        self.current_speed += amount
        print(f"The car is going {self.current_speed} km/h")
        
    def brake(self, amount):
        self.current_speed -= amount
        print(f"The car will stop in {self.current_speed} km/h distance")
    
my_car = Car("BMW", "X5", 2021, "Black", 12000)
my_car.start()
my_car.accelerate(50)
my_car.brake(50)


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
        
my_student = Student(123456, "Furkan", 25)
my_student.add_grade(90)
my_student.add_grade(80)
my_student.add_grade(70)
my_student.add_grade(100)
my_student.add_grade(95)

average = my_student.calculate_average()
print(average)

details = my_student.get_details()
print(details)
