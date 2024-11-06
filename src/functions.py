def greeting(name):
    print(f"Hello {name}!")


greeting("Ahmet")


def greet(name, age):
    print(f"Hello {name}! You are {age} years old.")


greet("Ahmet", 25)
greet(age=30, name="John")


def add_item(item, lst=None):  # default value for lst is None
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(add_item(5))
print(add_item(10))


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


def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.
    Args:
        a (int or float): The first number to multiply.
        b (int or float): The second number to multiply.
    Returns:
        int or float: The result of multiplying a and b.
        str: Error message if either a or b is zero.
    Raises:
        ValueError: If either a or b is zero.
    """
    
    if a == 0 or b == 0:
        return "Error: Multiplication by zero is not allowed." # return statement ends the function
    return a * b


print(multiply_numbers(5, 10))
print(multiply_numbers(0, 10))


result = greeting("Ahmet")
print(result) # None, the function does not return anything explicitly


say_hello = greeting
print(say_hello("Mehmet")) # Hello Ahmet!

# Function as an argument
def apply_func(func, value):
    return func(value)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def double(x):
    return x * 2


print(f"apply_func(cube) {apply_func(cube, 5)}") # 125
print(f"apply_func(square) {apply_func(square, 5)}") # 25
print(f"apply_func(double) {apply_func(double, 5)}") # 10

# lambda function

add =lambda x,y,z: x+y+z
print(f"add(1,2,3) {add(1,2,3)}") # 6

even = lambda x:x%2==0
print(f"even(5) {even(5)}") # False
print(f"even(10) {even(10)}") # True

odd = lambda x:x%2!=0
print(f"odd(5) {odd(5)}") # True
print(f"odd(10) {odd(10)}") # False


# lambda function as an argument
def apply_func(func, value):
    return func(value)

print(f"apply_func(lambda x: x ** 2, 5) {apply_func(lambda x: x ** 2, 5)}") # 25
print(f"apply_func(lambda x: x ** 3, 5) {apply_func(lambda x: x ** 3, 5)}") # 125
print(f"apply_func(lambda x: x * 2, 5) {apply_func(lambda x: x * 2, 5)}") # 10

# lambda function as a return value
def get_power_function(n):
    return lambda x: x ** n

square = get_power_function(2)
cube = get_power_function(3)

print(f"square(5) {square(5)}") # 25
print(f"cube(5) {cube(5)}") # 125

# filter function returns a new list with the elements that satisfy the condition
filter_list = lambda lst: [i for i in lst if i % 2 == 0]
print(f"filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) {filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}") # [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x:x%2==0, numbers)
print(f"even_numbers {list(even_numbers)}") # [2, 4, 6, 8, 10]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
filtered_fruits = filter(lambda x: x.startswith("a"), fruits)
print(f"filtered_fruits {list(filtered_fruits)}") # ['apple']

my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "kiwi", 5: "mango"}
filtered_dict = filter(lambda x: x[1].startswith("k"), my_dict.items())
print(f"filtered_dict {dict(filtered_dict)}") # {4: 'kiwi'}


# map function transform each element in the list
double_list = lambda lst: [i * 2 for i in lst]
print(f"double_list([1, 2, 3, 4, 5]) {double_list([1, 2, 3, 4, 5])}") # [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(f"doubled_numbers {list(doubled_numbers)}") # [2, 4, 6, 8, 10]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
uppercased_fruits = map(lambda x: x.upper(), fruits) 
print(f"uppercased_fruits {list(uppercased_fruits)}") # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "kiwi", 5: "mango"}
uppercased_dict = map(lambda x: (x[0], x[1].upper()), my_dict.items())
print(f"uppercased_dict {dict(uppercased_dict)}") # {1: 'APPLE', 2: 'BANANA', 3: 'CHERRY', 4: 'KIWI', 5: 'MANGO'}

# reduce function
from functools import reduce
sum_list = lambda lst: reduce(lambda x, y: x + y, lst)
print(f"sum_list([1, 2, 3, 4, 5]) {sum_list([1, 2, 3, 4, 5])}") # 15
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(f"sum_numbers {sum_numbers}") # 15
product_list = lambda lst: reduce(lambda x, y: x * y, lst)
print(f"product_list([1, 2, 3, 4, 5]) {product_list([1, 2, 3, 4, 5])}") # 120
numbers = [1, 2, 3, 4, 5]
product_numbers = reduce(lambda x, y: x * y, numbers)
print(f"product_numbers {product_numbers}") # 120

# partial function
from functools import partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5) {square(5)}") # 25
print(f"cube(5) {cube(5)}") # 125

# closure
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_5 = outer_function(5)
add_10 = outer_function(10)

print(f"add_5(10) {add_5(10)}") # 15
print(f"add_10(10) {add_10(10)}") # 20

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

