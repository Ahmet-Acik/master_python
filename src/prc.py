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

# myD_numbers = {'name': "one", 'age': "two", "city": "three"}

# print(f"myD_numbers : {myD_numbers['age']}")  # output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# print(f"myD_numbers : {myD_numbers['age']}")  # output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# print(f"myD_numbers : {myD_numbers['age']}")  # output:

# print(f"myD_numbers.get('salary', 'not found') : {myD_numbers.get('salary', 'not found')}")  # output: myD_numbers.get('salary', 'not found')  # output: not found

# # myD_numbers.name = "four"
# # print(f"myD_numbers : {myD_numbers.name}")  # output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# character = {
#     "name": "Ahmet",
#     "age": 25,
#     "weight": 72.5,
#     "is_student": True,
# }
# print(f"character : {character}") # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True} - Dictionary
# print(type(character)) # output: <class 'dict'> - Dictionary type

# # Dictionary methods
# # Accessing key-value pairs
# print(character["name"]) # output: Ahmet - Accessing value by key
# print(character["age"]) # output: 25 - Accessing value by key
# # get() method returns the value for the specified key if key is in dictionary, else default value is returned
# print(character.get("height", "not found")) # output: not found - get() method returns the value for the specified key if key is in dictionary, else default value is returned

# # Adding, updating, and removing key-value pairs
# # Adding a new key-value pair
# character["height"] = 175, 68.9 # Adds the specified element to the set
# print(character) # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True, 'height': (175, 68.9)}
# # Updating the value of an existing key
# character["age"] = 26
# print(character) # output: {'name': 'Ahmet', 'age': 25, 'weight': 72.5, 'is_student': True, 'height': 175}


# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [item for sublist in nested_list for item in sublist]
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Example 1: Flattening a list of lists  syntax
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([x for sublist in nested_list for x in sublist])

# # Example 2: Filtering and flattening a list of lists
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# even_numbers = [num for sublist in nested_list for num in sublist if num % 2 == 0]
# even_numbers = [x for sublist in nested_list for x in sublist if x % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6, 8]
# odd_numbers = [x for sublist in nested_list for x in sublist if x % 2 == 1]
# print(odd_numbers)


# for x in range(0, 100, 10):
#     print(x)

# mylist = [x for x in range(0,100,5)]  # Create a list of numbers from 0 to 100 with a step of 5
# print(mylist)

# while True:
#     user_input = input("Enter a number: ")
#     if user_input == "q":
#         break
#     print(user_input)


# for x in range(1, 13):
#     for y in range(1, 13):
#         print(f"{x} * {y} = {x*y}")
#     print()


# even = []
# odd = []
# [even.append(x) if x %2==0 else odd.append(x) for x in range(20)]
# print(even)
# print(odd)


# student = {"name": "Ahmet", "age": 25, "is_student": True}
# print(student.keys())# output: dict_keys(['name', 'age', 'is_student'])
# print(student.values()) # output: dict_values(['Ahmet', 25, True])
# print(student.items()) # output: dict_items([('name', 'Ahmet'), ('age', 25), ('is_student', True)])

# for key in student.keys():
#     print(key) # output: name, age, is_student

# for value in student.values():
#     print(value) # output: Ahmet, 25, True

# for key, value in student.items():
#     print(f"{key} : {value}") # output: name : Ahmet, age : 25, is_student : True


# keys =['a', 'b', 'c']
# values = [1, 2, 3, 4, 5]
# my_dict = dict(zip(keys, values))
# print(f"my_dict : {my_dict}") # output: {'a': 1, 'b': 2, 'c': 3}

# new_keys =['a', 'b', 'c']
# default_value = 0
# new_my_dict = dict.fromkeys(new_keys, default_value)
# print(f"new_my_dict : {new_my_dict}") # output: {'a': 0, 'b': 0, 'c': 0}

# squre_d = {x: x**2 for x in range(6)}  # dictionary comprehension
# print(f"squre_d : {squre_d}")  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# squre_s = {x**2 for x in range(6) if x > 3}  # set comprehension
# print(f"squre_s : {squre_s }")  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# squre_t = tuple((x**2 for x in range(7) if x % 2 == 0))
# print(f"squre_t : {squre_t }")  # output:

# squre_l = [x**2 for x in range(6) if x % 2 == 1]  # list comprehension
# print(f"squre_l : {squre_l }")  # output:

# prices = {"apple": 1, "banana": 2, "orange": 3}
# double_prices = {key: value * 2 for key, value in prices.items()}
# print(
#     f"double_prices : {double_prices}"
# )  # output: {'apple': 2, 'banana': 4, 'orange': 6}

# prices = {"apple": 1, "banana": 2, "orange": 3}
# double_prices = {x: y * 2 for x, y in prices.items()}
# print(
#     f"double_prices : {double_prices}"
# )  # output: {'apple': 2, 'banana': 4, 'orange': 6}

