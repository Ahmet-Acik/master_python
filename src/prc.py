# try:
#     invalid_set = {
#         1,
#         "Python",
#         3,
#         4,
#         5,
#         [6, 7, 8, 9, 10],
#         10,
#     }  # TypeError: unhashable type: 'list'
#     print(f"invalid_set: {invalid_set}")
# except TypeError as e:
#     print(f"invalid_set: {e}")
# try:
#     invalid_set = {
#         1,
#         "Python",
#         3,
#         4,
#         5,
#         (6, 7, 8, 9, 10),
#         10,
#     }  # TypeError: unhashable type: 'list'
#     print(f"set: {invalid_set}")
# except TypeError as e:
#     print(f"invalid_set: {e}")

# try:
#     invalid_set = {
#         1,
#         "Python",
#         3,
#         4,
#         5,
#         { 7, 9, 12},
#         10,
#     }  # TypeError: unhashable type: 'list'
#     print(f"set: {invalid_set}")
# except TypeError as e:
#     print(f"invalid_set: {e}")
    
# try:
#     invalid_set = {
#         1,
#         "Python",
#         3,
#         4,
#         5,
#         {6 : 7, 8 : 9, 10 : 12},
#         10,
#     }  # TypeError: unhashable type: 'list'
#     print(f"set: {invalid_set}")
# except TypeError as e:
#     print(f"invalid_set: {e}")


# my_set = {1, 2, 3, 4, 5}
# my_empty_set = {}
# print(my_empty_set)
# print(my_set)

# # Sets are unordered, unindexed, and do not allow duplicates 
# # Set Methods - add, copy, remove, discard, pop, clear 
# # my_set.add(6)
# print(f"my_set after adding 6: {my_set}") # output: {1, 2, 3, 4, 5, 6}
# my_set.copy()
# print(f"my_set after copying: {my_set}") # output: {1, 2, 3, 4, 5, 6}
# my_set.discard(6) # Removes the specified element from the set - Does not raise an error if the element is not found
# print(f"my_set after discarding 6: {my_set}") # output: {1, 2, 4, 5, 6}

# item = my_set.pop()
# print(f"my_set after popping: {my_set}") # 
# print(f"item popped: {item}") # output: 1


# try:
#     my_set.remove(6) 
#     print(f"my_set after removing 6: {my_set}") # output: {1, 2, 5, 6}
# except KeyError as e:
#     print(f"Error, set does not include: {e}")
    
    
# age = 23
# my_dict ={'age': 23, "name": "Ahmet", "age": 25, "role": "Software Engineer"}
# print(f"my_dict : {my_dict}")

# myD_employee = dict(my_dict)

# myD_age = dict(age=23)
# print(f"myD_age : {myD_age}")
# import numpy as np

# np_mdarray = np.array([[[1, 2, 3], [4, 5, 6]]])

# print(f"np_mdarray: {np_mdarray}")  # np_mdarray: [[1 2 3]  [4 5 6]]

# # try:
# #     my_set = {1, 2, 3, 4, 5}
# #     my_set.add(6,7,8,9,10)
# #     print(f"my_set after adding 6_10: {my_set}")  # output: {1, 2, 3, 4, 5, 6}
# # except TypeError as e:
# #     print(f"Error: {e}")

# my_set2 = {0, 2, 3, 4, 5}
# my_set2.add(3.5) # bool, int, float, str, tuple, frozenset
# # my_set2.update((6,7,8,9,10)) 
# # my_set2.update([6,7,8,9,10])
# my_set2.update({6,7,8,9,10}, [11, 12, 13], (14, 15, 16)) # add multiple itearables to the set
# print(f"my_set after adding 6_10: {my_set2}")

  
# my_oneitem_list = ["Ahmet", 25] 
# my_dict_form_oneitem_list = dict(my_oneitem_list)
# print(f"my_dict_form_oneitem_list : {my_dict_form_oneitem_list}") # output: {'Ahmet': 25}

# my_oneitem_tuple = ("Ahmet", 25)
# my_dict_form_oneitem_tuple = dict(my_oneitem_tuple)
# print(f"my_dict_form_oneitem_tuple : {my_dict_form_oneitem_tuple}") # output: {'Ahmet': 25}

myD_numbers = {'name': "one", 'age': "two", "city": "three"}

print(f"myD_numbers : {myD_numbers['age']}")  # output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(f"myD_numbers : {myD_numbers['age']}")  # output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(f"myD_numbers : {myD_numbers['age']}")  # output: 

print(f"myD_numbers.get('salary', 'not found') : {myD_numbers.get('salary', 'not found')}")  # output: myD_numbers.get('salary', 'not found')  # output: not found

# myD_numbers.name = "four"
# print(f"myD_numbers : {myD_numbers.name}")  # output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

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
character["height"] = 175, 68.9 # Adds the specified element to the set
print(character) # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True, 'height': (175, 68.9)}
# Updating the value of an existing key
character["age"] = 26
print(character) # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True, 'height': 175}
