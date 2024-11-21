# # sets.py
"""
This module demonstrates the usage of sets in Python. Sets are unordered collections of unique elements.
They do not allow duplicates and support various methods for adding, removing, and manipulating elements.

Functions and examples included:
- Creating sets: empty set, set with elements, heterogeneous set
- Set methods: add, copy, remove, discard, pop, clear
- Converting lists and tuples to sets
- Set operations: union, intersection, difference, symmetric difference, subset, superset, disjoint
- Frozen sets: immutable sets with no add, remove, discard, pop, clear operations

Examples:
- Adding elements to a set
- Removing elements from a set
- Discarding elements from a set
- Popping elements from a set
- Clearing a set
- Performing set operations (union, intersection, difference, symmetric difference)
- Checking subset, superset, and disjoint status
- Handling AttributeError for frozenset operations

Note:
- Sets are defined using curly braces {} or the set() constructor.
- An empty set must be created using set(), not {}.
- Tuples are allowed as elements in a set, but lists are not (unhashable type).
"""

my_set = {1, 2, 3, 4, 5}
my_empty_set = {}
print(my_empty_set)
print(my_set)
print(type(my_set))

# Sets are unordered, unindexed, and do not allow duplicates
# Set Methods - add, copy, remove, discard, pop, clear
my_set.add(6)
print(f"my_set after adding 6: {my_set}")  # output: {1, 2, 3, 4, 5, 6}
my_set.copy()
print(f"my_set after copying: {my_set}")  # output: {1, 2, 3, 4, 5, 6}
my_set.discard(
    3
)  # Removes the specified element from the set - Does not raise an error if the element is not found
print(f"my_set after discarding 3: {my_set}")  # output: {1, 2, 4, 5, 6}
my_set.remove(4)
print(f"my_set after removing 4: {my_set}")  # output: {1, 2, 5, 6}
my_set.pop()
print(f"my_set after popping: {my_set}")  # output: {2, 5, 6}
my_set.clear()
print(f"my_set after clearing: {my_set}")  # output: set()


my_mixed_set = {
    2,
    "Hello",
    3.14,
    True,
    (1, 2, 3),
}  # output: {2, 3.14, 'Hello', (1, 2, 3), True} tuples are allowed in sets
print(my_mixed_set)

my_list_to_set = set([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10])  # Duplicates are removed
print(my_list_to_set)  # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

my_tuple_to_set = set(
    (1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 8, 9, 10)
)  # Duplicates are removed

my_tuple_to_set2 = {(1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 8, 9, 10)}

""" 
# output: {(1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 8, 9, 10)} 
The tuple itself contains duplicate values, but since it is a single element in the set, 
the set will not remove duplicates within the tuple.
"""


print(my_tuple_to_set2)  # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

emails = [
    "abc@gmail.com",
    "def@gmail.com",
    "ghf@gmail.com",
    "abc@gmail.com",
    "xyz@gmail.com",
]
emails_set = set(emails)
print(emails_set)  #

list(set(emails))  # Removes duplicates from the list

# Creating sets
empty_set = set()  # Empty set, with set constructor, not {}. {} is for empty dictionary
my_set = {1, 2, 3, 4, 5}
heterogeneous_set = {1, "Python", 3.14, True}

my_fruits_set = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print(f"my_fruits_set: {my_fruits_set}")

list_to_set = set(
    ["apple", "banana", "cherry", "apple", "orange", "kiwi", "melon", "orange", "mango"]
)  # Duplicates are removed
print(f"list_to_set: {list_to_set}")

tuple_to_set = set((1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 0, 0))  # Duplicates are removed
print(f"tuple_to_set: {tuple_to_set}")

string_to_set = set("hello Python")  # Duplicates are removed
print(f"string_to_set: {string_to_set}")

valid_set = {1, "hello", 3, 4, (5, 6), 7, 8, 9, 10}  # Tuples are allowed
print(f"valid_set: {valid_set}")

try:
    invalid_set = {
        1,
        "Python",
        3,
        4,
        5,
        [6, 7, 8, 9, 10],
        10,
    }  # TypeError: unhashable type: 'list'
    print(f"invalid_set: {invalid_set}")
except TypeError as e:
    print(f"invalid_set: {e}")

# Set Methods - add, remove, discard, pop, clear

# Adding elements - Adds the specified element to the set
my_set2 = {0, 2, 3, 4, 5}
my_set2.ad(3.5) # bool, int, float, str, tuple, frozenset
my_set2.ad(1) # bool, int, float, str, tuple, frozenset
my_set2.ad("hello") # bool, int, float, str, tuple, frozenset
my_set2.ad(True)
my_set2.ad((1,2,3)) # bool, int, float, str, tuple, frozenset
my_set2.ad(frozenset([1,2,3])) # bool, int, float, str, tuple, frozenset
print(f"my_set after adding 3.5, 1, hello, True, (1,2,3), frozenset([1,2,3]): {my_set2}")


