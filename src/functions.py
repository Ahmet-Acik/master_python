"""
    This module contains various examples of Python functions, including:
    1. Basic function definitions and calls:
        - greeting(name): Prints a greeting message.
        - greet(name, age): Prints a greeting message with name and age.
        - describe_pet(animal_type, pet_name): Prints information about a pet.
        - add_item(item, lst=None): Adds an item to a list, with a default empty list.
        - check_age_group(age): Returns a string indicating the age group.
        - add_numbers(a, b): Returns the sum of two numbers.
        - divide_numbers(a, b): Returns the product of two numbers or an error message if division by zero.
    2. Functions as first-class objects:
        - apply_func(func, value): Applies a function to a value.
        - get_power_function(n): Returns a lambda function that raises a number to the power of n.
    3. Lambda functions:
        - Various examples of lambda functions for addition, checking even/odd, filtering, and mapping.
    4. Higher-order functions:
        - filter_list(lst): Filters a list to include only even numbers.
        - double_list(lst): Doubles each element in a list.
        - sum_list(lst): Sums all elements in a list.
        - product_list(lst): Multiplies all elements in a list.
    5. Partial functions:
        - power(base, exponent): Returns the result of base raised to the power of exponent.
        - square: Partial function to square a number.
        - cube: Partial function to cube a number.
    6. Closures:
        - outer_function(x): Returns an inner function that adds x to its argument.
    7. Decorators:
        - my_decorator(func): A simple decorator that prints messages before and after a function call.
        - repeat(num_times): A decorator that repeats the function call a specified number of times.
    Examples of usage are provided for each function.
"""
def greeting(name):
    print(f"Hello {name}!")


greeting("Ahmet")


def greet(name, age):
    print(f"Hello {name}! You are {age} years old.")


greet("Ahmet", 25)
greet(age=30, name="John")

# 
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
    
describe_pet(animal_type="dog", pet_name="Buddy")    

# default value for an argument
def add_item(item, lst=None):  # default value for lst is None
    if lst is None:
        lst = []
    lst.append(item)
    return lst

list_from_add_item = add_item(5)


print(add_item(5))
print(add_item(10))
add_item(5)
add_item(10)


def check_age_group(age):
    if age >= 18:
        return "You are an adult."
    elif age >= 13:
        return "You are a teenager."
    else:
        return "You are a child."


print(check_age_group(25))


def add_numbers(a, b):
    return a + b


print(add_numbers(5, 10))


def divide_numbers(a, b):
    if a == 0 or b == 0:
        return "Error: Division by zero is not allowed."  # return statement ends the function
    return a * b


print(divide_numbers(5, 10))
print(divide_numbers(0, 10))


result = greeting("Ahmet")
print(result)  # None, the function does not return anything explicitly


say_hello = greeting
print(say_hello("Mehmet"))  # Hello Ahmet!


# Function as an argument
def apply_func(func, value):
    return func(value)


def square(x):
    return x**2


def cube(x):
    return x**3


def double(x):
    return x * 2


print(f"apply_func(cube) {apply_func(cube, 5)}")  # 125
print(f"apply_func(square) {apply_func(square, 5)}")  # 25
print(f"apply_func(double) {apply_func(double, 5)}")  # 10

# lambda function
# syntax>  lambda arguments: expression e.g lambda x: x ** 2

add = lambda x, y, z: x + y + z
print(f"add(1,2,3) {add(1,2,3)}")  # 6

print(lambda x: x ** 2, 5)  

even = lambda x: x % 2 == 0
print(f"even(5) {even(5)}")  # False
print(f"even(10) {even(10)}")  # True

odd = lambda x: x % 2 != 0
print(f"odd(5) {odd(5)}")  # True
print(f"odd(10) {odd(10)}")  # False


# lambda function as an argument
def apply_func(func, value):
    return func(value)


print(f"apply_func(lambda x: x ** 2, 5) {apply_func(lambda x: x ** 2, 5)}")  # 25
print(f"apply_func(lambda x: x ** 3, 5) {apply_func(lambda x: x ** 3, 5)}")  # 125
print(f"apply_func(lambda x: x * 2, 5) {apply_func(lambda x: x * 2, 5)}")  # 10


fruits = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango",
    "orange",
    "pineapple",
    "strawberry",
    "watermelon",
    "grape",
    "blueberry",
    "raspberry",
    "blackberry",
    "papaya",
    "pear",
    "peach",
    "plum",
    "pomegranate",
    "melon"
]
fruits_with_p = list(filter(lambda x: x.startswith("p"), fruits))
print(fruits_with_p)

