# src/conditionals.py


def check_adult(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are a minor."


def check_age_group(age):
    if age >= 18:
        return "You are an adult."
    elif age >= 13:
        return "You are a teenager."
    else:
        return "You are a minor."


def check_driving_eligibility(age, has_license):
    if age >= 18:
        if has_license:
            return "You can drive."
        else:
            return "You can take driving test."
    else:
        return "You cannot drive."


def greet_name(name):
    if name == "Ahmet":
        return "Hello Ahmet!"
    else:
        return "Hello Stranger!"


def check_name_conditions(name):
    if (
        name.startswith("A")
        and name.endswith("t")
        and name.isalpha()
        and name.istitle()
        and len(name) == 5
    ):
        return "success"
    else:
        return "fail"


def check_name_any_conditions(name):
    if (
        name.isupper()
        or name.startswith("A")
        or name.endswith("t")
        or name.isalpha()
        or name.istitle()
    ):
        return "success"
    else:
        return "fail"


def compare_xyz(x, y, z):
    if x > y:
        return "x is greater than y"
    elif y > z:
        return "y is greater than z"
    else:
        return "z is greater than x and y"


def check_game(game):
    match game:
        case "football":
            return "You are playing football."
        case "basketball":
            return "You are playing basketball."
        case "tennis":
            return "You are playing tennis."
        case _:
            return "You are playing something else."


def get_month_name(month):
    match month:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return "Invalid month"


if __name__ == "__main__":
    print(check_adult(21))  # Output: You are an adult.
    print(check_age_group(15))  # Output: You are a teenager.
    print(check_driving_eligibility(21, True))  # Output: You can drive.
    print(greet_name("Ahmet"))  # Output: Hello Ahmet!
    print(check_name_conditions("Ahmet"))  # Output: success
    print(check_name_any_conditions("Ahmet"))  # Output: success
    print(compare_xyz(5, 10, 15))  # Output: z is greater than x and y
    print(check_game("football"))  # Output: You are playing football.
    print(get_month_name(4))  # Output: April