# prices = {"apple": 1, "banana": 2, "orange": 3}
# double_prices = {a: b * 2 for a, b in prices.items()}
# print(
#     f"double_prices : {double_prices}"
# )  # output: {'apple': 2, 'banana': 4, 'orange': 6}

# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"b": 4, "c": 5, "d": 6}
# merged_dict = dict_1 | dict_2
# # print(f"merged_dict : {merged_dict}")  # output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
# # print(f"dict_1 : {dict_1}")  # output: {'a': 1, 'b': 2, 'c': 3}

# # dict_1 = {"a": 1, "b": 2, "c": 3}
# # dict_2 = {"b": 4, "c": 5, "d": 6}
# # dict_1.update(dict_2)
# # print(f"dict_1 : {dict_1}")  # output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}

# # student_scores = {"Alice": 90, "Bob": 85, "Charlie": 80}
# # print(student_scores["Alice"])  # output: 90
# # print(student_scores["Charlie"])  # output: 80

# # student_scores_list = [["Alice", 90], ["Bob", 85], ["Charlie", 80]]
# # for student, score in student_scores_list:
# #     if student == "Bob":
# #         print(f"{student} : {score}")
# #         break

# # # Using list comprehension to find the score of "Bob"
# # bob_score = [score for student, score in student_scores_list if student == "Bob"]

# # # Print the result if "Bob" is found
# # if bob_score:
# #     print(f"Bob : {bob_score[0]}")

# # print(student_scores_list[0])


# # my_dict = {"fruit": "apple", "sweet": "candy", "cake": "apple pie", "drink" : "water", "food": "apple jam", "snack": "candy"}
# # filtered_dict = filter(lambda x: x[1].startswith("a"), my_dict.items())
# # print(f"filtered_dict {dict(filtered_dict)}") #


# # # Dictionaries vs Lists
# # # student_scores = {"Alice": 90, "Bob": 85, "Charlie": 80}

# # # print(student_scores["Charlie"])  # output: 80

# # student_socres_list = '{"Alice": 90, "Bob": 95, "Charlie": 80, "Bob": 60}'
# # student_socres_list2 = {"Alice": 20, "Bob": 95, "Charlie": 50, "Bob": 60}


# # import json

# # print(json.loads(student_socres_list))
# # print(json.dumps(student_socres_list2))


# # # for student, score in student_socres_list:
# # #     if student == "Bob":
# # #         print(f"{student} : {score}")
# # #         break
# # # # print(student_socres_list["Bob"]) # output: 95
# # # print(student_socres_list[0]) # output: 95
# # # print(student_socres_list[0:2]) # output: 95

# # sales_data = [
# #     {"date": "2021-01-01", "product": "apple", "quantity": 1, "price": 5000},
# #     {"date": "2021-01-02", "product": "IBM", "quantity": 2, "price": 2000},
# #     {"date": "2021-01-03", "product": "apple", "quantity": 3, "price": 5000},
# #     {"date": "2021-01-04", "product": "IBM", "quantity": 4, "price": 2000},
# #     {"date": "2021-01-05", "product": "apple", "quantity": 5, "price": 5000},
# # ]
# # product_sales = {}
# # for sales in sales_data:
# #     product = sales["product"]
# #     total = sales["quantity"] * sales["price"]
# #     product_sales[product] = product_sales.get(product, 0) + total

# # # print(f"product_sales : {product_sales}")  # output: {'apple': 60000}

# # def describe_pet(animal_type, pet_name):
# #     print(f"I have a {animal_type}.")
# #     print(f"My {animal_type}'s name is {pet_name}.")

# # describe_pet(animal_type="dog", pet_name="Buddy")


# # def add_item_toList(item, abc=None):
# #     if abc is None:
# #         abc = []
# #     abc.append(item)
# #     return abc

# # print(add_item_toList(5))
# # print(add_item_toList(10))
# # print(add_item_toList(15))

# # def add_item_toList(item, abc=[]):
# #     abc.append(item)
# #     return abc

# # print(add_item_toList(5))
# # print(add_item_toList(10))
# # print(add_item_toList(15))

# # def hello(name):
# #     return f"Hello World! {name}"

# # say = hello

# # print(say("Ahmet"))

# # def greet(name:str, age:int):
# #     return f"Hello, {name}, you are {age} years old!"

# # print(hello("ahmet"))


# # def requires_permission(permission):
# #     def decorator(func):
# #         def wrapper(user, args):
# #             if user.get("permissions") and permission in user["permissions"]:
# #                 return func(user, args)
# #             else:
# #                 print(f"User '{user['name']}' does not have permission '{permission}'")
# #         return wrapper
# #     return decorator

# # # @requires_permission("admin")
# # # def delete_user(user, user_to_delete):
# # #     print(f"User '{user_to_delete}' deleted by '{user['name']}'")

