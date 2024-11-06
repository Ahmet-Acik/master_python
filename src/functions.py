def greeting(name):
    print(f"Hello {name}!")


greeting("Ahmet")


def greet(name, age):
    print(f"Hello {name}! You are {age} years old.")


greet("Ahmet", 25)
greet(age=30, name="John")


def add_item(item, lst=None):  # default value for lst is None
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(add_item(5))
print(add_item(10))


def check_age_group(age):
    if age >= 18:
        return "You are an adult."
    elif age >= 13:
        return "You are a teenager."
    else:
        return "You are a child."


print(check_age_group(25))


def add_numbers(a, b):
    return a + b


print(add_numbers(5, 10))


def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.
    Args:
        a (int or float): The first number to multiply.
        b (int or float): The second number to multiply.
    Returns:
        int or float: The result of multiplying a and b.
        str: Error message if either a or b is zero.
    Raises:
        ValueError: If either a or b is zero.
    """
    
    if a == 0 or b == 0:
        return "Error: Multiplication by zero is not allowed." # return statement ends the function
    return a * b


print(multiply_numbers(5, 10))
print(multiply_numbers(0, 10))


result = greeting("Ahmet")
print(result) # None, the function does not return anything explicitly


say_hello = greeting
print(say_hello("Mehmet")) # Hello Ahmet!
