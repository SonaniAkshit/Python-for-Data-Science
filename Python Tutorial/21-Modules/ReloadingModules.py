# Tutorial: Reloading Modules 🔄

import importlib
import my_calculator # Initial import

print(f"Initial PI value: {my_calculator.PI}")

# ----- Imagine you edit 'my_calculator.py' file NOW -----
# Change PI from 3.14159 to 3.0 in my_calculator.py
# Add a new function like 'power(base, exp)'

# To see these changes, we need to reload:
print("\n--- Please manually edit 'my_calculator.py' now ---")
print("  - Change `PI = 3.14159` to `PI = 3.0`")
print("  - Add a new function: `def power(base, exp): return base ** exp`")
print("  - Save the file.")
input("Press Enter after you've saved the changes to my_calculator.py...")

# Now, reload the module
importlib.reload(my_calculator)

print(f"\nAfter reloading, PI value: {my_calculator.PI}")
try:
    print(f"Using new power function: {my_calculator.add(2, 3)}")
except AttributeError as e:
    print(f"Error accessing new power function (did you save the file correctly?): {e}")