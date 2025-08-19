import sys

print("Python's module search path (sys.path):")

for path in sys.path:
    print(f"- {path}")

# You can temporarily add a path (useful for testing or specific scenarios)
# sys.path.append("D:\GitHub Repo's\Python-for-Data-Science\Python Tutorial\Modules\my_calculator.py")
# print("\nPath after adding custom_modules:")
# for path in sys.path:
#     print(f"- {path}")