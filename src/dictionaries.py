# dictionarioes.py
"""
This script covers various aspects of working with dictionaries in Python.
It includes topics such as dictionary creation, methods, and operations including adding, updating,
removing elements, looping, merging dictionaries, dictionary comprehensions, and JSON handling.
Key features:
1. Creating dictionaries using:
    - Curly braces
    - The `dict` constructor with key-value pairs, lists of tuples, etc.
2. Basic dictionary operations including:
    - Accessing, adding, updating, and removing elements
    - methods like: `clear`, `copy`, `get`, `pop`, `popitem`, and `update`
    - Checking if a key or value exists in a dictionary
3. Dictionary built-in methods:
    - `keys`, `values`, `items` for iterating over dictionaries
    - Dictionary comprehensions
4. Merging dictionaries using the `|` operator and the `update` method
5. Using dictionaries versus lists for data storage and retrieval:
    - Demonstrating querying data and organizing data workers for performance
6. JSON handling techniques including conversion of:
    - Dictionaries to JSON strings using `json.dumps()`
    - JSON strings to dictionaries using `json.loads()`
7. Sales data processing:
    - Example of handling a list of dictionaries
    - Aggregating and summing sales data by product
"""

# # Creating Dictionary, whic is a collection of key-value pairs keys are unique
# fruits ={"apple": "red", "banana": "yellow", "cherry": "red", "orange": "orange", "kiwi": "green", "mango": "yellow"}
# print(f"fruits : {fruits}") # output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'orange': 'orange', 'kiwi': 'green', 'mango': 'yellow'}

myD_empty = {}  # Empty dictionary
print(f"myD_empty_dict : {myD_empty}")  # output: {}
myD_numbers = {1: "one", 2: "two", 3: "three"}
print(f"myD_numbers : {myD_numbers}")  # output: {1: 'one', 2: 'two', 3: 'three'}
myD_list = [["four", 4], ["five", 5]]

print(f"myD_List : {dict(myD_list)}")
myD_tuple = ((6, "six"), (7, "seven"))
print(f"myD_Tuple : {dict(myD_tuple)}")

# Dictionary methods
# dict() constructor
# add() method is not available in dictionary
# clear() method removes all key-value pairs
# copy() method returns a copy of the dictionary
# get() method returns the value for the specified key
# items() method returns a list of key-value pairs
# keys() method returns a list of keys
# pop() method removes the specified key and returns the value
# popitem() method removes the last inserted key-value pair
# update() method updates the dictionary with the specified key-value pairs



employee = {"name": "Ahmet", "age": 25, "role": "Software Engineer"}
myD_employee = dict(employee)
print(f"myD_employee : {myD_employee}")

age =23
myD_age = dict(age=23)

my_breakfast = dict(egg="omelette", bread="toast", coffee="latte")
print(my_breakfast["egg"])  # output: omelette
myD_from_tuples = dict(myD_tuple)
print(f"myD_from_tuples", myD_from_tuples)  # output: {6: 'six', 7: 'seven'}
print(f"myD_from_tuples", myD_from_tuples[6])  # output: six

student = {"name": "Alice", "age": 15, "is_student": True}
print(f"student : {student}")  # output: {'name': 'Alice', 'age': 15, 'is_student': True}
print(f"student name : {student['name']}")  # output: Alice
print(f"student.get(age, not found) : {student.get("age", "not found")}")  # output: 15
print(f"student.get(class, not found) : {student.get("class", "not found")}")  # output: not found
student["class"] = 9
print(f"student after adding class : {student}")  # output: {'name': 'Alice', 'age': 15, 'is_student': True, 'class': 9}
student["age"] = 17
print(f"student after updating age : {student['age']}")  # output: 17
student.update({"age":18,"grade": "A"})
print(f"student after updating age and adding grade : {student}")  # output: {'name': 'Alice', 'age': 18, 'is_student': True, 'class': 9, 'grade


# Using dict() constructor with simple strings
my_fruits_form_string = dict(apple="red", banana="yellow", cherry="red")
print(f"my_fruits : {my_fruits_form_string}") # output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

# Using dict() constructor with list of tuples
my_list_tuples = [("Ahmet", 25), ("Mehmet", 30), ("Ali", 35)]
my_dict_form_list_tuples = dict(my_list_tuples)
print(f"my_dict_form_list_tuples : {my_dict_form_list_tuples}") # output: {'Ahmet': 25, 'Mehmet': 30, 'Ali': 35}

# Using dict() constructor with list of lists
my_list_lists = [["Jack", 25], ["Jane", 30], ["Josh", 35]]
my_dict_form_list_lists = dict(my_list_lists)
print(f"my_dict_form_list_lists : {my_dict_form_list_lists}") # output: {'Jack': 25, 'Jane': 30, 'Josh': 35}

