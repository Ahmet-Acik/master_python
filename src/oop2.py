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


