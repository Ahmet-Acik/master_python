# List creation
"""
This module demonstrates various operations and manipulations on lists in Python.

It covers:
- List creation using different methods
- List comprehensions with and without conditions
- Nested list comprehensions
- Applying functions to list elements
- List methods for modification and querying
- List slicing and indexing
- List concatenation and repetition
- Built-in functions for lists (len, min, max, sum, sorted)
- List comprehensions with multiple conditions and nested loops
- String manipulation with list comprehensions
- List modification using slicing
- Using list comprehensions to create matrices
- Utility functions to get specific items from a list
- Utility functions to get sublists with different slicing techniques
- Utility functions to generate sequences and iterate through lists

Functions:
- square(x): Returns the square of x.
- classify(x): Classifies x as even or odd.
- get_first_item(items): Returns the first item in the list.
- get_last_item(items): Returns the last item in the list.
- get_second_item(items): Returns the second item in the list.
- get_penultimate_item(items): Returns the penultimate item in the list.
- get_items(items, start, end): Returns a sublist from start to end.
- get_items_from_start(items, end): Returns a sublist from the start to end.
- get_items_to_end(items, start): Returns a sublist from start to the end.
- get_items_with_step(items, start, end, step): Returns a sublist from start to end with a step.
- get_items_with_negative_step(items, start, end): Returns a sublist from start to end with a negative step.
- get_items_with_negative_start(items, start, end): Returns a sublist from a negative start to end.
- get_items_with_negative_end(items, start, end): Returns a sublist from start to a negative end.
- get_items_with_negative_start_and_end(items, start, end): Returns a sublist from a negative start to a negative end.
- get_items_reversed(items): Returns the reversed list.
- get_items_reversed_with_step(items, step): Returns the reversed list with a step.
- get_items_reversed_with_negative_step(items, step): Returns the list with a negative step.
- get_items_reversed_with_negative_start(items, start): Returns the list with a negative start.
- range_sequence(start, stop, step=1): Returns a list of numbers from start to stop with a step.
- iterate_list(items): Returns a list of items by iterating through the input list.
"""

empty_list = []
print(f"empty_list: {empty_list}")
grocery_list = ["milk", "bread", "eggs"]
print(f"grocery_list: {grocery_list}")

# list creation with list() function
number_list = list(range(1, 6))
print(f"number_list: {number_list}")
letters_list = list("Python")
letters_list.append("s")
print(f"letters_list: {letters_list}")
print(f"letters_list: {letters_list}")
nested_list = list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"nested_list: {nested_list}")
# list creation from tuple and set
tuple_list = list(("P", "y", "t", "h", "o", "n"))
print(f"tuple_list: {tuple_list}")
set_list = list({"apple", "banana", "cherry"})
print(f"set_list: {set_list}")

# Create list with List comprehension 
# Create a list of squares
squares = [x**2 for x in range(10)]
print(f"Create a list of squares ; {squares}")

# List Comprehension with Condition
# Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Create a list of even numbers : {evens}")

odds = [x for x in range(10) if x % 2 != 0]
print(f"Create a list of odd numbers : {odds}")

# Nested List Comprehension
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flatten a 2D list : {flattened}")
import pdb
# Set a breakpoint
pdb.set_trace()

matrix =[[ j for j in range(1,4)] for i in range(1,4)] 
print(f"matrix : {matrix}")

matrix2 = [[i*j for j in range(1,5)] for i in range(1,5)]
print(f"matrix2 : {matrix2}")

# Apply a function to each element
def square(x):
    return x**2

squares = [square(x) for x in range(10)]
print(f"Apply a function to each element : {squares}")

# List Comprehension with Multiple Conditions
# Create a list of numbers divisible by both 2 and 3
divisible_by_2_and_3 = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
print(f"Create a list of numbers divisible by both 2 and 3 : {divisible_by_2_and_3}")

# List Comprehension with Nested Loops
# Create a list of tuples (x, y) where x is from 0-2 and y is from 0-2
tuples = [(x, y) for x in range(3) for y in range(3)]
print(f"Create a list of tuples (x, y) where x is from 0-2 and y is from 0-2 : {tuples}")

# List Comprehension with String Manipulation
# Create a list of characters from a string
string = "Python"
chars = [char for char in string]
print(f"Create a list of characters from a string : {chars}")


# List Comprehension with if-else
# Classify numbers as even or odd
def classify(x):
    return f"even {x}" if x % 2 == 0 else f"odd {x}"

