# dictionarioes.py

fruits ={"apple": "red", "banana": "yellow", "cherry": "red", "orange": "orange", "kiwi": "green", "mango": "yellow"}
print(f"fruits : {fruits}") # output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'orange': 'orange', 'kiwi': 'green', 'mango': 'yellow'}

my_fruits_form_string = dict(apple="red", banana="yellow", cherry="red") # Using dict() constructor with simple strings
print(f"my_fruits : {my_fruits_form_string}") # output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

my_list_tuples = [("Ahmet", 25), ("Mehmet", 30), ("Ali", 35)] # Using dict() constructor with list of tuples
my_dict_form_list_tuples = dict(my_list_tuples)
print(f"my_dict_form_list_tuples : {my_dict_form_list_tuples}") # output: {'Ahmet': 25, 'Mehmet': 30, 'Ali': 35}

character = {
    "name": "Ahmet",
    "age": 25,
    "weight": 72.5,
    "is_student": True,
}
print(f"character : {character}") # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True} - Dictionary
print(type(character)) # output: <class 'dict'> - Dictionary type

print(character["name"]) # output: Ahmet - Accessing value by key
print(character["age"]) # output: 25 - Accessing value by key
print(character.get("height", "not found")) # output: not found - get() method returns the value for the specified key if key is in dictionary, else default value is returned

# Adding, updating, and removing key-value pairs
character["height"] = 175 # Adding a new key-value pair
print(character) # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True, 'height': 175}

# No add method in dictionary
try:
    character.add("height", 175) # AttributeError: 'dict' object has no attribute 'add'
except AttributeError as e:
    print(e)
    
character["age"] = 26 # Updating the value of an existing key
print(character) # output: {'name': 'Ahmet', 'age': 26, 'weight': 72.5, 'is_student': True, 'height': 175}
character.update({"weight": 75.5, "is_student": False}) # Updating multiple key-value pairs
print(character) # output: {'name': 'Ahmet', 'age': 26, 'weight': 75.5, 'is_student': False, 'height': 175}

# Removing a key-value pair
del character["weight"] # Removing a key-value pair
print(character) # output: {'name': 'Ahmet', 'age': 26, 'is_student': True, 'height': 175}

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