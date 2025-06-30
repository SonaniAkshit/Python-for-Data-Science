PI = 3.14159

def add(a,b):
    """Adds two numbers and returns the sum."""
    return a+b

def subtract(a,b):
    """Subtracts the second number from the first."""
    return a-b

def multiply(a,b):
    """Multiplies two numbers."""
    return a*b

def divide(a,b):
    """Divides the first number by the second. Handles division by zero."""
    if b == 0:
        return "ZeroDivisionError"
        # raise ZeroDivisionError
    return a/b

def greeting(name):
    return f'Hello, {name}! welcome to my calculator module!'

# This part runs only if the module is executed directly
if __name__ == '__main__':
    print("This is my calculator module!")
    print(f"PI Value: {PI}")
    print(f"2 + 3 = {add(2,3)}")
    print(f"10 - 5 = {subtract(10,5)}")
    print(f"10 * 5 = {multiply(10,5)}")
    print(f"10 / 0 = {divide(10,0)}")
    print(greeting('john'))
