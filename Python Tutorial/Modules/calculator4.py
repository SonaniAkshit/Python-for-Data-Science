# Tutorial: from module_name import * (Use with caution! ⚠️)

# Don't do this in large projects unless you fully understand the implications
from my_calculator import *

print(f"Directly calling divide(10, 2): {divide(10, 2)}")
print(f"Directly accessing PI: {PI}")

# Example of a potential name collision
# If you had your own 'add' function here, it would be overwritten
def add(x, y, z):
    return x + y + z

print(f"My local add(1,2,3): {add(1,2,3)}") # This is MY add function
# The 'add' from my_calculator is now shadowed/overwritten in this scope

# If you want to use my_calculator's add, you'd need to re-import it explicitly
# or avoid 'import *' in the first place and use 'import my_calculator'