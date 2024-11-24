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
