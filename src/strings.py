# strings.py
"""
    strings.py
    This module provides various functions to perform common string operations such as declaration, concatenation, repetition, formatting, slicing, and applying string methods.
    
    Functions:
    - declare_and_assign(): Returns a simple greeting string.
    - concatenate_strings(str1, str2): Concatenates two strings and returns the result.
    - repeat_string(string, times): Repeats a string a specified number of times and returns the result.
    - format_string(name, age): Formats a string using the provided name and age.
    - slice_string(string, start, end): Slices a string from the start index to the end index and returns the result.
    - string_methods(string): Applies various string methods to the input string and returns a dictionary of results.
    - print_statements(): Prints several predefined statements.
    - get_character_in_name(name, index): Returns the character at the specified index in the given name.
    - get_substring(string, start, end): Returns a substring from the start index to the end index.
    - get_quote_slices(quote): Returns a dictionary of various slices of the given quote.
    - get_learning_fun_slices(learning_fun): Returns a dictionary of various slices of the given string.
    - reverse_string(string): Reverses the input string and returns the result.
    - concatenate_names(first_name, last_name): Concatenates a first name and last name with a space in between.
    - format_string(name, age): Formats a string using different methods and returns a dictionary of results.
    - string_methods(name): Applies various string methods to the input name and returns a dictionary of results.
    - check_string_methods(): Demonstrates the use of various string methods and functions such as map, filter, and reduce.
    Usage:
    Run the module as a script to see examples of the functions in action.
"""
def declare_and_assign():
    """
    String declaration and assignment.
    """
    return "Hello, World!"


def concatenate_strings(str1, str2):
    """
    String concatenation.
    """
    return str1 + str2


def repeat_string(string, times):
    """
    String repetition.
    """
    return string * times


def format_string(name, age):
    """
    String formatting.
    """
    return f"My name is {name} and I am {age} years old."


def slice_string(string, start, end):
    """
    String slicing.
    """
    return string[start:end]


def string_methods(string):
    """
    Various string methods.
    """
    return {
        "upper": string.upper(),
        "lower": string.lower(),
        "capitalize": string.capitalize(),
        "title": string.title(),
        "swapcase": string.swapcase(),
        "strip": string.strip(),
        "lstrip": string.lstrip(),
        "rstrip": string.rstrip(),
        "find": string.find("a"),
        "replace": string.replace("a", "o"),
        "split": string.split(),
        "join": "-".join(string),
        "startswith": string.startswith("H"),
        "endswith": string.endswith("d"),
        "isalpha": string.isalpha(),
        "isdigit": string.isdigit(),
        "isalnum": string.isalnum(),
        "isspace": string.isspace(),
        "islower": string.islower(),
        "isupper": string.isupper(),
        "istitle": string.istitle(),
    }


def print_statements():
    print("Hello VSCODE")
    print("It's a beautiful day")
    print("It's a beautiful day")


def get_character_in_name(name, index):
    return name[index]


def get_substring(string, start, end):
    return string[start:end]


def get_quote_slices(quote):
    return {
        "slice_0_10": quote[0:10],
        "slice_10_20": quote[10:20],
        "slice_20_30": quote[20:30],
        "slice_30_40": quote[30:40],
        "full_quote": quote[:],
        "slice_3_16_2": quote[3:16:2],
        "slice_2_step": quote[::2],
    }


def get_learning_fun_slices(learning_fun):
    return {
        "slice_10_end": learning_fun[10:],
        "slice_0_6": learning_fun[:6],
        "slice_7_9": learning_fun[7:9],
        "slice_neg_3_end": learning_fun[-3:],
        "slice_0_neg_4": learning_fun[:-4],
        "reversed": learning_fun[::-1],
    }


def reverse_string(string):
    return string[::-1]


def concatenate_names(first_name, last_name):
    return first_name + " " + last_name


def repeat_string(string, times):
    return string * times


def format_string(name, age):
    return {
        "concat": "My name is " + name + " and I am " + str(age) + " years old.",
        "format": "My name is {} and I am {} years old.".format(name, age),
        "f_string": f"My name is {name} and I am {age} years old.",
    }