classification = [classify(x) for x in range(10)]
print(f"List Comprehension with if-else : {classification}") 


# List methods
grocery_list.append("butter")
print(f"grocery_list append('butter' :){grocery_list}")
grocery_list.insert(1, "cheese")
print(f"grocery_list insert(1, 'cheese'): {grocery_list}")
grocery_list.extend(["yogurt", "juice"])
print(f"grocery_list extend(['yogurt', 'juice']): {grocery_list}")
grocery_list.remove("cheese")
print(f"grocery_list remove('cheese'): {grocery_list}")
popped_item = grocery_list.pop(1)
print(f"grocery_list pop(1): {grocery_list}")
grocery_list.clear()
print(f"grocery_list clear(): {grocery_list}")

# List operations
fruit_list = ["apple", "banana", "cherry"]
color_list = ["red", "yellow", "pink"]
fruit_color_list = fruit_list + color_list
print(f"fruit_color_list: {fruit_color_list}")
repeated_fruit_list = fruit_list * 2
print(f"repeated_fruit_list: {repeated_fruit_list}")

# List slicing
print(f"fruit_list[1:3]: {fruit_list[1:3]}")
print(f"fruit_list[:2]: {fruit_list[:2]}")
print(f"fruit_list[1:]: {fruit_list[1:]}")
print(f"fruit_list[:]: {fruit_list[:]}")
print(f"fruit_list[::2]: {fruit_list[::2]}")
print(f"fruit_list[::-1]: {fruit_list[::-1]}")

# List comprehensions
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]  # [1, 3, 5, 7, 9]

# Print results
print(f"grocery_list: {grocery_list}")
print(f"popped_item: {popped_item}")
print(f"fruit_color_list: {fruit_color_list}")
print(f"repeated_fruit_list: {repeated_fruit_list}")
print(f"squares: {squares}")
print(f"even_numbers: {even_numbers}")
print(f"odd_numbers: {odd_numbers}")


my_empty_list = []

shopping_list = ["apple", "banana", "cherry"]
todo_list = ["learn Python", "practice coding", "build projects"]

fruits = ["apple", "banana", "cherry", "mango", "orange"]
colors = ["red", "yellow", "pink"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.5, True]

# list() function creates a list from an iterable with range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
number_list = list(range(1, 6))  # [1, 2, 3, 4, 5]
number_list2 = list(range(0, 6, 2))  # [0, 2, 4]

print(f"number_list: {number_list}")  # Output: [1, 2, 3, 4, 5]
print(f"number_list2: {number_list2}")  # Output: [0, 2, 4]

# list() function creates a list from an iterable.
letters_list = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n'] # string
letters_list2 = list(
    ("P", "y", "t", "h", "o", "n")
)  # ['P', 'y', 't', 'h', 'o', 'n'] # tuple
print(f"letters_list: {letters_list}")
print(f"letters_list2: {letters_list2}")

# nested list or list of lists or 2D list or 2-dimensional list or matrix or 2D array
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(f"nested_list: {nested_list}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(
    f"nested_list2: {nested_list2}"
)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# indexing starts from 0 and negative indexing starts from -1
print(f"shopping_list[0]: {shopping_list[0]}")  # apple
print(f"shopping_list[-1]: {shopping_list[-1]}")  # cherry

# access elements
print(f"shopping_list: {shopping_list}")  # ['apple', 'banana', 'cherry']
print(f"shopping_list[1]: {shopping_list[1]}")  # banana
print(f"shopping_list[2]: {shopping_list[2]}")  # cherry
print(f"shopping_list[-1]: {shopping_list[-1]}")  # cherry
print(f"shopping_list[-2]: {shopping_list[-2]}")  # banana


# slicing returns a new list with the specified range of elements, start index is included, end index is excluded.
print(f"shopping_list[1:3]: {shopping_list[1:3]}")  # ['banana', 'cherry']
print(f"shopping_list[:2]: {shopping_list[:2]}")  # ['apple', 'banana']
print(f"shopping_list[1:]: {shopping_list[1:]}")  # ['banana', 'cherry']
print(f"shopping_list[:]: {shopping_list[:]}")  # ['apple', 'banana', 'cherry']
print(f"shopping_list[1:3:2]: {shopping_list[1:3:2]}")  # ['banana']
print(f"shopping_list[::2]: {shopping_list[::2]}")  # ['apple', 'cherry']
print(f"shopping_list[::-1]: {shopping_list[::-1]}")  # ['cherry', 'banana', 'apple']

