# src/loops.py


# while loop
# The while loop executes a block of code as long as the specified condition is true.
i = 1
while i < 8:
    print(f"i: {i}")
    i += 1  # Increment the value of i by 1 in each iteration.

# The break statement is used to exit the loop.
i = 1
while i < 10:
    print(f"i: {i}")
    if i == 3:
        break  # Exit the loop when i is equal to 3.
    i += 1

# The continue statement is used to skip the current iteration and continue with the next iteration.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip the iteration when i is equal to 3.
    print(f"i: {i}")

# The else block is executed when the condition in the while loop becomes false.
i = 1
while i < 5:
    print(f"i: {i}")
    i += 1
else:
    print("i is no longer less than 5.")


# loop examples
# The range() function generates a sequence of numbers from the start value to the end value.
for number in range(1, 6):
    print(f"number: {number}")  # Output: 1 2 3 4 5

# The range() function can also take a step argument to generate numbers with a specific step value.
for number in range(1, 10, 2):
    print(f"number: {number}")  # Output: 1 3 5 7 9

# The range() function can also generate numbers in descending order.
for number in range(5, 0, -1):
    print(f"number: {number}")  # Output: 5 4 3 2 1

# The for loop can also iterate over a list of items.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"fruit: {fruit}")  # Output: apple banana cherry

# The for loop can also iterate over a tuple of items.
fruits = ("apple", "banana", "cherry", "mango", "orange")
for fruit in fruits:
    print(f"fruit: {fruit}")  # Output: apple banana cherry mango orange

# The for loop can also iterate over a string.
for letter in "Ahmet":
    print(f"letter: {letter}")  # Output: A h m e t

# The for loop can also iterate over a dictionary.
person = {"name": "Ahmet", "age": 21, "city": "Istanbul"}
for key, value in person.items():
    print(f"{key}: {value}")  # Output: name Ahmet age 21 city Istanbul

# The for loop can also iterate over a set.
fruits = {"apple", "banana", "cherry", "mango", "orange"}
for fruit in fruits:
    print(f"fruit: {fruit}")  # Output: apple banana cherry mango orange


### Example 1: Flattening a List of Lists
# Suppose you have a list of lists of numbers and you want to flatten it into a single list of numbers.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
import numpy as np

np.flaten = nested_list
print(np.flaten)

nested2_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
flattened2_list = [i for sublist in nested2_list for i in sublist if i >5 and not i % 2 ==0]
print(flattened2_list)

### Example 2: Filtering and Flattening a List of Lists
# Suppose you have a list of lists of numbers and you want to flatten it into a single list of even numbers.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = [num for sublist in nested_list for num in sublist if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8]


### Example 3: Extracting Specific Elements from a List of Dictionaries
# Suppose you have a list of dictionaries representing students and their grades, 
# and you want to extract the names of students who scored above 80.
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 90}
]
high_scorers = [student["name"] for student in students if student["grade"] > 80]
print(high_scorers)  # Output: ['Alice', 'Charlie']


### Example 4: Combining Two Lists with a Condition
# Suppose you have two lists of numbers and 
# you want to create a list of tuples containing pairs of numbers where the sum is even.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
even_sum_pairs = [(x, y) for x in list1 for y in list2 if (x + y) % 2 == 0]
print(even_sum_pairs)  # Output: [(1, 5), (2, 4), (3, 5)]


### Example 5: Creating a List of Tuples from a Dictionary
# Suppose you have a dictionary of items and their prices and 
# you want to create a list of tuples containing the items and their prices where the price is above 10.
items = {
    "apple": 5,
    "banana": 12,
    "cherry": 15,
    "date": 8
}
expensive_items = [(item, price) for item, price in items.items() if price > 10]
print(expensive_items)  # Output: [('banana', 12), ('cherry', 15)]