fruits_with_b = list(
    filter(
        lambda x: x.startswith("b"),
        [
            "apple",
            "banana",
            "cherry",
            "kiwi",
            "mango",
            "orange",
            "pineapple",
            "strawberry",
            "melon",
            "watermelon",
            "grape",
            "blueberry",
            "raspberry",
            "blackberry",
            "papaya",
            "pear",
        ],
    )
)
print(fruits_with_b)


fruits = ["apple", "banana", "cherry", "mango", "melon", "orange"]
fruits_with_m = []
for x in fruits:
    if x.startswith("m"):
        fruits_with_m.append(x)

print(fruits_with_m)

print(list(filter(lambda x: x.startswith("m"), fruits)))


# lambda function as a return value
def get_power_function(n):
    return lambda x: x**n


square = get_power_function(2)
cube = get_power_function(3)

print(f"square(5) {square(5)}")  # 25
print(f"cube(5) {cube(5)}")  # 125

# filter function returns a new list with the elements that satisfy the condition
filter_list = lambda lst: [i for i in lst if i % 2 == 0]
print(
    f"filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) {filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}"
)  # [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"even_numbers {list(even_numbers)}")  # [2, 4, 6, 8, 10]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
filtered_fruits = filter(lambda x: x.startswith("a"), fruits)
print(f"filtered_fruits {list(filtered_fruits)}")  # ['apple']

my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "kiwi", 5: "mango"}
filtered_dict = filter(lambda x: x[1].startswith("k"), my_dict.items())
print(f"filtered_dict {dict(filtered_dict)}")  # {4: 'kiwi'}


my_dict = {
    "fruit": "apple",
    "sweet": "candy",
    "cake": "apple pie",
    "drink": "water",
    "food": "apple jam",
    "snack": "candy",
}
filtered_dict = filter(lambda x: x[1].startswith("a"), my_dict.items())
print(
    f"filtered_dict {dict(filtered_dict)}"
)  # {'fruit': 'apple', 'cake': 'apple pie', 'food': 'apple jam'}


# map function transform each element in the list
double_list = lambda lst: [i * 2 for i in lst]
print(
    f"double_list([1, 2, 3, 4, 5]) {double_list([1, 2, 3, 4, 5])}"
)  # [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(f"doubled_numbers {list(doubled_numbers)}")  # [2, 4, 6, 8, 10]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
uppercased_fruits = map(lambda x: x.upper(), fruits)
print(
    f"uppercased_fruits {list(uppercased_fruits)}"
)  # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "kiwi", 5: "mango"}
uppercased_dict = map(lambda x: (x[0], x[1].upper()), my_dict.items())
print(
    f"uppercased_dict {dict(uppercased_dict)}"
)  # {1: 'APPLE', 2: 'BANANA', 3: 'CHERRY', 4: 'KIWI', 5: 'MANGO'}

# reduce function
from functools import reduce

map() # map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
filter() # filter() function returns an iterator 
reduce() # reduce() function returns a single value


print(f"sum_list([1, 2, 3, 4, 5]) {sum_list([1, 2, 3, 4, 5])}")  # 15
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(f"sum_numbers {sum_numbers}")  # 15
product_list = lambda lst: reduce(lambda x, y: x * y, lst)
print(f"product_list([1, 2, 3, 4, 5]) {product_list([1, 2, 3, 4, 5])}")  # 120
numbers = [1, 2, 3, 4, 5]
product_numbers = reduce(lambda x, y: x * y, numbers)
print(f"product_numbers {product_numbers}")  # 120

# partial function
from functools import partial


def power(base, exponent):
    return base**exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5) {square(5)}")  # 25
print(f"cube(5) {cube(5)}")  # 125


# closure
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_5 = outer_function(5)
add_10 = outer_function(10)

print(f"add_5(10) {add_5(10)}")  # 15
print(f"add_10(10) {add_10(10)}")  # 20


# decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)
say_hello()


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello {name}!")


say_hello("Ahmet")


# decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}!")


greet("Ahmet")

def add_item_toList(item, abc=None):
    if abc is None:
        abc = []
    abc.append(item)
    return abc

print(add_item_toList(5))
print(add_item_toList(10))
print(add_item_toList(15))

def add_item_toList(item, abc=[]):
    abc.append(item)
    return abc

print(add_item_toList(5))
print(add_item_toList(10))
print(add_item_toList(15))


def math_operations(a, b, operation):
    return operation(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


print(math_operations(5, 3, add))  
print(math_operations(5, 3, subtract))
print(math_operations(5, 3, multiply))

def math_operations(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    else:
        return "Invalid operation"
    

print(math_operations(5, 3, "+"))
print(math_operations(5, 3, "-"))
print(math_operations(5, 3, "*"))
print(math_operations(5, 3, "/"))