# Adding itreables to the set - update method - add multiple elements to the set
my_set2.update((6,7,8,9,10))  
my_set2.update([6,7,8,9,10])
my_set2.update({6,7,8,9,10}, [11, 12, 13], (14, 15, 16)) # add multiple itearables to the set
print(f"my_set after adding 6_10: {my_set2}")


# Adding elements - Adds the specified element to the set
my_fruits_set.add("strawberry")
print(f"my_fruits_set after adding strawberry: {my_fruits_set}")
my_set.add(6)
print(f"my_set after adding 6: {my_set}")

# Removing elements - Removes the specified element from the set - Raises KeyError if the element is not found
my_fruits_set.remove("banana")
print(f"my_fruits_set after removing banana: {my_fruits_set}")
my_set.remove(6)
print(f"my_set after removing 6: {my_set}")

# Discard elements - Removes the specified element from the set - Does not raise an error if the element is not found
my_fruits_set.discard("kiwi")
print(f"my_fruits_set after discarding kiwi: {my_fruits_set}")
my_set.discard(6)
print(f"my_set after discarding 6: {my_set}")

# Pop elements - Removes and returns an arbitrary element from the set - Raises KeyError if the set is empty
my_fruit = my_fruits_set.pop()
print(f"my_fruit after popping: {my_fruit}")  # Output: my_fruit after popping: mango
print(
    f"my_fruits_set after popping: {my_fruits_set}"
)  # Output: my_fruits_set after popping: {'apple', 'cherry', 'orange', 'melon', 'strawberry'}

# Clear elements - Empty the set
my_fruits_set.clear()
print(f"my_fruits_set after clearing: {my_fruits_set}")

# Set Operations - Union, Intersection, Difference, Symmetric Difference, Subset, Superset, Disjoint

# Union - All unique elements from both sets > set1 | set2
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2) # set1 | set2
print(f"union_set: {union_set}")

# Intersection - unique elements that are common in both sets > set1 & set2
intersection_set = set1.intersection(set2) # set1 & set2
print(f"intersection_set: {intersection_set}")

# Difference - unique Elements that are in set1 but not in set2 or vice versa > set1 - set2
difference_set = set1.difference(set2) # set1 - set2
print(f"difference_set: {difference_set}")

# Symmetric Difference - Elements that are in one set but not in both sets (Union - Intersection) > set1 ^ set2
symmetric_difference_set = set1.symmetric_difference(set2) # set1 ^ set2
print(f"symmetric_difference_set: {symmetric_difference_set}")

# Subset - Returns True if all elements of the set are present in the specified set
subset = set1.issubset(set2)
print(f"subset: {subset}")

# Superset - Returns True if all elements of the set are present in the specified set
superset = set1.issuperset(set2)
print(f"superset: {superset}")

# Disjoint - No common elements between sets - Returns True if no common elements
disjoint = set1.isdisjoint(set2)
print(f"disjoint: {disjoint}")

# Frozen Sets - Immutable Sets (Read-only) - No add, remove, discard, pop, clear operations
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"frozen_set: {frozen_set}")

# Handling AttributeError for frozenset operations
try:
    frozen_set.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
except AttributeError as e:
    print(f"Error: {e}")

try:
    frozen_set.remove(3)  # AttributeError: 'frozenset' object has no attribute 'remove'
except AttributeError as e:
    print(f"Error: {e}")

try:
    frozen_set.discard(
        3
    )  # AttributeError: 'frozenset' object has no attribute 'discard'
except AttributeError as e:
    print(f"Error: {e}")

try:
    frozen_set.pop()  # AttributeError: 'frozenset' object has no attribute 'pop'
except AttributeError as e:
    print(f"Error: {e}")

try:
    frozen_set.clear()  # AttributeError: 'frozenset' object has no attribute 'clear'
except AttributeError as e:
    print(f"Error: {e}")

# Handling AttributeError for frozenset operations
try:
    frozen_set.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
    frozen_set.remove(3)  # AttributeError: 'frozenset' object has no attribute 'remove'
    frozen_set.discard(
        3
    )  # AttributeError: 'frozenset' object has no attribute 'discard'
    frozen_set.pop()  # AttributeError: 'frozenset' object has no attribute 'pop'
    frozen_set.clear()  # AttributeError: 'frozenset' object has no attribute 'clear'
except AttributeError as e:
    print(f"Error: {e}")