"""
Comprehensions and generators are related concepts in Python, but they serve different purposes and have distinct characteristics. Here's a clear comparison:

### Comprehensions

1. **Definition**:
   - Comprehensions are a concise way to create collections such as lists, sets, and dictionaries.

2. **Types**:
   - **List Comprehensions**: Create lists.
   - **Set Comprehensions**: Create sets.
   - **Dictionary Comprehensions**: Create dictionaries.

3. **Syntax**:
   - List Comprehension: `[expression for item in iterable if condition]`
   - Set Comprehension: `{expression for item in iterable if condition}`
   - Dictionary Comprehension: `{key: value for item in iterable if condition}`

4. **Example**:
   - List Comprehension: `[x**2 for x in range(10)]` creates a list of squares.

### Generators

1. **Definition**:
   - Generators are a way to create iterators that generate values on-the-fly and do not store the entire sequence in memory.

2. **Types**:
   - **Generator Functions**: Use the `yield` keyword to produce values one at a time.
   - **Generator Expressions**: Similar to comprehensions but use parentheses and generate values lazily.

3. **Syntax**:
   - Generator Expression: `(expression for item in iterable if condition)`

4. **Example**:
   - Generator Expression: `(x**2 for x in range(10))` creates a generator that yields squares.

### Key Differences

1. **Memory Usage**:
   - Comprehensions create collections that are stored in memory.
   - Generators produce values one at a time and do not store the entire sequence in memory.

2. **Evaluation**:
   - Comprehensions evaluate and store all elements immediately.
   - Generators evaluate elements lazily, generating them as needed.

### Summary

- **Comprehensions**: A concise way to create collections like lists, sets, and dictionaries.
- **Generators**: A way to create iterators that generate values on-the-fly, using less memory.

Both comprehensions and generators are powerful tools in Python, each with its own use cases and advantages.

"""




# while loop
# The while loop executes a block of code as long as the specified condition is true.
i = 1
while i < 8:
    print(f"i: {i}")
    i += 1  # Increment the value of i by 1 in each iteration.


# The break statement is used to exit the loop.
i = 1
while i < 10:
    print(f"i: {i}")
    if i == 3:
        break  # Exit the loop when i is equal to 3.
    i += 1


# The continue statement is used to skip the current iteration and continue with the next iteration.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip the iteration when i is equal to 3.
    print(f"i: {i}")

# The else block is executed when the condition in the while loop becomes false.
i = 1
while i < 5:
    print(f"i: {i}")
    i += 1
else:
    print("i is no longer less than 5.")

# Nested loops
# You can use one or more loops inside another loop.
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# The pass statement is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute.
for i in range(5):
    pass  # Do nothing.


# The pass statement is also used for empty functions.
def my_function():
    pass  # Do nothing.


# The pass statement is also used for empty loops.
for i in range(5):
    pass  # Do nothing.

# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
fruits = ["apple", "banana", "cherry", "mango", "orange"]
for index, fruit in enumerate(fruits):
    print(f"index: {index}, fruit: {fruit}")

# The zip() function returns an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator is paired together, etc.
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]
for fruit, color in zip(fruits, colors):
    print(f"fruit: {fruit}, color: {color}")

# The reversed() function returns an iterator that accesses the given sequence in the reverse order.
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(f"fruit: {fruit}")

# The sorted() function returns a new sorted list from the elements of any iterable.
fruits = ["apple", "banana", "cherry"]
for fruit in sorted(fruits):
    print(f"fruit: {fruit}")

# The sorted() function can also take a reverse argument to sort the list in descending order.
fruits = ["apple", "banana", "cherry"]
for fruit in sorted(fruits, reverse=True):
    print(f"fruit: {fruit}")

# The sorted() function can also take a key argument to specify a function to be called on each list element before making comparisons.
fruits = ["apple", "strawberry", "banana", "cherry"]
for fruit in sorted(fruits, key=len):
    print(f"fruit: {fruit}")

