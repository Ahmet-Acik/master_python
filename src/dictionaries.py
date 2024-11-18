# dictionarioes.py

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
print(character.get("height", "not found")) # output: not found - get() method returns the value for the specified key if key is in dictionary, else default value is returned

# Adding, updating, and removing key-value pairs
# Adding a new key-value pair
character["height"]["cm"] = 175, 68.9
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
