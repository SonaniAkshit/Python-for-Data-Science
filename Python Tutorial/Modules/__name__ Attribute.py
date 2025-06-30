# Tutorial: The __name__ Attribute 🤔

# When you run this Jupyter cell, this script itself is being executed directly,
# so its __name__ is '__main__'.
print(f"This script's __name__ is: {__name__}")

import my_calculator # When my_calculator is imported, its __name__ is 'my_calculator'
print(f"my_calculator's __name__ is: {my_calculator.__name__}")

# Remember the __name__ block in my_calculator.py:
if __name__ == "__main__":
    print("This is my_calculator.py being run directly!")
# This line *did not* print when we imported it above.
# It would only print if you ran `python my_calculator.py` from your terminal.