class Dog:

    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def purr(self):
        print(f"{self.name} purrs")

    def bark(self):
        print(f'{self.name} says "Woof!"')


my_dog = Dog("Rex", 3, "German Shepherd")  # Create an instance of the Dog class
my_dog.bark()
my_dog.purr()
my_dog.age = 4  # Change the age attribute of the Dog class
print(my_dog.age)  # Print the age attribute of the Dog class
print(my_dog.breed)  # Print the breed attribute of the Dog class
print(my_dog.name)  # Print the name attribute of the Dog class
print(my_dog.species)  # Print the species attribute of the Dog class

another_dog = Dog("Buddy", 5, "Golden Retriever")

patients = [
    Dog("Rex", 3, "German Shepherd"),
    Dog("Buddy", 5, "Golden Retriever"),
    Dog("Max", 2, "Poodle"),
]


class Cat:

    species = "Felis catus"  # Class attribute

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def purr(self):
        print(f"{self.name} purrs")

    def meow(self):
        print(f'{self.name} says "Meow!"')


class MathOperations:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(csl, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        return a / b


print(MathOperations.add(2, 3))  # 5


class Rectangle:

    def __init__(self, width, height):
        self.width = (width,)
        self.height = height

    def area(self, width, height):
        return width * height

    def perimeter(self, width, height):
        return 2 * (width + height)


rect = Rectangle(3, 4)
print(rect.area(3, 4))  # 12
print(rect.perimeter(3, 4))  # 14


class Car:

    def __int__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __del__(self):
        print("The car has been deleted")


class FileHandler:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "w")
        print(f"File {file_name} has been opened")

    def __del__(self):
        self.file.close()
        print(f"File {self.file_name} has been closed")


# Encapsulation
class BankAccount:

    def __init__(self):
        self.__balance = 0 # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Balance: {self.balance}"



# access modifiers

# Encapsulation
class BankAccount:

    def __init__(self):
        self.__balance = 0  # Private attribute
        self._account_number = "123456789"  # Protected attribute
        self.owner = "John Doe"  # Public attribute

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    # Public method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # Public method
    def get_balance(self):
        return self.__balance

    # Protected method
    def _get_account_number(self):
        return self._account_number

    # Private method
    def __calculate_interest(self):
        return self.__balance * 0.05

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}, Account Number: {self._account_number}"

# # Example usage
# account = BankAccount()
# account.deposit(100)
# print(account)  # Output: Owner: John Doe, Balance: 100, Account Number: 123456789

# # Accessing public attribute
# print(account.owner)  # Output: John Doe

# # Accessing protected attribute (not recommended)
# print(account._account_number)  # Output: 123456789

# # Accessing private attribute (will raise an AttributeError)
# try:
#     print(account.__balance)
# except AttributeError as e:
#     print(e)  # Output: 'BankAccount' object has no attribute '__balance'

# # Accessing private attribute using name mangling (not recommended)
# print(account._BankAccount__balance)  # Output: 100

# # Accessing protected method (not recommended)
# print(account._get_account_number())  # Output: 123456789

# # Accessing private method using name mangling (not recommended)
# print(account._BankAccount__calculate_interest())  # Output: 5.0

import abc 

class Animal(abc.ABC):
    
        @abc.abstractmethod
        def make_sound(self):
            pass
        
        @abc.abstractmethod
        def eat(self):
            pass
            
            
class Dog(Animal):
        
        def make_sound(self):
            print("Woof!")
            
        def eat(self):
            print("Dog is eating")
        
class Cat(Animal):
        
            def make_sound(self):
                print("Meow!")
                
            def eat(self):
                print("Cat is eating")
                
class Cow(Animal):
    
    def make_sound(self):
        print("Moo!")
        
    def eat(self):
        print("Cow is eating")
        
my_dog = Dog()
my_dog.make_sound()

my_cat = Cat()
my_cat.make_sound()

my_cow = Cow()
my_cow.make_sound()

try:
    my_animal = Animal()
except TypeError as e:
    print(e)
    

animals = [my_dog, my_cat, my_cow]

for animal in animals:
    animal.make_sound()
    animal.eat()
    