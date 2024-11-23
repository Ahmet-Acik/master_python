# Source:   
"""
    This module demonstrates various common exception types in Python and how to handle them using try-except blocks.
    Exception types covered:
    1. ZeroDivisionError: Raised when attempting to divide by zero.
    2. AttributeError: Raised when accessing a non-existent attribute of an object.
    3. IndexError: Raised when accessing an element in a list with an invalid index.
    4. KeyError: Raised when accessing a non-existent key in a dictionary.
    5. NameError: Raised when using a variable that has not been defined.
    6. TypeError: Raised when performing an operation on incompatible types.
    7. ValueError: Raised when passing an argument of the correct type but inappropriate value.
    8. FileNotFoundError: Raised when trying to open a non-existent file.
    9. IOError: Raised when performing an I/O operation (e.g., reading or writing a file) that fails.
    10. ImportError: Raised when importing a non-existent module.
    11. RuntimeError: Raised when an error is detected that doesn't fall into any of the other categories.
    12. StopIteration: Raised to signal the end of an iteration.
    13. SyntaxError: Raised when the parser encounters a syntax error.
    14. IndentationError: Raised when there is incorrect indentation.
    15. MemoryError: Raised when an operation runs out of memory.
    Each exception type is demonstrated with a specific scenario and handled using a try-except block.
"""
try:
    10/0
except ZeroDivisionError as e:
    print(e)

try:
    user_input = int(input("Enter a number: "), 10)
    result = 10/user_input
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("No exception occurred.")
finally:
    print("This will be executed no matter what.")
    
# Common exception types in Python:

### 1. `AttributeError`

# **Scenario**: Accessing a non-existent attribute of an object.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Car("Toyota", "Camry")
try:
    print(car.year)  # 'year' attribute does not exist
except AttributeError as e:
    print(f"AttributeError: {e}")


### 2. `IndexError`

# **Scenario**: Accessing an element in a list with an invalid index.

fruits = ["apple", "banana", "cherry"]
try:
    print(fruits[3])  # Index 3 does not exist
except IndexError as e:
    print(f"IndexError: {e}")


### 3. `KeyError`

# **Scenario**: Accessing a non-existent key in a dictionary.

person = {"name": "Alice", "age": 30}
try:
    print(person["address"])  # 'address' key does not exist
except KeyError as e:
    print(f"KeyError: {e}")


### 4. `NameError`

# **Scenario**: Using a variable that has not been defined.

try:
    print(age)  # 'age' is not defined
except NameError as e:
    print(f"NameError: {e}")


### 5. `TypeError`

# **Scenario**: Adding a string to an integer.

try:
    result = "Hello" + 5  # Cannot add string and integer
except TypeError as e:
    print(f"TypeError: {e}")


### 6. `ValueError`

# **Scenario**: Passing a string to a function that expects an integer.

try:
    number = int("abc")  # Cannot convert 'abc' to an integer
except ValueError as e:
    print(f"ValueError: {e}")


### 7. `ZeroDivisionError`

# **Scenario**: Dividing a number by zero.

try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")


### 8. `FileNotFoundError`

# **Scenario**: Trying to open a non-existent file.

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")


### 9. `IOError`

# **Scenario**: Reading from a file that is not open.

try:
    file = open("example.txt", "r")
    file.close()
    content = file.read()  # File is already closed
except IOError as e:
    print(f"IOError: {e}")


### 10. `ImportError`

# **Scenario**: Importing a non-existent module.

try:
    import non_existent_module  # Module does not exist
except ImportError as e:
    print(f"ImportError: {e}")


### 11. `RuntimeError`

# **Scenario**: Raising a generic runtime error.

try:
    raise RuntimeError("This is a runtime error")
except RuntimeError as e:
    print(f"RuntimeError: {e}")


### 12. `StopIteration`

# **Scenario**: Manually raising a `StopIteration` exception in an iterator.

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            raise StopIteration

iterator = MyIterator(3)
try:
    while True:
        print(next(iterator))
except StopIteration as e:
    print("Iteration stopped")


### 13. `SyntaxError`

# **Scenario**: Writing invalid Python code.

# This code will raise a SyntaxError when executed
# try:
#     eval("x === 3")  # Invalid syntax
# except SyntaxError as e:
#     print(f"SyntaxError: {e}")


### 14. `IndentationError`

# **Scenario**: Incorrectly indenting code blocks.

# This code will raise an IndentationError when executed
# try:
    # def my_function():
    # print("Hello")  # Incorrect indentation
# except IndentationError as e:
    # print(f"IndentationError: {e}")


### 15. `MemoryError`

# **Scenario**: Creating a very large list that exceeds the available memory.

# try:
#     large_list = [1] * (10**10)  # Attempt to create a very large list
# except MemoryError as e:
#     print(f"MemoryError: {e}")



