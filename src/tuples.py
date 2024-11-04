# tuples.py
# Syntax
# Tuples are defined using parentheses () and can contain any number of elements, separated by commas.

# Creating tuples
empty_tuple = ()
single_element_tuple = (1,)
my_tuple = (1, 2, 3, 4, 5)
heterogeneous_tuple = (1, "apple", 3.14, True)

# Converting a list to a tuple
list_to_tuple = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

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

# Creating a generator object (not a tuple)
my_generated_tuplethree = (x * 3 for x in range(100) if x % 2 == 1)
print(f"my_generated_tuple2 : {my_generated_tuplethree}")  # Output: my_generated_tuple2 : <generator object <genexpr> at 0x7f8b1c3b3d60>

my_generated_tuple3 = tuple(
    x * 3 for x in range(100) if x % 2 == 1
)  
print(f"my_generated_tuple : {my_generated_tuple3}")

my_generated_tuple2 = (x * 3 for x in range(100) if x % 2 == 1)
print(f"my_generated_tuple2 : {my_generated_tuple2}") # Output: my_generated_tuple2 : <generator object <genexpr> at 0x7f8b1c3b3d60>

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