my_oneitem_list = [("Ahmet", 25)]
my_dict_form_oneitem_list = dict(my_oneitem_list)
print(f"my_dict_form_oneitem_list : {my_dict_form_oneitem_list}") # output: {'Ahmet': 25}

character = {
    "name": "Ahmet",
    "age": 25,
    "weight": 72.5,
    "is_student": True,
}
print(f"character : {character}") # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True} - Dictionary
print(type(character)) # output: <class 'dict'> - Dictionary type

# Dictionary methods
# Accessing key-value pairs
print(character["name"]) # output: Ahmet - Accessing value by key
print(character["age"]) # output: 25 - Accessing value by key
# get() method returns the value for the specified key if key is in dictionary, else default value is returned
print(character.get("height", "height not found")) # output: not found - get() method returns the value for the specified key if key is in dictionary, else default value is returned

# Adding, updating, and removing key-value pairs
# Adding a new key-value pair
character["height"] = 175, 68.9
print(character) # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True, 'height': 175}

# No add method in dictionary
try:
    character.add("height", 175) # AttributeError: 'dict' object has no attribute 'add'
except AttributeError as e:
    print(e)

# Updating the value of an existing key
character["age"] = 26
print(character) # output: {'name': 'Ahmet', 'age': 26, 'weight': 72.5, 'is_student': True, 'height': 175}

# Updating multiple key-value pairs
character.update({"weight": 75.5, "is_student": False})
print(character) # output: {'name': 'Ahmet', 'age': 26, 'weight': 75.5, 'is_student': False, 'height': 175}
student = {"name": "Ahmet", "age": 26}
print(f"student : {student}") # output: {'name': 'Ahmet', 'age': 26}
student.update({"weight": 75.5, "is_student": False})
print(f"studnet updated : {student}") # output: {'name': 'Ahmet', 'age': 26, 'weight': 75.5, 'is_student': False}

# Removing a key-value pair using del keyword or pop() method or popitem() method
new_fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(f"new_fruits : {new_fruits}") # output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

# pop() method removes the specified key and returns the value
new_fruits.pop("banana") # Removing a key-value pair
print(f"new_fruits after removing banana : {new_fruits}") # output: {'apple': 'red', 'cherry': 'red'} 

safe_move = new_fruits.pop("banana", "not found") # Removing a key-value pair
print(f"safe_move : {safe_move}") # output: not found - pop() method removes the specified key and returns the value, if key is not found, default value is returned

# del keyword removes the specified key-value pair
del character["weight"] # Removing a key-value pair
print(f"character after removing weight : {character}") # output: {'name': 'Ahmet', 'age': 26, 'is_student': True, 'height': 175}
# output: {'name': 'Ahmet', 'age': 26, 'is_student': True, 'height': 175}

# popitem() method removes the last inserted key-value pair
character.popitem() # Removing the last inserted key-value pair
print(f"character after removing last inserted key-value pair : {character}") # output: {'name': 'Ahmet', 'age': 26, 'is_student': True}

# clear() method removes all key-value pairs
character.clear() # Removing all key-value pairs
print(f"character after removing all key-value pairs : {character}") # output: {}


# No remove method in dictionary
try:
    character.remove("age") # AttributeError: 'dict' object has no attribute 'remove'
except AttributeError as e:
    print(e)


def get_dictionary():
    return {
        "name": "Ahmet",
        "age": 25,
        "weight": 72.5,
        "is_student": True,
    }
get_dictionary()

student = {"name": "Ahmet", "age": 25, "is_student": True}
print(student.keys())# output: dict_keys(['name', 'age', 'is_student'])
print(student.values()) # output: dict_values(['Ahmet', 25, True])
print(student.items()) # output: dict_items([('name', 'Ahmet'), ('age', 25), ('is_student', True)])

for key in student.keys():
    print(key) # output: name, age, is_student
    
for value in student.values():
    print(value) # output: Ahmet, 25, True
    
for key, value in student.items():
    print(f"{key} : {value}") # output: name : Ahmet, age : 25, is_student : True

