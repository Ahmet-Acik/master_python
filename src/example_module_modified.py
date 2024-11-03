# example_module_modified.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Top-level code that should only run when the module is executed directly
    print("This will be printed when the module is executed directly.")
    print(greet("World"))
    
    name= "Ahmet"
    age= 25
    print(f"My name is {name} and I am {age} years old.")
