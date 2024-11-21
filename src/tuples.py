# tuples.py
"""
This module demonstrates various operations and methods that can be performed on tuples in Python.
Tuples are immutable sequences, typically used to store collections of heterogeneous data. Tuples are defined using parentheses () and can contain any number of elements, separated by commas.
The module covers the following topics:
Key Points:
    - Creating tuples: `my_tuple = (1, 2, 3)`
    - Indexing: `my_tuple[0]`
    - Slicing: `my_tuple[1:3]`
    - Concatenation: `combined_tuple = tuple1 + tuple2`
    - Repetition: `repeated_tuple = my_tuple * 2`
    - Membership: `3 in my_tuple`
    - Length: `len(my_tuple)`
    - Count: `my_tuple.count(2)`
    - Index: `my_tuple.index(3)`
    - Unpacking: `a, b, c = my_tuple`
    - Returning Multiple Values: `return min(numbers), max(numbers)`
    - Tuple Comprehension: `my_generated_tuple = tuple(x * 2 for x in range(100) if x % 2 == 0)`
    - Named Tuples: `Person = namedtuple("Person", ['name', 'age', 'city'])`
    - Converting a list to a tuple: `tuple([1, 2, 3])`
    - Converting a string to a tuple: `tuple("Hello")`
    - Using generator expressions to create tuples

Examples:
    - Creating tuples
    - Accessing elements using indexing and slicing
    - Combining tuples using concatenation
    - Repeating tuples
    - Checking membership of elements in a tuple
    - Getting the length of a tuple
    - Counting occurrences of an element in a tuple
    - Finding the index of an element in a tuple
    - Unpacking tuples into variables
    - Returning multiple values from a function using a tuple
    - Creating tuples using generator expressions
    - Using named tuples for better readability
    - Converting lists and strings to tuples

Usage:
    Run the module to see the output of various tuple operations and methods.
"""
# Syntax
# Tuples are defined using parentheses () and can contain any number of elements, separated by commas.

# Creating tuples
empty_tuple = ()
single_element_tuple = (1,)
my_tuple = (1, 2, 3, 4, 5)

a, b, c, d, e = my_tuple

print(a, b, c, d, e)

heterogeneous_tuple = (1, "apple", 3.14, True)
try:
    heterogeneous_tuple[0] = 2
    print(heterogeneous_tuple)
except TypeError as e:
    print(f"Error: {e}")

a, b, c, d = heterogeneous_tuple

colors = "red", "green", "blue"  # Parentheses are optional when defining a tuple
number = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(type(colors))
print(f"type(number) : {type(number)}")
print(f"type(colors) : {type(colors)}")
num = 1,
print(f"type(num) : {type(num)}")
strn = "hello",
print(f"type(str) : {type(strn)}")

my_list = [1, 2, 3, 4, 5] # list[]
my_sety = {1, 2, 3, 4, 5} # set{}

# Tuple Methods and Operations
'''
Common Tuple Methods and Operations
    Indexing: Access elements by their index.
    Slicing: Access a range of elements.
    Concatenation: Combine two or more tuples.
    Repetition: Repeat the elements of a tuple.
    Membership: Check if an element is in a tuple.
    Length: Get the number of elements in a tuple.
    Count: Count the occurrences of a specific element.
    Index: Find the index of the first occurrence of a specific element.
    Unpacking: Assign elements of a tuple to multiple variables.
    Returning Multiple Values: Return multiple values from a function using a tuple.
'''
# Creating tuples
my_tuple = (1, 2, 3, 4, 5)

# 1. Indexing
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3


# 2. Slicing
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)
print(my_tuple[:3])   # Output: (1, 2, 3)
print(my_tuple[3::])  # Output: (4, 5)


# 3. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6) new tuple

# 4. Repetition
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# 5. Membership
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)   # Output: True
print(6 in my_tuple)   # Output: False
print(6 not in my_tuple)  # Output: True


# 6. Length
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5

# 7. Count
my_tuple = (1, 2, 3, 2, 4, 2, 5)
print(my_tuple.count(2))  # Output: 3

# 8. Index
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2


# 9. Unpacking
my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# 10. Returning Multiple Values
def min_max(numbers):
    return min(numbers), max(numbers)

my_tuple = (1, 2, 3, 4, 5)
min_value, max_value = min_max(my_tuple)
print(min_value, max_value)  # Output: 1 5

# Tuple Comprehension
# Tuple comprehension is not directly supported in Python. However, you can use a generator expression to create a tuple.
# Creating a tuple using a generator expression
my_generated_tuple = tuple(x * 2 for x in range(100) if x % 2 == 0)
print(my_generated_tuple)


# Named Tuple
# A named tuple is a tuple with named fields. It is similar to a struct in C or a record in Pascal.
# Named tuples are defined using the namedtuple() function from the collections module.
# Creating a named tuple syntax: namedtuple("name", [field1, field2, ...])

# Syntax: namedtuple("name", [field1, field2, ...])
from collections import namedtuple

Person = namedtuple("Person", ['name', 'age','city'])
# print(f"person_tuple : {person_tuple}")

p = Person( 1, 25, 3)
print(p.name)
print(p.age)
print(p.city)

