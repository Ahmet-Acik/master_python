'''
List Comprehensions
    A list comprehension is a concise way to create a new list by applying an expression to each element of an iterable.

    Basic Syntax:[expression for item in iterable if condition]
'''
# Examples:

# Generate a list of squares of numbers from 1 to 10:
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filter even numbers from a list:
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# Flatten a 2D list:
matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for row in matrix for item in row]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

# Transform a list of strings to uppercase:
words = ['hello', 'world']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD']

# Create a list of tuples (number, square):
num_square = [(x, x**2) for x in range(1, 6)]
print(num_square)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Extract vowels from a string:
vowels = [char for char in "hello world" if char in "aeiou"]
print(vowels)  # Output: ['e', 'o']


'''
Set Comprehensions
    A set comprehension is similar to a list comprehension but creates a set, ensuring that the result contains unique elements.

    Basic Syntax: {expression for item in iterable if condition}
'''
# Examples:

# Generate a set of squares of numbers from 1 to 10:
squares = {x**2 for x in range(1, 11)}
print(squares)  # Output: {64, 1, 4, 36, 9, 16, 49, 81, 100, 25}

# Remove duplicate words and convert them to lowercase:
words = ['Hello', 'World', 'HELLO', 'world']
unique_words = {word.lower() for word in words}
print(unique_words)  # Output: {'hello', 'world'}

# Create a set of lengths of words in a list:
words = ['apple', 'banana', 'cherry']
lengths = {len(word) for word in words}
print(lengths)  # Output: {5, 6}

# Extract unique characters from a string:
unique_chars = {char for char in "hello world"}
print(unique_chars)  # Output: {' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'}

'''
Dictionary Comprehensions
    A dictionary comprehension is used to create a dictionary by mapping keys to values based on an expression.

    Basic Syntax: {key_expression: value_expression for item in iterable if condition}
'''

# Examples:

# Create a dictionary of numbers and their squares:
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Swap keys and values in a dictionary:
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Create a dictionary of word lengths:
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

# Filter a dictionary by values:
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {key: value for key, value in original.items() if value % 2 == 0}
print(filtered)  # Output: {'b': 2, 'd': 4}

# Create a dictionary of ASCII values for characters in a string:
ascii_map = {char: ord(char) for char in "abc"}
print(ascii_map)  # Output: {'a': 97, 'b': 98, 'c': 99}

# Count occurrences of each word in a list:
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = {word: words.count(word) for word in set(words)}
print(word_count)  # Output: {'cherry': 1, 'banana': 2, 'apple': 3}

'''
Comparison of Comprehensions
Feature	            List Comprehension	         Set Comprehension	         Dictionary Comprehension
Output Type	        List	                     Set (unique elements)	     Dictionary
Usage Example	    [x**2 for x in range(5)]	 {x**2 for x in range(5)}	 {x: x**2 for x in range(5)}
Duplicate Handling	Allows duplicates	         Removes duplicates	         Keys must be unique
Conclusion
Comprehensions are a powerful feature in Python that allow you to create lists, sets, and dictionaries in a concise and expressive way. 
By using comprehensions, you can write more readable and efficient code for common tasks like filtering, transforming, and mapping elements in an iterable.
'''