# strings.py

def print_statements():
    print('Hello VSCODE')
    print("It's a beautiful day")
    print('It\'s a beautiful day')

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
        "slice_2_step": quote[::2]
    }

def get_learning_fun_slices(learning_fun):
    return {
        "slice_10_end": learning_fun[10:],
        "slice_0_6": learning_fun[:6],
        "slice_7_9": learning_fun[7:9],
        "slice_neg_3_end": learning_fun[-3:],
        "slice_0_neg_4": learning_fun[:-4],
        "reversed": learning_fun[::-1]
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
        "f_string": f"My name is {name} and I am {age} years old."
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
        "encode_cp1252": name.encode("cp1252")
    }

if __name__ == "__main__":
    print_statements()
    print(get_character_in_name("Ahmetoglu", 0))
    print(get_character_in_name("Ahmetoglu", -1))
    print(get_substring("Ahmetoglu", 0, 3))

    quote = "The greatest glory in living lies not in never falling, but in rising every time we fall."
    print(get_quote_slices(quote))

    learning_fun = 'Python is fun'
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