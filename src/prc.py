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
    
    
age = 23
my_dict ={'age': 23, "name": "Ahmet", "age": 25, "role": "Software Engineer"}
print(f"my_dict : {my_dict}")

myD_employee = dict(my_dict)

myD_age = dict(age=23)
print(f"myD_age : {myD_age}")