# list modification
new_fruit_list = ["mango", "orange", "grape", "kiwi"]
print(
    f"new_fruit_list before modification: {new_fruit_list}"
)  # ['mango', 'orange', 'grape', 'kiwi']
new_fruit_list[1] = "strawberry"
print(
    f"new_fruit_list after modification: {new_fruit_list}"
)  # ['mango', 'strawberry', 'grape', 'kiwi']

# list modification with slicing
new_fruit_list[1:3] = [
    "blueberry",
    "blackberry",
]  # ['mango', 'blueberry', 'blackberry', 'kiwi']
print(
    f"new_fruit_list after modification with slicing: {new_fruit_list}"
)  # ['mango', 'blueberry', 'blackberry', 'kiwi']

new_numbers_list = [1, 2, 3, 4, 5]
print(f"new_numbers_list before modification: {new_numbers_list}")  # [1, 2, 3, 4, 5]
new_numbers_list[2:4] = [6, 7, 8]  # [1, 2, 6, 7, 8, 5]
print(
    f"new_numbers_list after modification with slicing: {new_numbers_list}"
)  # [1, 2, 6, 7, 8, 5]

new_letters_list = ["P", "y", "t", "h", "o", "n"]
print(
    f"new_letters_list before modification: {new_letters_list}"
)  # ['P', 'y', 't', 'h', 'o', 'n']
new_letters_list[2:5] = ["Y", "T"]  # ['P', 'y', 'Y', 'T', 'n']
print(
    f"new_letters_list after modification with slicing: {new_letters_list}"
)  # ['P', 'y', 'Y', 'T', 'n']

# list modification with slicing and step
new_numbers_list = [1, 2, 3, 4, 5, 6]
new_numbers_list[::2] = [10, 20, 30]  # [10, 2, 20, 4, 30, 6]
print(
    f"new_numbers_list after modification with slicing and step: {new_numbers_list}"
)  # [10, 2, 20, 4, 30, 6]

# list modification with negative step
new_numbers_list[::-1] = [60, 50, 40, 30, 20, 10]  # [10, 20, 30, 40, 50, 60]
print(
    f"new_numbers_list after modification with negative step: {new_numbers_list}"
)  # [10, 20, 30, 40, 50, 60]

# list concatenation, + operator combines two lists, and returns a new list.
fruits = ["apple", "banana", "cherry", "mango", "orange"]
colors = ["red", "yellow", "pink"]
fruits_colors = fruits + colors
print(
    f"fruits_colors: {fruits_colors}"
)  # ['apple', 'banana', 'cherry', 'mango', 'orange', 'red', 'yellow', 'pink']

# list repetition * operator repeats a list, and returns a new list, here fruits list is repeated 2 times.
repeated_fruits = fruits * 2
print(
    f"repeated_fruits: {repeated_fruits}"
)  # ['apple', 'banana', 'cherry', 'mango', 'orange', 'apple', 'banana', 'cherry', 'mango', 'orange']

# len() function returns the number of elements in the list.
print(f"len(fruits): {len(fruits)}")  # 5

# in operator checks if an element is present in the list, returns True or False.
print(f"'apple' in fruits: {'apple' in fruits}")  # True
print(f"'kiwi' in fruits: {'kiwi' in fruits}")  # False

# not in operator checks if an element is not present in the list, returns True or False.
print(f"'apple' not in fruits: {'apple' not in fruits}")  # False
print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")  # True

# min() function returns the smallest element in the list.
print(f"min(numbers): {min(numbers)}")  # 1

# max() function returns the largest element in the list.
print(f"max(numbers): {max(numbers)}")  # 5

# sum() function returns the sum of all elements in the list.
print(f"sum(numbers): {sum(numbers)}")  # 15

# sorted() function returns a new sorted list from the elements of the list.
sorted_numbers = sorted(numbers)
print(f"sorted_numbers: {sorted_numbers}")  # [1, 2, 3, 4, 5]

# sort() method sorts the elements of the list, it modifies the original list.
numbers.sort()
print(f"numbers after sort: {numbers}")  # [1, 2, 3, 4, 5]


# copy() method returns a shallow copy of the list.
fruits_copy = fruits.copy()
print(f"fruits_copy: {fruits_copy}")  # ['apple', 'banana', 'cherry', 'mango', 'orange']


# append() method adds an element to the end of the list, it modifies the original list.
shopping_list.append("date")
print(
    f"shopping_list after append: {shopping_list}"
)  # ['apple', 'banana', 'cherry', 'date']