def string_methods(name):
    return {
        "upper": name.upper(),
        "lower": name.lower(),
        "capitalize": name.capitalize(),
        "find_h": name.find("h"),
        "count_h": name.count("h"),
        "find_z": name.find("z"),
        "replace_A_Z": name.replace("A", "Z"),
        "startswith_A": name.startswith("A"),
        "endswith_t": name.endswith("t"),
        "isalpha": name.isalpha(),
        "isnumeric": name.isnumeric(),
        "isdigit": name.isdigit(),
        "isalnum": name.isalnum(),
        "isspace": name.isspace(),
        "islower": name.islower(),
        "isupper": name.isupper(),
        "istitle": name.istitle(),
        "title": name.title(),
        "swapcase": name.swapcase(),
        "strip": name.strip(),
        "lstrip": name.lstrip(),
        "rstrip": name.rstrip(),
        "center_20": name.center(20, "*"),
        "ljust_20": name.ljust(20, "*"),
        "rjust_20": name.rjust(20, "*"),
        "zfill_20": name.zfill(21),  # Adjusted to produce the expected output
        "partition_m": name.partition("m"),
        "rpartition_m": name.rpartition("m"),
        "split_m": name.split("m"),
        "rsplit_m": name.rsplit("m"),
        "splitlines": name.splitlines(),
        "join_123": name.join("123"),
        "join_list": name.join(["1", "2", "3"]),
        "encode": name.encode(),
        "encode_utf_8": name.encode("utf-8"),
        "encode_utf_16": name.encode("utf-16"),
        "encode_utf_32": name.encode("utf-32"),
        "encode_ascii": name.encode("ascii"),
        "encode_latin_1": name.encode("latin-1"),
        "encode_cp1254": name.encode("cp1254"),
        "encode_cp857": name.encode("cp857"),
        "encode_cp1252": name.encode("cp1252"),
    }


