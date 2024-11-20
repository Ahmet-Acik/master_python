# FILE: nested_comprehensions.py
# Example 1: Flattening a list of lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 2: Filtering and flattening a list of lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = [num for sublist in nested_list for num in sublist if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8]

# Example 3: Extracting specific elements from a list of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 90},
]
high_scorers = [student["name"] for student in students if student["grade"] > 80]
print(high_scorers)  # Output: ['Alice', 'Charlie']

# Example 4: Combining two lists with a condition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
even_sum_pairs = [(x, y) for x in list1 for y in list2 if (x + y) % 2 == 0]
print(even_sum_pairs)  # Output: [(1, 5), (2, 4), (3, 5)]

# Example 5: Creating a list of tuples from a dictionary
items = {"apple": 5, "banana": 12, "cherry": 15, "date": 8}
expensive_items = [(item, price) for item, price in items.items() if price > 10]
print(expensive_items)  # Output: [('banana', 12), ('cherry', 15)]

# Example 6: Finding common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = [x for x in list1 for y in list2 if x == y]
print(common_elements)  # Output: [3, 4]

# Example 7: Creating a list of squares of even numbers from a list of lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares_of_even_numbers = [
    num**2 for sublist in nested_list for num in sublist if num % 2 == 0
]
print(squares_of_even_numbers)  # Output: [4, 16, 36, 64]

# Example 8: Extracting values from a list of dictionaries based on a condition
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]
names_of_people_older_than_30 = [d["name"] for d in data if d["age"] > 30]
print(names_of_people_older_than_30)  # Output: ['Charlie']

# Example 9: Generating a multiplication table
n = 3
multiplication_table = [(i, j, i * j) for i in range(1, n + 1) for j in range(1, n + 1)]
print(
    multiplication_table
)  # Output: [(1, 1, 1), (1, 2, 2), (1, 3, 3), (2, 1, 2), (2, 2, 4), (2, 3, 6), (3, 1, 3), (3, 2, 6), (3, 3, 9)]

# Example 10: Filtering and transforming a list of tuples
n = 3
multiplication_table = [(i, j, i * j) for i in range(1, n + 1) for j in range(1, n + 1)]
print(
    multiplication_table
)  # Output: [(1, 1, 1), (1, 2, 2), (1, 3, 3), (2, 1, 2), (2, 2, 4), (2, 3, 6), (3, 1, 3), (3, 2, 6), (3, 3, 9)]

# Example 11: Extracting Nested Dictionary Values
nested_dict = {
    "group1": {"name": "Alice", "age": 25},
    "group2": {"name": "Bob", "age": 30},
    "group3": {"name": "Charlie", "age": 35},
}
names = [info["name"] for group, info in nested_dict.items()]
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

# Example 12: Filtering Nested Lists Based on Condition
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered_numbers = [num for sublist in nested_list for num in sublist if num > 5]
print(filtered_numbers)  # Output: [6, 7, 8, 9]

### Example 13: Extracting Specific Keys from a List of Dictionaries
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]
names_and_cities = [(d["name"], d["city"]) for d in data]
print(
    names_and_cities
)  # Output: [('Alice', 'New York'), ('Bob', 'Los Angeles'), ('Charlie', 'Chicago')]


### Example 14: Filtering and Flattening Nested Lists of Strings
nested_list = [["apple", "banana"], ["cherry", "date"], ["fig", "grape"]]
filtered_fruits = [
    fruit for sublist in nested_list for fruit in sublist if len(fruit) > 5
]
print(filtered_fruits)  # Output: ['banana', 'cherry']


### Example 15: Creating a List of Indices of Even Numbers in Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_indices = [
    (i, j)
    for i, sublist in enumerate(nested_list)
    for j, num in enumerate(sublist)
    if num % 2 == 0
]
print(even_indices)  # Output: [(0, 1), (1, 0), (1, 2), (2, 1)]


### Example 16: Extracting Values from Nested Dictionaries Based on a Condition
nested_dict = {
    "group1": {"name": "Alice", "age": 25},
    "group2": {"name": "Bob", "age": 30},
    "group3": {"name": "Charlie", "age": 35},
}
names_older_than_30 = [
    info["name"] for group, info in nested_dict.items() if info["age"] > 30
]
print(names_older_than_30)  # Output: ['Charlie']