# car = namedtuple("Car", ['make', 'model', 'year'])
car = namedtuple("Car", ['make', 'model', 'year']) # namedtuple creation  namedtuple("", ['', '', ''])
c = car("Toyota", "Corolla", 2021) # instance creation
print(c.make)
print(c.model)
print(c.year)


employee = namedtuple("employee",['id', 'name', 'salary'])
emp1 = employee(1, "John", 1000)
print(emp1.id)
print(emp1.name)
print(emp1.salary)



print(heterogeneous_tuple.__add__((1, 2, 3, 4, 5))) # Output: (1, 'apple', 3.14, True, 1, 2, 3, 4, 5) new tuple


number = tuple(x for x in range(20)) 
print(f"number: {number}")

print(tuple(x for x in range(20) if x % 2 == 0))
print(tuple(x for x in range(20) if x % 2 == 1))
print(tuple(x * 3 for x in range(20) if x % 2 == 0))
print(list(x * 3 for x in range(20) if x % 2 == 0))
print(set(x * 3 for x in range(20) if x % 2 == 0))

print(tuple(x**2 for x in range (6) if x % 2 == 1))


# # Converting a list to a tuple
list_to_tuple = tuple([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(list_to_tuple[::])
print(list_to_tuple[3:8])
print(list_to_tuple[5:-2]) #
print(list_to_tuple[::-1]) # reverse the tuple
print(list_to_tuple[:])

print(tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Converting a string to a tuple
string_to_tuple = tuple("Hello World, from Python!")

# Unpacking a tuple
x, y, z = (
    1,
    2,
    3,
)  # Tuple unpacking is used to assign multiple values to multiple variables in a single statement.

# Common Methods and Operations
# Tuples support various methods and operations, although they are limited compared to lists due to their immutability.

first, second, middle, *rest = (
    my_tuple  # The *rest syntax is used to assign multiple values to a single variable.
)
print(first, second, middle, rest)

point = (3, 5)
x, y = (
    point  # Tuple unpacking is used to assign multiple values to multiple variables in a single statement.
)
print(f"x coordinate : {x}, y coordinate: {y}")

# Creating a tuple using a generator expression
my_generated_tupletwo = tuple(x * 2 for x in range(100) if x % 2 == 0)
print(f"my_generated_tuple : {my_generated_tupletwo}")

# comprehension syntax : (expression for item in iterable if condition)
# Creating a tuple using a generator expression
my_generated_tuplethree = tuple(x * 3 for x in range(100) if x % 2 == 1)

number = tuple(x * 4 for x in range(20))


# Creating a generator object (not a tuple)
my_generated_tuplethree = (x * 3 for x in range(100) if x % 2 == 1)
print(
    f"my_generated_tuple2 : {my_generated_tuplethree}"
)  # Output: my_generated_tuple2 : <generator object <genexpr> at 0x7f8b1c3b3d60>

my_generated_tuple3 = tuple(x * 3 for x in range(100) if x % 2 == 1)
print(f"my_generated_tuple : {my_generated_tuple3}")

my_generated_tuple2 = (x * 3 for x in range(100) if x % 2 == 1)
print(
    f"my_generated_tuple2 : {my_generated_tuple2}"
)  # Output: my_generated_tuple2 : <generator object <genexpr> at 0x7f8b1c3b3d60>

# Indexing: Access elements by index
first_element = my_tuple[0]
last_element = my_tuple[-1]

# Slicing: Extract a subset of the tuple
sub_tuple = my_tuple[1:4]  # (2, 3, 4)
reversed_tuple = my_tuple[::-1]  # (5, 4, 3, 2, 1)
sliced_with_step_tuple = my_tuple[1:4:2]  # (2, 4)

# Concatenation: Combine tuples using the + operator
combined_tuple = my_tuple + heterogeneous_tuple

# Repetition: Repeat tuples using the * operator
repeated_tuple = my_tuple * 2

# Membership: Check if an element is in the tuple using in and not in operators
is_in_tuple = 3 in my_tuple
is_not_in_tuple = 6 not in my_tuple

# Length: Get the number of elements in a tuple
tuple_length = len(my_tuple)

# Count occurrences: Count the number of occurrences of an element in a tuple
count_of_1 = my_tuple.count(1)

# Find index: Get the index of the first occurrence of an element in a tuple
index_of_3 = my_tuple.index(3)

# Unpacking
a, b, c, d, e = my_tuple


# Returning multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)


min_value, max_value = min_max(my_tuple)


if __name__ == "__main__":
    print(f"empty_tuple: {empty_tuple}")
    print(f"single_element_tuple: {single_element_tuple}")
    print(f"my_tuple: {my_tuple}")
    print(f"heterogeneous_tuple: {heterogeneous_tuple}")
    print(f"list_to_tuple: {list_to_tuple}")
    print(f"string_to_tuple: {string_to_tuple}")
    print(f"first_element: {first_element}")
    print(f"last_element: {last_element}")
    print(f"sub_tuple: {sub_tuple}")
    print(f"combined_tuple: {combined_tuple}")
    print(f"repeated_tuple: {repeated_tuple}")
    print(f"is_in_tuple: {is_in_tuple}")
    print(f"is_not_in_tuple: {is_not_in_tuple}")
    print(f"tuple_length: {tuple_length}")
    print(f"count_of_1: {count_of_1}")
    print(f"index_of_3: {index_of_3}")
    print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}")
    print(f"min_value: {min_value}, max_value: {max_value}")
