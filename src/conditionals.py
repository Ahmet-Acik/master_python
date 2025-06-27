def check_adult(age):
    return "You are an adult." if age >= 18 else "You are a minor."


def check_age_group(age):
    if age >= 18:
        return "You are an adult."
    elif 13 <= age < 18:
        return "You are a teenager."
    else:
        return "You are a minor."


def check_driving_eligibility(age, has_license):
    if age >= 18 and has_license:
        return "You can drive."
    elif age >= 18:
        return "You can take driving test."
    else:
        return "You cannot drive."


def greet_name(name):
    return f"Hello {name}!" if name == "Ahmet" else "Hello Stranger!"


def check_name_conditions(name):
    return "success" if name == "Ahmet" else "fail"


def check_name_any_conditions(name):
    return "success" if name.lower() in ["ahmet", "john"] else "fail"


def compare_xyz(x, y, z):
    if z > x and z > y:
        return "z is greater than x and y"
    elif x > y:
        return "x is greater than y"
    else:
        return "y is greater than z"


def check_game(game):
    games = ["football", "basketball", "tennis"]
    return f"You are playing {game}." if game in games else "You are playing something else."


def get_month_name(month):
    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return months.get(month, "Invalid month")
