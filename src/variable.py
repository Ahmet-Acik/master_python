# src/variable.py


def get_integer():
    return 25


def get_string():
    return "twenty five"


def get_name():
    return "Ahmet Ahmetoglu"


def get_details():
    age = 25
    weight = 72.5
    is_student = True
    return f"{age} {weight} {is_student}"


def print_variable_types():
    print(type(get_integer()))
    print(type(get_string()))
    print(type(get_details()))
    print(type(True))


def print_boolean_values():
    print(True)
    print(True)
    print(True)
    print(True)


def print_combined_details():
    age = 26
    weight = 72.5
    is_student = False
    print(f"{age} {weight} {is_student}")


def print_datetime():
    print("2021-09-01 12:00:00")


def print_final_details():
    first_name = "Ahmet"
    last_name = "Ahmetoglu"
    age = 25
    weight = 74.5
    is_student = True
    print(f"{first_name} - {last_name} - {age} - {weight} - {is_student}")


def print_all():
    print(get_integer())
    print(type(get_integer()))
    print(get_string())
    print(get_name())
    print(get_details())
    print_variable_types()
    print_boolean_values()
    print_combined_details()
    print_datetime()
    print(type(get_string()))
    print(True)
    print_final_details()


if __name__ == "__main__":
    print_all()