# do-while loop
# Python does not have a built-in do-while loop, but you can create one using a while loop.
i = 0
while True:
    print(f"i: {i}")
    i += 1
    if i == 5:
        break

count = 10
while count > 0:
    print(f"count: {count}")
    count -= 1
else:
    print("Count is no longer greater than 0.")

# loop control statements
# The break statement is used to exit the loop.
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is equal to 3.
    print(f"i: {i}")

# The continue statement is used to skip the current iteration and continue with the next iteration.
for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i is equal to 3.
    print(f"i: {i}")


def range_sequence(start, end, step=1):
    """
    Generates a sequence of numbers from start to end with a specific step value.
    """
    return list(range(start, end, step))


def iterate_list(items):
    """
    Iterates over a list of items.
    """
    return [item for item in items]


def iterate_string(string):
    """
    Iterates over a string.
    """
    return [char for char in string]


def iterate_dict(dictionary):
    """
    Iterates over a dictionary's key-value pairs.
    """
    return [(key, value) for key, value in dictionary.items()]


def while_loop_example(limit):
    """
    Executes a block of code as long as the specified condition is true.
    """
    result = []
    i = 1
    while i < limit:
        result.append(i)
        i += 1
    return result


def while_loop_with_break(limit):
    """
    Uses the break statement to exit the loop when a condition is met.
    """
    result = []
    i = 1
    while i < limit:
        result.append(i)
        if i == 3:
            break
        i += 1
    return result


def while_loop_with_continue(limit):
    """
    Uses the continue statement to skip the current iteration and continue with the next iteration.
    """
    result = []
    i = 0
    while i < limit:
        i += 1
        if i == 3:
            continue
        result.append(i)
    return result


def while_loop_with_else(limit):
    """
    Executes the else block when the condition in the while loop becomes false.
    """
    result = []
    i = 1
    while i < limit:
        result.append(i)
        i += 1
    else:
        result.append("i is no longer less than {}".format(limit))
    return result


def nested_loops(outer, inner):
    """
    Uses nested loops to iterate over a range of numbers.
    """
    result = []
    for i in range(outer):
        for j in range(inner):
            result.append((i, j))
    return result


def enumerate_example(items):
    """
    Uses the enumerate() function to add a counter to an iterable.
    """
    return [(index, item) for index, item in enumerate(items)]


def zip_example(list1, list2):
    """
    Uses the zip() function to return an iterator of tuples.
    """
    return [(item1, item2) for item1, item2 in zip(list1, list2)]


def reversed_example(items):
    """
    Uses the reversed() function to access the given sequence in reverse order.
    """
    return [item for item in reversed(items)]


def sorted_example(items, reverse=False, key=None):
    """
    Uses the sorted() function to return a new sorted list from the elements of any iterable.
    """
    return sorted(items, reverse=reverse, key=key)


def do_while_example(limit):
    """
    Simulates a do-while loop using a while loop.
    """
    result = []
    i = 0
    while True:
        result.append(i)
        i += 1
        if i == limit:
            break
    return result


def while_loop_with_else_example(start):
    """
    Uses a while loop with an else block.
    """
    result = []
    count = start
    while count > 0:
        result.append(count)
        count -= 1
    else:
        result.append("Count is no longer greater than 0.")
    return result


