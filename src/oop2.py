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


# multiple inheritance
# person/ employee / It professional


class People:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def update_address(self, new_address):
        self.address = new_address
        print(f"Address updated to: {self.address}")


class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def work(self):
        print(f"Employee {self.emp_id} is working.")

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by {amount}. New salary: {self.salary}")


class ITProfessional(People, Employee):
    def __init__(self, name, age, address, emp_id, salary, role, skills):
        self.role = role
        self.skills = skills
        People.__init__(self, name, age, address)
        Employee.__init__(self, emp_id, salary)

    def code(self):
        print(f"{self.name} is coding in {', '.join(self.skills)}.")

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Skill {skill} added. Current skills: {', '.join(self.skills)}")


# Example usage
it_professional = ITProfessional(
    "Alice", 30, "123 Main St", "E123", 70000, "Developer", ["Python", "JavaScript"]
)
it_professional.introduce()
it_professional.update_address("456 Elm St")
it_professional.work()
it_professional.give_raise(5000)
it_professional.code()
it_professional.add_skill("Java")


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on.")

    def power_off(self):
        print(f"{self.brand} {self.model} is powering off.")


class InternetConnectedDevice:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def connect_to_internet(self):
        print(f"Connecting to the internet with IP address {self.ip_address}.")

    def disconnect_from_internet(self):
        print(f"Disconnecting from the internet with IP address {self.ip_address}.")


class SmartLight(Device, InternetConnectedDevice):
    def __init__(self, brand, model, ip_address, brightness):
        Device.__init__(self, brand, model)
        InternetConnectedDevice.__init__(self, ip_address)
        self.brightness = brightness

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"Brightness set to {self.brightness}.")


# Example usage
smart_light = SmartLight("Philips", "Hue", "192.168.1.10", 75)
smart_light.power_on()
smart_light.connect_to_internet()
smart_light.set_brightness(100)
smart_light.disconnect_from_internet()
smart_light.power_off()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def study(self):
        print(f"Studying {self.major}.")


class TeachingAssistant(Person, Student):
    def __init__(self, name, age, student_id, major, courses):
        Person.__init__(self, name, age)
        Student.__init__(self, student_id, major)
        self.courses = courses

    def assist(self):
        print(f"{self.name} is assisting in courses: {', '.join(self.courses)}.")


# Example usage
ta = TeachingAssistant("Alice", 25, "S12345", "Computer Science", ["CS101", "CS102"])
ta.introduce()
ta.study()
ta.assist()


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.year} {self.make} {self.model} is stopping.")


class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the battery to {self.battery_capacity} kWh.")


class HybridCar(Vehicle, ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricVehicle.__init__(self, battery_capacity)
        self.fuel_capacity = fuel_capacity

    def refuel(self):
        print(f"Refueling the car with {self.fuel_capacity} liters of fuel.")


# Example usage
hybrid_car = HybridCar("Toyota", "Prius", 2022, 8.8, 45)
hybrid_car.start()
hybrid_car.charge()
hybrid_car.refuel()
hybrid_car.stop()


class MediaPlayer:
    def __init__(self, supported_formats):
        self.supported_formats = supported_formats

    def play(self, format):
        if format in self.supported_formats:
            print(f"Playing {format} format.")
        else:
            print(f"Format {format} not supported.")


class Recorder:
    def __init__(self, recording_quality):
        self.recording_quality = recording_quality

    def record(self):
        print(f"Recording in {self.recording_quality} quality.")


class SmartMediaDevice(MediaPlayer, Recorder):
    def __init__(self, supported_formats, recording_quality, storage_capacity):
        MediaPlayer.__init__(self, supported_formats)
        Recorder.__init__(self, recording_quality)
        self.storage_capacity = storage_capacity

    def store_media(self):
        print(f"Storing media in {self.storage_capacity} GB storage.")


# Example usage
smart_media_device = SmartMediaDevice(["mp3", "mp4"], "HD", 128)
smart_media_device.play("mp3")
smart_media_device.record()
smart_media_device.store_media()


# abstract class
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Example usage
circle = Circle(5)
print(circle.area())
print(circle.perimeter())


# polimorphism


class dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"


class cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow!"


class mouse:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Squeak!"


def animal_speak(animal):  # common interface
    print(animal.speak())


# Example usage
animal_speak(dog("Tommy"))
animal_speak(cat("Kitty"))
animal_speak(mouse("Jerry"))


# Mixins  (is-a relationship)  (Person is a JSON)  (Person is a XML) (Person is a CSV)  (Person is a PDF)  (Person is a HTML)


class JSONMixin:
    def to_json(self):
        import json

        return json.dumps(self.__dict__)


class XMLMixin:
    def to_xml(self):
        xml = []
        for key, value in self.__dict__.items():
            xml.append(f"<{key}>{value}</{key}>")
        return "".join(xml)


class Person(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Example usage
person = Person("Alice", 30)
print(person.to_json())
print(person.to_xml())


class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")


from datetime import datetime


class TimestampMixin:
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class User(LoggingMixin, TimestampMixin):
    def __init__(self, username):
        self.username = username

    def display_user(self):
        self.log(f"User: {self.username}")
        print(f"Timestamp: {self.get_timestamp()}")


class Product(LoggingMixin, TimestampMixin):
    def __init__(self, product_name):
        self.product_name = product_name

    def display_product(self):
        self.log(f"Product: {self.product_name}")
        print(f"Timestamp: {self.get_timestamp()}")


# Example usage
user = User("Alice")
user.display_user()

product = Product("Laptop")
product.display_product()


# Composition over inheritance  (has-a relationship)  (Car has an engine)  (Car has a wheel) (Car has a door) (Car has a seat) (Car has a steering wheel)


class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print("Engine starting.")

    def stop(self):
        print("Engine stopping.")


class Car:
    def __init__(self):
        self.engine = Engine(2.0)

    def start(self):
        print("Car starting.")
        self.engine.start()

    def stop(self):
        print("Car stopping.")
        self.engine.stop()


# Example usage
car = Car()
car.start()
car.stop()


class CPU:
    def __init__(self, model):
        self.model = model

    def process(self):
        print(f"CPU {self.model} processing.")


class RAM:
    def __init__(self, size):
        self.size = size

    def load(self):
        print(f"RAM {self.size}GB loading.")


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

    def read(self):
        print(f"Storage {self.capacity}GB reading.")

    def write(self):
        print(f"Storage {self.capacity}GB writing.")


class Computer:
    def __init__(self, cpu_model, ram_size, storage_capacity):
        self.cpu = CPU(cpu_model)
        self.ram = RAM(ram_size)
        self.storage = Storage(storage_capacity)

    def start(self):
        self.cpu.process()
        self.ram.load()
        self.storage.read()
        print("Computer starting.")


# Example usage
computer = Computer("Intel i7", 16, 512)
computer.start()


class Room:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def describe(self):
        print(f"{self.name} with area {self.area} square meters.")


class House:
    def __init__(self, rooms):
        self.rooms = rooms

    def describe(self):
        for room in self.rooms:
            room.describe()


# Example usage
living_room = Room("Living Room", 20)
kitchen = Room("Kitchen", 15)
bedroom = Room("Bedroom", 25)

house = House([living_room, kitchen, bedroom])
house.describe()
