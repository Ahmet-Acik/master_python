class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print(f"{self.name} speaks")


class Dog(Animal):

    def __init__(self, name, age, color, breed):
        self.breed = breed
        super().__init__(name, age, color)

    def bark(self):
        print(f"{self.name} says Woof")


class Cat(Animal):

    def __init__(self, name, age, color, breed):
        self.breed = breed
        super().__init__(name, age, color)

    def meaw(self):
        print(f"{self.name} says Meow")


dog = Dog("Tommy", 5, "Brown", "Bulldog")
dog.speak()
dog.bark()
cat = Cat("Kitty", 3, "White", "Persian")
cat.speak()
cat.meaw()

print(dog.age)
print(dog.breed)
print(cat.color)
print(cat.breed)


