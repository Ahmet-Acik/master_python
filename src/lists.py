my_empty_list = []

shopping_list = ["apple", "banana", "cherry"]
todo_list = ["learn Python", "practice coding", "build projects"]

fruits = ["apple", "banana", "cherry", "mango", "orange"]
colors = ["red", "yellow", "pink"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.5, True]

# list() function creates a list from an iterable with range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
number_list = list(range(1, 6))  # [1, 2, 3, 4, 5]
print(f"number_list: {number_list}")  # Output: [1, 2, 3, 4, 5]

# list() function creates a list from an iterable.
letters_list = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
print(f"letters_list: {letters_list}")

# nested list or list of lists or 2D list or 2-dimensional list or matrix or 2D array
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"nested_list: {nested_list}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# indexing starts from 0 and negative indexing starts from -1
print(f"shopping_list[0]: {shopping_list[0]}")  # apple
print(f"shopping_list[-1]: {shopping_list[-1]}")  # cherry


# slicing
print(f"shopping_list[1:3]: {shopping_list[1:3]}")  # ['banana', 'cherry']
print(f"shopping_list[:2]: {shopping_list[:2]}")  # ['apple', 'banana']
print(f"shopping_list[1:]: {shopping_list[1:]}")  # ['banana', 'cherry']
print(f"shopping_list[:]: {shopping_list[:]}")  # ['apple', 'banana', 'cherry']

# list concatenation
fruits_colors = fruits + colors
print(f"fruits_colors: {fruits_colors}")  # ['apple', 'banana', 'cherry', 'mango', 'orange', 'red', 'yellow', 'pink']

# list repetition
repeated_fruits = fruits * 2
print(f"repeated_fruits: {repeated_fruits}")  # ['apple', 'banana', 'cherry', 'mango', 'orange', 'apple', 'banana', 'cherry', 'mango', 'orange']

# append() method adds an element to the end of the list.
shopping_list.append("date")
print(f"shopping_list after append: {shopping_list}")  # ['apple', 'banana', 'cherry', 'date']

# insert() method adds an element at the specified index.
shopping_list.insert(1, "grape")
print(f"shopping_list after insert: {shopping_list}")  # ['apple', 'grape', 'banana', 'cherry', 'date']

# extend() method adds elements of an iterable to the end of the list.
shopping_list.extend(["kiwi", "mango"])
print(f"shopping_list after extend: {shopping_list}")  # ['apple', 'grape', 'banana', 'cherry', 'date', 'kiwi', 'mango']

# remove() method removes the first occurrence of the specified element.
shopping_list.remove("grape")
print(f"shopping_list after remove: {shopping_list}")  # ['apple', 'banana', 'cherry', 'date', 'kiwi', 'mango']

# pop() method removes the element at the specified index, and returns it.
popped_item = shopping_list.pop(1)
print(f"popped_item: {popped_item}")  # banana
print(f"shopping_list after pop: {shopping_list}")  # ['apple', 'cherry', 'date', 'kiwi', 'mango']

# del keyword removes the element at the specified index.
del shopping_list[1]
print(f"shopping_list after del: {shopping_list}")  # ['apple', 'date', 'kiwi', 'mango']

# clear() method removes all the elements from the list.
shopping_list.clear()
print(f"shopping_list after clear: {shopping_list}")  # []

shopping_list.extend(["apple", "grape", "banana", "cherry", "date", "kiwi", "mango"])
print(f"shopping_list after extend: {shopping_list}")  # ['apple', 'grape', 'banana', 'cherry', 'date', 'kiwi', 'mango']

# reverse() method reverses the order of the list.
shopping_list.reverse()
print(f"shopping_list after reverse: {shopping_list}")  # ['mango', 'kiwi', 'date', 'cherry', 'banana', 'grape', 'apple']

# count() method returns the number of elements with the specified value.
print(f"fruits.count('apple'): {fruits.count('apple')}")  # 1
# index() method returns the index of the first occurrence of the specified element.
print(f"fruits.index('cherry'): {fruits.index('cherry')}")  # 2

# list comprehension creates a list from an iterable, with an optional condition.
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
