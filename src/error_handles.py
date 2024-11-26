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
    10 / 0
except ZeroDivisionError as e:
    print(e)

try:
    # user_input = int(input("Enter a number: "), 10)
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
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


# well-implemented logging and exception handling mechanism 
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def process_data(data):
    logging.debug("Processing data: %s", data)
    
    if not data:
        logging.warning("No data provided")
        raise ValueError("Data cannot be empty")
    
    logging.debug("Data processing staterted successfully")

    try:
        if len(data) < 2:
            raise ValueError("Data must contain at least two elements")
        result = data[0] / data[1]
        logging.info("Calculating Result: %s", result)
    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError: %s", e)
    except TypeError as e:
        logging.error("TypeError: %s", e)
    else:
        logging.info("No exception occurred")
    finally:
        logging.info("Data processing complete")

# Example usage
print(f"process_data([10, 5]) : {process_data([10, 5])}")
print(f"process_data([10, 0]) : {process_data([10, 0])}")
print(f"process_data([]) : {process_data([])}")




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


## 13. `SyntaxError`

# **Scenario**: Writing invalid Python code.

# This code will raise a SyntaxError when executed
try:
    eval("x === 3")  # Invalid syntax
except SyntaxError as e:
    print(f"SyntaxError: {e}")


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


import traceback
"""
A stack trace is a report that provides information about the active stack frames at a specific point in time during the execution of a program.
It is typically generated when an exception occurs and helps developers understand the sequence of function calls that led to the error. 
In Python, stack traces are automatically printed to the console when an unhandled exception occurs.

### Example of a Stack Trace

Here is an example of a Python program that generates a stack trace due to an unhandled exception:

```python
def function_a():
    function_b()

def function_b():
    function_c()

def function_c():
    raise ValueError("An error occurred in function_c")

try:
    function_a()
except Exception as e:
    print(f"Exception caught: {e}")
    raise
```

### Output

When you run the above code, you will see a stack trace similar to this:

```
Traceback (most recent call last):
  File "example.py", line 12, in <module>
    function_a()
  File "example.py", line 2, in function_a
    function_b()
  File "example.py", line 5, in function_b
    function_c()
  File "example.py", line 8, in function_c
    raise ValueError("An error occurred in function_c")
ValueError: An error occurred in function_c
```

### Explanation

1. **Traceback**:
   - The `Traceback` section shows the sequence of function calls that led to the exception. 
   Each line in the traceback corresponds to a call frame, starting from the most recent call and going back to the initial call.

2. **File and Line Number**:
   - Each line in the traceback includes the file name and line number where the function call occurred. 
   This helps you locate the exact point in the code where the error happened.

3. **Function Name**:
   - The function name is shown for each call frame, indicating which function was called.

4. **Exception Type and Message**:
   - The last line of the traceback shows the type of exception (`ValueError`) and the error message ("An error occurred in function_c").

### Customizing Stack Traces

You can customize the way stack traces are handled and displayed using the `traceback` module. 
This module provides functions to extract, format, and print stack traces.

### Example: Custom Stack Trace Handling

```python
import traceback

def function_a():
    function_b()

def function_b():
    function_c()

def function_c():
    raise ValueError("An error occurred in function_c")

try:
    function_a()
except Exception as e:
    print("Custom stack trace:")
    traceback.print_exc()
```

### Output

The output will be similar to the default stack trace, 
but you can customize it further if needed:

```
Custom stack trace:
Traceback (most recent call last):
  File "example.py", line 14, in <module>
    function_a()
  File "example.py", line 2, in function_a
    function_b()
  File "example.py", line 5, in function_b
    function_c()
  File "example.py", line 8, in function_c
    raise ValueError("An error occurred in function_c")
ValueError: An error occurred in function_c
```

### Summary

A stack trace provides valuable information about the sequence of function calls that led to an exception. 
It includes the file name, line number, function name, and the exception type and message. 
By understanding and using stack traces, you can effectively debug and diagnose issues in your Python programs. 
The `traceback` module allows you to customize the handling and display of stack traces for more advanced use cases.
"""

def function_a():
    function_b()


def function_b():
    function_c()


def function_c():
    raise ValueError("An error occurred in function_c")


try:
    function_a()
except Exception as e:
    print("Custom stack trace:")
    traceback.print_exc()