### Example 17: Filtering and Transforming Nested Lists of Tuples
nested_tuples = [[(1, 2), (3, 4)], [(5, 6), (7, 8)], [(9, 10), (11, 12)]]
filtered_transformed = [
    (x * 2, y * 2) for sublist in nested_tuples for x, y in sublist if x % 2 != 0
]
print(filtered_transformed)  # Output: [(2, 4), (10, 12), (18, 20)]


### Example 18: Extracting and Flattening Nested Lists of Dictionaries
nested_list_of_dicts = [
    [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}],
    [{"name": "Charlie", "age": 35}, {"name": "David", "age": 40}],
]
names = [d["name"] for sublist in nested_list_of_dicts for d in sublist]
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'David']


### Example 19: Filtering Nested Lists of Lists Based on Sum
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered_sublists = [sublist for sublist in nested_list if sum(sublist) > 15]
print(filtered_sublists)  # Output: [[7, 8, 9]]


### Example 20: Creating a List of Pairs from Two Lists with a Condition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
pairs_with_sum_greater_than_7 = [(x, y) for x in list1 for y in list2 if x + y > 7]
print(pairs_with_sum_greater_than_7)  # Output: [(2, 6), (3, 5), (3, 6)]


# Example 1: Flattening a list of lists
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


# Example 2: Filtering and flattening a list of lists
def flatten_and_filter_even_numbers(nested_list):
    return [num for sublist in nested_list for num in sublist if num % 2 == 0]


# Example 3: Extracting specific elements from a list of dictionaries
def extract_high_scorers(students):
    return [student["name"] for student in students if student["grade"] > 80]


# Example 4: Combining two lists with a condition
def find_even_sum_pairs(list1, list2):
    return [(x, y) for x in list1 for y in list2 if (x + y) % 2 == 0]


# Example 5: Creating a list of tuples from a dictionary
def find_expensive_items(items):
    return [(item, price) for item, price in items.items() if price > 10]


# Example 6: Finding common elements in two lists
def find_common_elements(list1, list2):
    return [x for x in list1 for y in list2 if x == y]


# Example 7: Creating a list of squares of even numbers from a list of lists
def squares_of_even_numbers(nested_list):
    return [num**2 for sublist in nested_list for num in sublist if num % 2 == 0]


# Example 8: Extracting values from a list of dictionaries based on a condition
def extract_values_by_condition(data, key, condition):
    return [d[key] for d in data if condition(d)]


# Example 9: Generating a multiplication table
def multiplication_table(n):
    return [(i, j, i * j) for i in range(1, n + 1) for j in range(1, n + 1)]


# Example 10: Filtering and transforming a list of tuples
def filter_and_transform_tuples(nested_tuples):
    """
    Filter and transform nested tuples.

    :param nested_tuples: List of lists of tuples.
    :return: List of transformed tuples where the first element is odd.
    """
    return [
        (x * 2, y * 2)
        for sublist in nested_tuples
        if isinstance(sublist, list)
        for x, y in sublist
        if isinstance((x, y), tuple) and x % 2 != 0
    ]


# FILE: loops_nested_comprehensions.py


# Example 11: Extracting Nested Dictionary Values
def extract_names(nested_dict):
    return [info["name"] for group, info in nested_dict.items()]


# Example 12: Filtering Nested Lists Based on Condition
def filter_numbers(nested_list):
    return [num for sublist in nested_list for num in sublist if num > 5]


# Example 13: Extracting Specific Keys from a List of Dictionaries
def extract_names_and_cities(data):
    return [(d["name"], d["city"]) for d in data]


# Example 14: Filtering and Flattening Nested Lists of Strings
def filter_fruits(nested_list):
    return [fruit for sublist in nested_list for fruit in sublist if len(fruit) > 5]


# Example 15: Creating a List of Indices of Even Numbers in Nested Lists
def find_even_indices(nested_list):
    return [
        (i, j)
        for i, sublist in enumerate(nested_list)
        for j, num in enumerate(sublist)
        if num % 2 == 0
    ]


# Example 16: Extracting Values from Nested Dictionaries Based on a Condition
def extract_names_older_than_30(nested_dict):
    return [info["name"] for group, info in nested_dict.items() if info["age"] > 30]


