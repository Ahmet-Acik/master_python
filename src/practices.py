# fibinacci series
a, b = 0, 1
while b < 100:
    print(b, end=", ")
    a, b = b, a + b
    
print()

# Fibonacci series using for loop
a, b = 0, 1
for i in range(10):
    print(b, end=", ")
    a, b = b, a + b
    
print() 

# Fibonacci series using for loop
a, b = 0, 1
for i in range(10):
    print(b, end=", ")
    a, b = b, a + b
print()


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_tuple = tuple(fibonacci(10))
print(fibonacci_tuple)  # Output: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

# How do you create a tuple of uppercase versions of strings from a list?
strings = ["apple", "banana", "cherry"]
uppercase_tuple = tuple(s.upper() for s in strings)
print(uppercase_tuple)  # Output: ('APPLE', 'BANANA', 'CHERRY')

# How do you create a tuple of (number, square) pairs for numbers from 1 to 8?
squared_tuple = tuple((n, n ** 2) for n in range(1, 9))
print(squared_tuple)  # Output: ((1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64))

# How do you create a tuple of numbers from a list of strings?
strings = ["1", "2", "3", "4", "5"]
numbers_tuple = tuple(int(s) for s in strings)
print(numbers_tuple)  # Output: (1, 2, 3, 4, 5)

# How do you generate a tuple of prime numbers less than 20?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_tuple = tuple(n for n in range(20) if is_prime(n))
print(primes_tuple)  # Output: (2, 3, 5, 7, 11, 13, 17, 19)


# How do you generate a tuple of reversed strings from a list?
strings = ["apple", "banana", "cherry"]
reversed_tuple = tuple(s[::-1] for s in strings)
print(reversed_tuple)  # Output: ('elppa', 'ananab', 'yrrehc')

# How do you create a tuple of squares of numbers divisible by 3 between 1 and 30?
squares_divisible_by_3 = tuple(x**2 for x in range(1, 31) if x % 3 == 0)
print(squares_divisible_by_3)  # Output: (9, 36, 81, 144, 225, 324, 441, 576, 729)

# How do you create a tuple of the lengths of words in a sentence?
sentence = "Python is a powerful programming language"
word_lengths = tuple(len(word) for word in sentence.split())
print(word_lengths)  # Output: (6, 2, 1, 8, 11, 8)

# How do you generate a tuple of all ASCII values of characters in a string?
text = "Hello"
ascii_tuple = tuple(ord(char) for char in text)
print(ascii_tuple)  # Output: (72, 101, 108, 108, 111)

# How do you create a tuple of numbers and their binary representations from 1 to 5?
binary_representation = tuple((x, bin(x)) for x in range(1, 6))
print(binary_representation)  # Output: ((1, '0b1'), (2, '0b10'), (3, '0b11'), (4, '0b100'), (5, '0b101'))


def add(x, y):
    return x + y


def fibonacci2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def greet(name:str, age:int):
    print(f"Hello,{name}, you are {age} years old!")
    
greet(23,"Ahmet")

greet(age=23, name="Ahmet")


print('hello world, end of the page')