if __name__ == "__main__":
    # Example usage of the functions
    print(f"range_sequence(1, 6): {range_sequence(1, 6)}")
    print(
        f"iterate_list(['apple', 'banana', 'cherry']): {iterate_list(['apple', 'banana', 'cherry'])}"
    )
    print(f"iterate_string('Ahmet'): {iterate_string('Ahmet')}")
    print(
        f"iterate_dict({{'name': 'Ahmet', 'age': 21, 'city': 'Istanbul'}}): {iterate_dict({'name': 'Ahmet', 'age': 21, 'city': 'Istanbul'})}"
    )
    print(f"while_loop_example(8): {while_loop_example(8)}")
    print(f"while_loop_with_break(10): {while_loop_with_break(10)}")
    print(f"while_loop_with_continue(5): {while_loop_with_continue(5)}")
    print(f"while_loop_with_else(5): {while_loop_with_else(5)}")
    print(f"nested_loops(3, 2): {nested_loops(3, 2)}")
    print(
        f"enumerate_example(['apple', 'banana', 'cherry']): {enumerate_example(['apple', 'banana', 'cherry'])}"
    )
    print(
        f"zip_example(['apple', 'banana', 'cherry'], ['red', 'yellow', 'pink']): {zip_example(['apple', 'banana', 'cherry'], ['red', 'yellow', 'pink'])}"
    )
    print(
        f"reversed_example(['apple', 'banana', 'cherry']): {reversed_example(['apple', 'banana', 'cherry'])}"
    )
    print(
        f"sorted_example(['apple', 'banana', 'cherry']): {sorted_example(['apple', 'banana', 'cherry'])}"
    )
    print(
        f"sorted_example(['apple', 'banana', 'cherry'], reverse=True): {sorted_example(['apple', 'banana', 'cherry'], reverse=True)}"
    )
    print(
        f"sorted_example(['apple', 'strawberry', 'banana', 'cherry'], key=len): {sorted_example(['apple', 'strawberry', 'banana', 'cherry'], key=len)}"
    )
    print(f"do_while_example(5): {do_while_example(5)}")
    print(f"while_loop_with_else_example(10): {while_loop_with_else_example(10)}")

    # The range() function generates a sequence of numbers from the start value to the end value.
    for number in range(1, 6):
        print(f"number: {number}")  # Output: 1 2 3 4 5

    # The range() function can also take a step argument to generate numbers with a specific step value.
    for number in range(1, 10, 2):
        print(f"number: {number}")  # Output: 1 3 5 7 9

    # The range() function can also generate numbers in descending order.
    for number in range(5, 0, -1):
        print(f"number: {number}")  # Output: 5 4 3 2 1

    # The for loop can also iterate over a list of items.
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"fruit: {fruit}")  # Output: apple banana cherry

    # The for loop can also iterate over a tuple of items.
    fruits = ("apple", "banana", "cherry", "mango", "orange")
    for fruit in fruits:
        print(f"fruit: {fruit}")  # Output: apple banana cherry mango orange

    # The for loop can also iterate over a string.
    for letter in "Ahmet":
        print(f"letter: {letter}")  # Output: A h m e t

    # The for loop can also iterate over a dictionary.
    person = {"name": "Ahmet", "age": 21, "city": "Istanbul"}
    for key, value in person.items():
        print(f"{key}: {value}")  # Output: name Ahmet age 21 city Istanbul

    # The for loop can also iterate over a set.
    fruits = {"apple", "banana", "cherry", "mango", "orange"}
    for fruit in fruits:
        print(f"fruit: {fruit}")  # Output: apple banana cherry mango orange

    # while loop
    # The while loop executes a block of code as long as the specified condition is true.
    i = 1
    while i < 8:
        print(f"i: {i}")
        i += 1  # Increment the value of i by 1 in each iteration.
    # Output: 1 2 3 4 5 6 7

    # The break statement is used to exit the loop.
    i = 1
    while i < 10:
        print(f"i: {i}")
        if i == 3:
            break  # Exit the loop when i is equal to 3.
        i += 1
    # Output: 1 2 3

    # The continue statement is used to skip the current iteration and continue with the next iteration.
    i = 0
    while i < 5:
        i += 1
        if i == 3:
            continue  # Skip the iteration when i is equal to 3.
        print(f"i: {i}")
    # Output: 1 2 4 5

    # The else block is executed when the condition in the while loop becomes false.
    i = 1
    while i < 5:
        print(f"i: {i}")
        i += 1
    else:
        print("i is no longer less than 5.")
    # Output: 1 2 3 4 i is no longer less than 5.

    # Nested loops
    # You can use one or more loops inside another loop.
    for i in range(3):
        for j in range(2):
            print(f"i: {i}, j: {j}")
    # Output: 0 0 0 1 1 0 1 1 2 0 2 1

    # The pass statement is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute.
    for i in range(5):
        pass  # Do nothing.

    # The pass statement is also used for empty functions.
    def my_function():
        pass  # Do nothing.

    # The pass statement is also used for empty loops.
    for i in range(5):
        pass  # Do nothing.

    # The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
    fruits = ["apple", "banana", "cherry", "mango", "orange"]
    for index, fruit in enumerate(fruits):
        print(f"index: {index}, fruit: {fruit}")
    # Output: 0 apple 1 banana 2 cherry 3 mango 4 orange

    # The zip() function returns an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator is paired together, etc.
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "pink"]
    for fruit, color in zip(fruits, colors):
        print(f"fruit: {fruit}, color: {color}")
    # Output: apple red banana yellow cherry pink

    # The reversed() function returns an iterator that accesses the given sequence in the reverse order.
    fruits = ["apple", "banana", "cherry"]
    for fruit in reversed(fruits):
        print(f"fruit: {fruit}")
    # Output: cherry banana apple

    # The sorted() function returns a new sorted list from the elements of any iterable.
    fruits = ["apple", "banana", "cherry"]
    for fruit in sorted(fruits):
        print(f"fruit: {fruit}")
    # Output: apple banana cherry

    # The sorted() function can also take a reverse argument to sort the list in descending order.
    fruits = ["apple", "banana", "cherry"]
    for fruit in sorted(fruits, reverse=True):
        print(f"fruit: {fruit}")
    # Output: cherry banana apple

    # The sorted() function can also take a key argument to specify a function to be called on each list element before making comparisons.
    fruits = ["apple", "strawberry", "banana", "cherry"]
    for fruit in sorted(fruits, key=len):
        print(f"fruit: {fruit}")
    # Output: apple cherry banana strawberry

    # do-while loop
    # Python does not have a built-in do-while loop, but you can create one using a while loop.
    i = 0
    while True:
        print(f"i: {i}")
        i += 1
        if i == 5:
            break
    # Output: 0 1 2 3 4

    count = 10
    while count > 0:
        print(f"count: {count}")
        count -= 1
    else:
        print("Count is no longer greater than 0.")
    # Output: 10 9 8 7 6 5 4 3 2 1 Count is no longer greater than 0.

    # loop control statements
    # The break statement is used to exit the loop.
    for i in range(5):
        if i == 3:
            break  # Exit the loop when i is equal to 3.
        print(f"i: {i}")
    # Output: 0 1 2

    # The continue statement is used to skip the current iteration and continue with the next iteration.
    for i in range(5):
        if i == 3:
            continue  # Skip the iteration when i is equal to 3.
        print(f"i: {i}")
    # Output: 0 1 2 4

    # The pass statement is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute.
    for i in range(5):
        pass  # Do nothing.

    # The else block is executed when the condition in the loop becomes false.
    for i in range(5):
        print(f"i: {i}")
    else:
        print("i is no longer less than 5.")
    # Output: 0 1 2 3 4 i is no longer less than 5.



# You can use one or more loops inside another loop.
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# The pass statement is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute.
for i in range(5):
    pass  # Do nothing.

# The pass statement is also used for empty functions.
def my_function():
    pass  # Do nothing.

# The pass statement is also used for empty loops.
for i in range(5):
    pass  # Do nothing.

# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
fruits = ["apple", "banana", "cherry", "mango", "orange"]
for index, fruit in enumerate(fruits):
    print(f"index: {index}, fruit: {fruit}")
    
# The zip() function returns an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator is paired together, etc.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for item1, item2 in zip(list1, list2):
    print(f"item1: {item1}, item2: {item2}")
    