# insert() method adds an element at the specified index, it modifies the original list.
shopping_list.insert(1, "grape")
print(
    f"shopping_list after insert: {shopping_list}"
)  # ['apple', 'grape', 'banana', 'cherry', 'date']

# extend() method adds elements of an iterable to the end of the list, it modifies the original list.
shopping_list.extend(["kiwi", "mango"])
print(
    f"shopping_list after extend: {shopping_list}"
)  # ['apple', 'grape', 'banana', 'cherry', 'date', 'kiwi', 'mango']

# remove() method removes the first occurrence of the specified element, it modifies the original list.
shopping_list.remove("grape")
print(
    f"shopping_list after remove: {shopping_list}"
)  # ['apple', 'banana', 'cherry', 'date', 'kiwi', 'mango']

# pop() method removes the element at the specified index, and returns it, it modifies the original list.
popped_item = shopping_list.pop(1)
print(f"popped_item: {popped_item}")  # banana
print(
    f"shopping_list after pop: {shopping_list}"
)  # ['apple', 'cherry', 'date', 'kiwi', 'mango']

# del keyword removes the element at the specified index, it modifies the original list.
del shopping_list[1]
print(f"shopping_list after del: {shopping_list}")  # ['apple', 'date', 'kiwi', 'mango']

# clear() method removes all the elements from the list, it modifies the original list.
shopping_list.clear()
print(f"shopping_list after clear: {shopping_list}")  # []

shopping_list.extend(["apple", "grape", "banana", "cherry", "date", "kiwi", "mango"])
print(
    f"shopping_list after extend: {shopping_list}"
)  # ['apple', 'grape', 'banana', 'cherry', 'date', 'kiwi', 'mango']

# reverse() method reverses the order of the list, it modifies the original list.
shopping_list.reverse()
print(
    f"shopping_list after reverse: {shopping_list}"
)  # ['mango', 'kiwi', 'date', 'cherry', 'banana', 'grape', 'apple']

# count() method returns the number of elements with the specified value in the list.
print(f"fruits.count('apple'): {fruits.count('apple')}")  # 1
# index() method returns the index of the first occurrence of the specified element.
print(f"fruits.index('cherry'): {fruits.index('cherry')}")  # 2

# list comprehension creates a list from an iterable, with an optional condition to filter the elements.
squares = [x**2 for x in range(1, 6)]
print(f"squares: {squares}")  # [1, 4, 9, 16, 25]

# list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"even_numbers: {even_numbers}")  # [2, 4, 6, 8, 10]

# list comprehension
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(f"odd_numbers: {odd_numbers}")  # [1, 3, 5, 7, 9]

# list comprehension
squared_even_numbers = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"squared_even_numbers: {squared_even_numbers}")  # [4, 16, 36, 64, 100]

# list comprehension
squared_odd_numbers = [x**2 for x in range(1, 11) if x % 2 != 0]
print(f"squared_odd_numbers: {squared_odd_numbers}")  # [1, 9, 25, 49, 81]

# list comprehension with nested list
matrix = [[x for x in range(1, 4)] for _ in range(3)]
print(f"matrix: {matrix}")  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def get_first_item(items):
    return items[0]


first_item_tobuy = get_first_item(shopping_list)
print(first_item_tobuy)  # apple


def get_last_item(items):
    return items[-1]


get_last_item_tobuy = get_last_item(shopping_list)
print(get_last_item_tobuy)  # cherry


def get_second_item(items):
    return items[1]


def get_penultimate_item(items):
    return items[-2]


def get_items(items, start, end):
    return items[start:end]

print(get_items(shopping_list,1,3)) # ['grape', 'banana']

def get_items_from_start(items, end):
    return items[:end]


def get_items_to_end(items, start):
    return items[start:]


def get_items_with_step(items, start, end, step):
    return items[start:end:step]


def get_items_with_negative_step(items, start, end):
    return items[start:end:-1]


def get_items_with_negative_start(items, start, end):
    return items[-start:end]


def get_items_with_negative_end(items, start, end):
    return items[start:-end]


def get_items_with_negative_start_and_end(items, start, end):
    return items[-start:-end]


def get_items_reversed(items):
    return items[::-1]


def get_items_reversed_with_step(items, step):
    return items[::-step]


def get_items_reversed_with_negative_step(items, step):
    return items[::step]


def get_items_reversed_with_negative_start(items, start):
    return items[-start:]


def range_sequence(start, stop, step=1):
    return list(range(start, stop, step))


def iterate_list(items):
    return [item for item in items]