# # # user = {"name": "Alice", "permissions": ["admin"]}
# # # delete_user(user, "Bob")

# # # user = {"name": "Bob", "permissions": ["user"]}
# # # delete_user(user, "Charlie")

# # def add(x, y):
# #     return x + y


# # print((lambda x,y: x+y)(2,3))
# # print((lambda x: x**3)(3))

# # print((lambda x: x.capitalize())("HELLO"))

# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "kiwi",
#     "mango",
#     "orange",
#     "pineapple",
#     "strawberry",
#     "watermelon",
#     "grape",
#     "blueberry",
#     "raspberry",
#     "blackberry",
#     "papaya",
#     "pear",
#     "peach",
#     "plum",
#     "pomegranate",
#      "melon"
# ]
# fruits_with_p = list(filter(lambda x: x.startswith("p"), fruits))
# print(fruits_with_p)

# fruits_with_b = list(
#     filter(
#         lambda x: x.startswith("b"),
#         [
#             "apple",
#             "banana",
#             "cherry",
#             "kiwi",
#             "mango",
#             "orange",
#             "pineapple",
#             "strawberry",
#             "melon",
#             "watermelon",
#             "grape",
#             "blueberry",
#             "raspberry",
#             "blackberry",
#             "papaya",
#             "pear",
#         ],
#     )
# )
# print(fruits_with_b)


# fruits = ["apple", "banana", "cherry", "mango", "melon", "orange"]
# fruits_with_m = []
# for x in fruits:
#     if x.startswith("m"):
#         fruits_with_m.append(x)

# print(fruits_with_m)

# print(list(filter(lambda x: x.startswith("m"), fruits)))

# strs =["ahmet", "mehmet", "ali", "veli", "ayse", "fatma", "zeynep", "elif", "aylin"]
# # strs_with_a = list(filter(lambda x: x.startswith("a"), strs))
# # print(strs_with_a)

# # # numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# # # print(even_numbers)
# # # odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
# # # print(odd_numbers)
# # # numbers_over_5 = list(filter(lambda x: x > 5, numbers))
# # # print(numbers_over_5)
# # # numbers_under_5 = list(filter(lambda x: x < 5, numbers))
# # # print(numbers_under_5)


# # strs_to_upper = list(map(lambda x: x.upper(), strs))
# # print(strs_to_upper)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)
# cube_numbers = list(map(lambda x: x ** 3, numbers))
# print(cube_numbers)
# add_10_precent = list(map(lambda x: round(x * 1.1,2), numbers))
# print((add_10_precent))

# def addtenpercent(x):
#     return round(x * 1.1,2)

# add_10_precent = list(map(addtenpercent, numbers))
# print((add_10_precent))

# strs =["ahmet", "mehmet", "ali", "veli", "ayse", "fatma", "zeynep", "elif", "aylin"]
# zfill_strs = list(map(lambda x: x.zfill(10), strs))
# print(zfill_strs)

# def get_biweekly_period(week):
#     return (week // 2) + 1

# # Example usage
# print(get_biweekly_period(0))  # Output: 1
# print(get_biweekly_period(1))  # Output: 1
# print(get_biweekly_period(2))  # Output: 2
# print(get_biweekly_period(3))  # Output: 2
# print(get_biweekly_period(4))  # Output: 3
# print(get_biweekly_period(5))  # Output: 3


# import logging

# logging.basicConfig(level=logging.DEBUG)


# def process_data(data):
#     logging.debug("Processing data: %s", data)
#     if not data:
#         logging.warning("No data provided")
#         raise ValueError("Data cannot be empty")
#     # Processing logic goes here
#     logging.debug("Data process started successfully")

#     try:
#         if len(data) < 2:
#             raise ValueError("Data must contain at least two elements")
#         result = data[0] / data[1]
#         logging.info("Calculating Result: %s", result)
#     except ZeroDivisionError as e:
#         logging.error("ZeroDivisionError: %s", e)
#     except TypeError as e:
#         logging.error("TypeError: %s", e)
#     except Exception as e:
#         logging.error("Exception occurred: %s", e)
#     else:
#         logging.info("No exception occurred")
#     finally:
#         logging.info("Data processing complete")


# print(f"process_data([10, 5]) : {process_data([10, 5])}")
# # data = [10, 5]
# # process_data(data)
# print(f"process_data([10, 0]) : {process_data([10, 0])}")
# # data = [10, 0]
# # process_data(data)
# print(f"process_data([]) : {process_data([])}")
# # data = []
# # process_data(data)


nested_list1 =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
flattened_list = [num for sublist in nested_list1 for num in sublist if num > 3 and not num % 2 == 0]
print(flattened_list)

import os 

text_file_path ='flt.txt'

if not os.path.exists(text_file_path):
    with open(text_file_path, 'w') as file:
        file.write('1,2,3\n4,5,6\n7,8,9')
