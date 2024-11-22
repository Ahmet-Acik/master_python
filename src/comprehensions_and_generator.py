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

"""
**Comprehension Syntax**:
   - List Comprehension: `[expression for item in iterable if condition]`
   - Set Comprehension: `{expression for item in iterable if condition}`
   - Dictionary Comprehension: `{key: value for item in iterable if condition}`

** Generator Syntax**:
   - Generator Expression: `(expression for item in iterable if condition)`
"""

# list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# set comprehension
squares_set = {x ** 2 for x in range(10)}
print(squares_set)  # output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# dictionary comprehension
squares_dict = {x: x ** 2 for x in range(10)}
print(squares_dict)  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# generator expression
squares_gen = (x ** 2 for x in range(10))
print(squares_gen)  # output: <generator object <genexpr> at 0x7f7f4c5d6c10>

print(list(squares_gen))  # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares_gen = (x ** 2 for x in range(10))
print(set(squares_gen))  # output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
squares_gen = (x ** 2 for x in range(10))
print(tuple(squares_gen))  # output: (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

squares_gen_to_dict = ((x, x ** 2) for x in range(10))
print(squares_gen_to_dict)  # output: <generator object <genexpr> at 0x7f7f4c5d6c10>
print(dict(squares_gen_to_dict))  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}