# Example 17: Filtering and Transforming Nested Lists of Tuples
def filter_and_transform_tuples(nested_tuples):
    return [
        (x * 2, y * 2) for sublist in nested_tuples for x, y in sublist if x % 2 != 0
    ]


# Example 18: Extracting and Flattening Nested Lists of Dictionaries
def extract_names_from_nested_dicts(nested_list_of_dicts):
    return [d["name"] for sublist in nested_list_of_dicts for d in sublist]


# Example 19: Filtering Nested Lists of Lists Based on Sum
def filter_sublists_by_sum(nested_list):
    return [sublist for sublist in nested_list if sum(sublist) > 15]


# Example 20: Creating a List of Pairs from Two Lists with a Condition
def find_pairs_with_sum_greater_than_7(list1, list2):
    return [(x, y) for x in list1 for y in list2 if x + y > 7]


# Example usage
if __name__ == "__main__":
    # Example 1
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Flattened list:", flatten_list(nested_list))

    # Example 2
    print(
        "Flattened and filtered even numbers:",
        flatten_and_filter_even_numbers(nested_list),
    )

    # Example 3
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 75},
        {"name": "Charlie", "grade": 90},
    ]
    print("High scorers:", extract_high_scorers(students))

    # Example 4
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("Even sum pairs:", find_even_sum_pairs(list1, list2))

    # Example 5
    items = {"apple": 5, "banana": 12, "cherry": 15, "date": 8}
    print("Expensive items:", find_expensive_items(items))

    # Example 6
    list3 = [1, 2, 3, 4]
    list4 = [3, 4, 5, 6]
    print("Common elements:", find_common_elements(list3, list4))

    # Example 7
    print("Squares of even numbers:", squares_of_even_numbers(nested_list))

    # Example 8
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35},
    ]
    print(
        "Names of people older than 30:",
        extract_values_by_condition(data, "name", lambda d: d["age"] > 30),
    )

    # Example 9
    print("Multiplication table for 3:", multiplication_table(3))

    # Example 10
    nested_tuples = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    print(
        "Filtered and transformed tuples:", filter_and_transform_tuples(nested_tuples)
    )

    # Main method to call the functions
    # Example 11
    nested_dict = {
        "group1": {"name": "Alice", "age": 25},
        "group2": {"name": "Bob", "age": 30},
        "group3": {"name": "Charlie", "age": 35},
    }
    print("Names:", extract_names(nested_dict))  # Output: ['Alice', 'Bob', 'Charlie']

    # Example 12
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Filtered numbers:", filter_numbers(nested_list))  # Output: [6, 7, 8, 9]

    # Example 13
    data = [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
    ]
    print(
        "Names and cities:", extract_names_and_cities(data)
    )  # Output: [('Alice', 'New York'), ('Bob', 'Los Angeles'), ('Charlie', 'Chicago')]

    # Example 14
    nested_list = [["apple", "banana"], ["cherry", "date"], ["fig", "grape"]]
    print(
        "Filtered fruits:", filter_fruits(nested_list)
    )  # Output: ['banana', 'cherry']

    # Example 15
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(
        "Even indices:", find_even_indices(nested_list)
    )  # Output: [(0, 1), (1, 0), (1, 2), (2, 1)]

    # Example 16
    nested_dict = {
        "group1": {"name": "Alice", "age": 25},
        "group2": {"name": "Bob", "age": 30},
        "group3": {"name": "Charlie", "age": 35},
    }
    print(
        "Names older than 30:", extract_names_older_than_30(nested_dict)
    )  # Output: ['Charlie']

    # Example 17
    nested_tuples = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    print(
        "Filtered and transformed tuples:", filter_and_transform_tuples(nested_tuples)
    )

    # Example 18
    nested_list_of_dicts = [
        [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}],
        [{"name": "Charlie", "age": 35}, {"name": "David", "age": 40}],
    ]
    print(
        "Names from nested dicts:",
        extract_names_from_nested_dicts(nested_list_of_dicts),
    )  # Output: ['Alice', 'Bob', 'Charlie', 'David']

    # Example 19
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(
        "Filtered sublists by sum:", filter_sublists_by_sum(nested_list)
    )  # Output: [[7, 8, 9]]

    # Example 20
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(
        "Pairs with sum greater than 7:",
        find_pairs_with_sum_greater_than_7(list1, list2),
    )  # Output: [(2, 6), (3, 5), (3, 6)]
