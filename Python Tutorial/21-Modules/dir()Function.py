# Tutorial: dir() Function 🔍
import my_calculator
import math # A standard library module

print("Contents of the 'math' module:")
print(dir(math))
print("\nSome specific items from math:")
print(f"math.pi: {math.pi}")
print(f"math.sqrt(25): {math.sqrt(25)}")

print("\nContents of our 'my_calculator' module:")
print(dir(my_calculator))

# You can also use dir() without arguments to see current local scope
print("\nContents of current local scope:")
print(dir())