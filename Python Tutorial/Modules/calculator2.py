from my_calculator import add,subtract,greeting

print(f"Using add(20, 10) directly: {add(20, 10)}")
print(f"Using subtract(50, 15) directly: {subtract(50, 15)}")
print(f"Direct greeting: {greeting('Bob')}")

# Try to use something not imported - it will cause an error
try:
    print(multiply(3, 3))
except NameError as e:
    print(f"Error! {e}. 'multiply' was not imported directly.")