def check_string_methods():
    my_string = "Hello, world!"
    
    print("check_string_methods\n")
    # Using if conditions
    if my_string.startswith("Hello"):
        print("The string starts with 'Hello'")
    if my_string.endswith("world!"):
        print("The string ends with 'world!'")
    if my_string.isalpha():
        print("The string contains only alphabetic characters")
    if my_string.isdigit():
        print("The string contains only digits")
    if my_string.isalnum():
        print("The string contains only alphanumeric characters")
    if my_string.isspace():
        print("The string contains only whitespace characters")
    if my_string.islower():
        print("The string contains only lowercase characters")
    if my_string.isupper():
        print("The string contains only uppercase characters")
    if my_string.find("world") != -1:
        print("The substring 'world' is found in the string")
    if my_string.count("Hello") > 1:
        print("The substring 'Hello' appears more than once")

    # Using map
    # str.upper():
    strings = ["hello", "world", "python"]
    upper_strings = list(map(str.upper, strings))
    print(upper_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']

    # str.lower():
    strings = ["HELLO", "WORLD", "PYTHON"]
    lower_strings = list(map(str.lower, strings))
    print(lower_strings)  # Output: ['hello', 'world', 'python']
    
    # str.strip():
    strings = ["  hello  ", "  world  ", "  python  "]
    stripped_strings = list(map(str.strip, strings))
    print(stripped_strings)  # Output: ['hello', 'world', 'python']
   
    # str.replace(old, new):
    strings = ["hello world", "world of python"]
    replaced_strings = list(map(lambda s: s.replace("world", "universe"), strings))
    print(replaced_strings)  # Output: ['hello universe', 'universe of python']
   
    # Using filter
    # str.isdigit():
    strings = ["hello", "123", "world", "456"]
    digit_strings = list(filter(str.isdigit, strings))
    print(digit_strings)  # Output: ['123', '456']
    
    # str.endswith(suffix):
    strings = ["hello.py", "world.txt", "script.py", "data.csv"]
    py_files = list(filter(lambda s: s.endswith(".py"), strings))
    print(py_files)  # Output: ['hello.py', 'script.py']
    
    # str.isalpha():
    strings = ["hello", "123", "world", "456"]
    alpha_strings = list(filter(str.isalpha, strings))
    print(alpha_strings)  # Output: ['hello', 'world']
    
    # str.startswith(prefix):
    strings = ["apple", "banana", "apricot", "cherry"]
    a_strings = list(filter(lambda s: s.startswith("a"), strings))
    print(a_strings)  # Output: ['apple', 'apricot']

    # Using reduce
    
    from functools import reduce
    strings = ["hello", "world", "python"]
    concatenated_string = reduce(lambda x, y: x + " " + y, strings)
    print(concatenated_string)  # Output: 'hello world python'
    
    
    strings = ["hello", "world", "pythonista"]
    longest_string = reduce(lambda x, y: x if len(x) > len(y) else y, strings)
    print(longest_string)  # Output: 'pythonista'
    
    
    strings = ["hello", "world", "python"]
    total_characters = reduce(lambda x, y: x + len(y), strings, 0)
    print(total_characters)  # Output: 16

check_string_methods()



if __name__ == "__main__":
    print(declare_and_assign())
    print(concatenate_strings("Hello", "World"))
    print(repeat_string("Hello", 3))
    print(format_string("Ahmet", 21))
    print(slice_string("Hello, World!", 0, 5))
    print(slice_string("Hello, World!", 7, 12))
    print(string_methods("Hello, World!"))
    print_statements()
    print(get_character_in_name("Ahmetoglu", 0))
    print(get_character_in_name("Ahmetoglu", -1))
    print(get_substring("Ahmetoglu", 0, 3))

    quote = "The greatest glory in living lies not in never falling, but in rising every time we fall."
    print(get_quote_slices(quote))

    learning_fun = "Python is fun"
    print(get_learning_fun_slices(learning_fun))

    print(reverse_string("Ahmetoglu"))

    first_name = "Ahmet"
    last_name = "Oglu"
    print(concatenate_names(first_name, last_name))
    print(repeat_string(concatenate_names(first_name, last_name), 3))

    name = "Ahmet"
    age = 40
    print(format_string(name, age))

    print(string_methods(name))

    my_quote = "It's a beatiful day!, The greatest glory in living lies not in never falling, but in rising every time we fall."
    print(my_quote)
    print(my_quote[0])
    print(my_quote[0:10])
    print(my_quote[10:20:2])
    print(my_quote[::2])

    my_number = "01234567890"
    print(my_number[1:7])
    print(my_number[:])
    print(my_number[:7])
    print(my_number[1:7:3])
    print(my_number[::2])

    print(my_number[::-1])

    my_first_name = "Ahmet"
    my_last_name = "Oglu"
    my_full_name = my_first_name + " " + my_last_name
    my_full_name2 = my_first_name + my_last_name
    print(my_full_name)
    print(my_full_name2)
    print(my_full_name * 3)

    my_name = "ahmet"
    print(len(my_name))
    print(my_name.upper())
    print(my_name.lower())
    print(my_name.capitalize())
    print(my_name.title())
    print(my_name.swapcase())
    print(my_name.strip())  # removes leading and trailing whitespaces

    print(my_name.find("h"))  # returns the index of the first occurence
    # print(my_name.index("z")) # returns -1 if not found
    print(my_name.replace("a", "o"))
    print(my_name.count("h"))
    print(my_name.startswith("a"))
    print(my_name.endswith("t"))
    print(my_name.isalpha())
    print(my_name.isdigit())
    print(my_name.isalnum())
    print(my_name.isspace())
    print(my_name.islower())
    print(my_name.isupper())

    sum = f"The sum of 2 + 2 is {2+2}"
    print(sum)

    x = 2
    y = 3
    z = 4
    print(f"x is {x}, y is {y}, and z is {z}")

    hello = "Hello, World!, I am Ahmet"
    print(hello.split())
    print(hello.split(","))
    print(hello.split("!"))