keys =['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(f"my_dict : {my_dict}") # output: {'a': 1, 'b': 2, 'c': 3}

keys =['a', 'b', 'c']
default_value = 0
my_dict = dict.fromkeys(keys, default_value)
print(f"my_dict : {my_dict}") # output: {'a': 0, 'b': 0, 'c': 0}

squre_dict = {x: x*x for x in range(6)}
print(f"squre_dict : {squre_dict}") # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



# keys() method returns a list of keys 
# values() method returns a list of values 
# items() method returns a list of key-value pairs
student = {"name": "Ahmet", "age": 25, "is_student": True}
print(student.keys())# output: dict_keys(['name', 'age', 'is_student'])
print(student.values()) # output: dict_values(['Ahmet', 25, True])
print(student.items()) # output: dict_items([('name', 'Ahmet'), ('age', 25), ('is_student', True)])

# Accessing key-value pairs using for loop 
for key in student.keys():
    print(key) # output: name, age, is_student

for value in student.values():
    print(value) # output: Ahmet, 25, True

for key, value in student.items():
    print(f"{key} : {value}") # output: name : Ahmet, age : 25, is_student : True

# zip() function Creating a dictionary from two lists using zip() function
keys =['a', 'b', 'c']
values = [1, 2, 3, 4, 5]
my_dict = dict(zip(keys, values))
print(f"my_dict : {my_dict}") # output: {'a': 1, 'b': 2, 'c': 3}

# fromkeys() method Creating a dictionary from a list of keys using fromkeys() method
new_keys =['a', 'b', 'c']
default_value = 0
new_my_dict = dict.fromkeys(new_keys, default_value)
print(f"new_my_dict : {new_my_dict}") # output: {'a': 0, 'b': 0, 'c': 0}

# Dictionary Comprehension
squre_d = {x: x**2 for x in range(6)}  # dictionary comprehension
print(f"squre_d : {squre_d}")  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squre_s = {x**2 for x in range(6) if x > 3}  # set comprehension
print(f"squre_s : {squre_s }")  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squre_t = tuple((x**2 for x in range(7) if x % 2 == 0)) #
print(f"squre_t : {squre_t }")  # output:

squre_l = [x**2 for x in range(6) if x % 2 == 1]  # list comprehension
print(f"squre_l : {squre_l }")  # output:

# Dictionary Comprehension
prices = {"apple": 1, "banana": 2, "orange": 3}
double_prices = {key: value * 2 for key, value in prices.items()}
print(
    f"double_prices : {double_prices}"
)  # output: {'apple': 2, 'banana': 4, 'orange': 6}

prices = {"apple": 1, "banana": 2, "orange": 3}
double_prices = {x: y * 2 for x, y in prices.items()}
print(
    f"double_prices : {double_prices}"
)  # output: {'apple': 2, 'banana': 4, 'orange': 6}

prices = {"apple": 1, "banana": 2, "orange": 3}
double_prices = {a: b * 2 for a, b in prices.items()}
print(
    f"double_prices : {double_prices}"
)  # output: {'apple': 2, 'banana': 4, 'orange': 6}

# Merging Dictionaries Using the | Operator
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}
merged_dict = dict_1 | dict_2
print(f"merged_dict : {merged_dict}")  # output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
print(f"dict_1 : {dict_1}")  # output: {'a': 1, 'b': 2, 'c': 3}

# Updating Dictionaries by Merging
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}
dict_1.update(dict_2)
print(f"dict_1 : {dict_1}")  # output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}


# Dictionaries vs Lists 
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 80}
print(student_scores["Alice"])  # output: 90
print(student_scores["Charlie"])  # output: 80

student_socres_list = [["Alice", 90], ["Bob", 85], ["Charlie", 80]]
for student, score in student_socres_list:
    if student == "Bob":
        print(f"{student} : {score}")
        break

# Using list comprehension to find the score of "Bob"
bob_score = [score for student, score in student_socres_list if student == "Bob"]

# Print the result if "Bob" is found
if bob_score:
    print(f"Bob : {bob_score[0]}")

# JSON to Dictionary
# json.loads() JSON string > dictionary 
# json.dumps() dictionary > JSON string

import json

# JSON string to dictionary
# JSON string
json_string = '{"name": "Ahmet", "age": 25, "is_student": True}'
# Convert JSON string to dictionary
student = json.loads(json_string)
print(f"student : {student}")  # output: {'name': 'Ahmet', 'age': 25, 'is_student': True}

# Dictionary to JSON
# Dictionary
student_dict = {"name": "Ahmet", "age": 25, "is_student": True}
# Convert dictionary to JSON string
student_dict_to_json_string = json.dumps(student_dict)
print(f"student_dict_to_json_string : {student_dict_to_json_string}")  # output: {"name": "Ahmet", "age": 25, "is_student": true}


sales_data = [
    {"date": "2021-01-01", "product": "Apple", "quantity": 1, "price": 5000},
    {"date": "2021-01-02", "product": "IBM", "quantity": 2, "price": 2000},
    {"date": "2021-01-03", "product": "Apple", "quantity": 3, "price": 5000},
    {"date": "2021-01-04", "product": "IBM", "quantity": 4, "price": 2000},
    {"date": "2021-01-05", "product": "Apple", "quantity": 5, "price": 5000},
]
product_sales = {}
for sales in sales_data:
    product = sales["product"]
    total = sales["quantity"] * sales["price"]
    product_sales[product] = product_sales.get(product, 0) + total

print(f"product_sales : {product_sales}")  #  
