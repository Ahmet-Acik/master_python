# src/conditionals.py

age = 20  # Example age value
is_adult = 'adult' if age >= 18 else 'minor'  # Ternary conditional expression
print(is_adult)  # Output: adult

# if-else statement
if age >= 18:
    print('You are an adult.')
else:
    print('You are a minor.')
    
# if-elif-else statement
if age >= 18:
    print('You are an adult.')
elif age >= 13:
    print('You are a teenager.')
else:
    print('You are a minor.')
    
# Nested if-else statement
has_license = True  # Example license status
if age >= 18:
    if has_license:
        print('You can drive.')
    else:
        print('You can take driving test.')
else:
    print('You cannot drive.')
    
# if-else statement with string comparison
name = 'Ahmet'  # Example name value
if name == 'Ahmet':
    print('Hello Ahmet!')
else:
    print('Hello Stranger!')
    
# if statement with multiple conditions
if name.startswith('A') and name.endswith('t') and name.isalpha() and name.istitle() and len(name) == 5:
    print('success')
else:
    print('fail')
    
# if statement with any condition
if name.isupper() or name.startswith('A') or name.endswith('t') or name.isalpha() or name.istitle():
    print('success')
else:
    print('fail')
    
# if-elif-else statement with multiple conditions
x, y, z = 5, 10, 15  # Example values
if x > y:
    print('x is greater than y')
elif y > z:
    print('y is greater than z')
else:
    print('z is greater than x and y')
    
# if-elif-else statement with match-case
game = 'football'  # Example game value
match game:
    case 'football':
        print('You are playing football.')
    case 'basketball':
        print('You are playing basketball.')
    case 'tennis':
        print('You are playing tennis.')
    case _:
        print('You are playing something else.')
        
# match-case statement with multiple cases
# Example grade value
grade = 'A'  # Example grade value
match grade:
    case 'A':
        print('Excellent')
    case 'B':
        print('Good')
    case 'C':
        print('Average')
    case 'D':
        print('Poor')
    case 'F':
        print('Fail')
    case _:
        print('Invalid grade')
        

# what else we can do with conditionals

# Function to check if a person is an adult
def check_adult(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are a minor."


# Function to check age group
def check_age_group(age):
    if age >= 18:
        return "You are an adult."
    elif age >= 13:
        return "You are a teenager."
    else:
        return "You are a minor."

# Function to check driving eligibility
def check_driving_eligibility(age, has_license):
    if age >= 18:
        if has_license:
            return "You can drive."
        else:
            return "You can take driving test."
    else:
        return "You cannot drive."

# Function to greet a person by name
def greet_name(name):
    if name == "Ahmet":
        return "Hello Ahmet!"
    else:
        return "Hello Stranger!"


# Function to check name conditions
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

# Function to check any name conditions
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

# Function to compare x, y, z values
def compare_xyz(x, y, z):
    if x > y:
        return "x is greater than y"
    elif y > z:
        return "y is greater than z"
    else:
        return "z is greater than x and y"

# Function to check the game being played
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

# Function to get month name
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
