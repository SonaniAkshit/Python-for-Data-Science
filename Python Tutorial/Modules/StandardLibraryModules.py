# Tutorial: Standard Library Modules 📖

import math
import random
import datetime

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi from math module: {math.pi}")

print(f"Random number between 1 and 10: {random.randint(1, 10)}")
print(f"Random float between 0.0 and 1.0: {random.random()}")

now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Current year: {now.year}")

# Example of using 'os' module
import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")