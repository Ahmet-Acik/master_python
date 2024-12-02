import random


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.age}, {self.color}"

    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age}, color={self.color})"

    def bark(self):
        print("Bark bark bark")

    def sleep(self):
        print("Zzzzzzzzz")

    def eat(self):
        print("Nom nom nom")

    def wag_tail(self):
        print("Wag wag wag")

    def run(self):
        print("Running")

    def walk(self):
        print("Walking")

    def sit(self):
        print("Sitting")


fino = Dog("Fino", 5, "Brown")
print(fino.name)
print(fino.age)
print(fino.color)

lily = Dog("Lily", 3, "White")
print(lily.name)

paty = Dog("Paty", 2, "Black")

paty


my_dog_list = [
    Dog("Fino", 5, "Brown"),
    Dog("Lily", 3, "White"),
    Dog("Paty", 2, "Black"),
    Dog("Bella", 1, "Brown"),
    Dog("Luna", 4, "White"),
]

my_dogs_under_3 = [x for x in my_dog_list if x.age < 3]
print(my_dogs_under_3)


for x in my_dog_list:
    print(x.name)
    print(x.age)
    print(x.color)
    print("-----")


class Student:

    scholl_name = "B&H High School"
    
    @classmethod
    def change_school_name(cls, new_name):
        cls.scholl_name = new_name


    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

        

furkan = Student("Furkan", 25, "Computer Science")
alper = Student("Alper", 24, "Finance")
omer = Student("Omer", 23, "Computer Science")
ibrahim = Student("Ibrahim", 22, "Economics")
mert = Student( "Mert", 21, "History")


# print(furkan.scholl_name)
# print(alper.scholl_name)
# print(omer.scholl_name)
# print(ibrahim.scholl_name)
# print(mert.scholl_name)

print(furkan.name)
# print(alper.name)
# print(omer.name)
# print(ibrahim.name)
print(mert.name)

print(Student.scholl_name)
print(furkan.scholl_name)

Student.change_school_name("B&H College")
print(Student.scholl_name)




random_number = random.randint(1, 100)
print(random_number)


furkan.name = "Faruk"
print(furkan.name)


# print(Student.name)
# print(Student.age)
# print(Student.major)

from oop import BankAccount

furkan_account = BankAccount()
print(furkan_account.get_balance())
furkan_account.deposit(500)
print(furkan_account.get_balance())
furkan_account.withdraw(200)
print(furkan_account.get_balance())
furkan_account.withdraw(2000)
print(furkan_account.get_balance())
