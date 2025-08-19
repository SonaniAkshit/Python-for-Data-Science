# 📦 Python Modules

---
### 1. What is a Module? 🤔
At its simplest, a module is a `.py` file containing Python definitions and statements. When you create a Python script and save it with a `.py` extension, that file itself is a module.

#### Why use modules?

- **Reusability:** Write code once, use it in many places.
- **Organization:** Keeps code logically structured and easy to manage.
- **Namespacing:** Prevents naming conflicts between different parts of your project.
- **Collaboration:** Different team members can work on different modules simultaneously.

### 2. Creating Your Own Module ✍️
Let's create a simple module named `my_calculator.py`. We'll put some basic math functions inside it.

>[Example`my_calculator.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/my_calculator.py)
###### Output:
```python
This is my calculator module!
PI Value: 3.14159
2 + 3 = 5
10 - 5 = 5
10 * 5 = 50
10 / 0 = ZeroDivisionError
Hello, john! welcome to my calculator module!
```

### 3. Importing Modules ➡️
Now, let's see how to use the functions and variables from our `my_calculator.py` module in another Python script

### 3.1. `import module_name`
This is the most common way. It imports the entire module, and you access its contents using `module_name.item`.

Let's create a simple python file named `calculator.py`. We'll import module.

>[Example`calculator.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/calculator.py)
###### Output:
```python
Using my_calculator.add(10,5) = 15
Using my_calculator.PI: 3.14159
Greeting from module: Hello, John! welcome to my calculator module!
```
### 3.2. `import module_name as alias`
You can give the module a shorter, more convenient alias.

>[Example`calculator1.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/calculator1.py)
###### Output:
```python
Hello, mr./miss john! welcome to my calculator module!
Addition of two numbers: 23 + 54 = 77
```
### 3.3. `from module_name import specific_item`
This allows you to import only specific functions, classes, or variables from a module directly into your current namespace. You can then use them without the `module_name`. prefix.


>[Example`calculator2.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/calculator2.py)
###### Output:
```python
Using add(20, 10) directly: 30
Using subtract(50, 15) directly: 35
Direct greeting: Hello, Bob! welcome to my calculator module!
Error! name 'multiply' is not defined. 'multiply' was not imported directly.
```

### 3.4. `from module_name import item1, item2`
Importing multiple specific items is just an extension of the previous method.

>[Example`calculator3.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/calculator3.py)
###### Output:
```python
Adding 5 and PI: 8.14159
```

### 3.5. `from module_name import *` (Caution! ⚠️)
This imports all public names (those not starting with an underscore `_`) from a module directly into your current namespace. While convenient, it's generally discouraged because it can lead to:

- **Name Collisions:** If you import `*` from multiple modules, or if your script has variables with the same names, you might overwrite things unintentionally.
- **Readability Issues:** It becomes harder to tell where a function or variable came from.

### 4. Module Search Path 🛣️
When you `import` a module, Python searches for it in a specific order:

1. **The directory containing the input script:** The current directory where your script is running.

2. `PYTHONPATH` **(if set):** An environment variable that lists additional directories.

3. **Standard library directories:** Locations where Python's built-in modules are installed.

4. **The contents of `.pth` files:** Site-specific configurations.

You can inspect the search path using the `sys` module:

>[Example`ModuleSearchPath.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/ModuleSearchPath.py)

### 5. `dir()` Function 🔍
The `dir()` function returns a list of names (attributes, functions, classes) defined in a module, object, or the current scope. It's great for exploring what's available in an imported module.

>[Example`dir()Function.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/dir()Function.py)

### 6. The `__name__` Attribute 🤔
Every Python module has a special built-in attribute called `__name__`. Its value depends on how the module is being used:

- If the module is being run directly as a script, `__name__` is set to `"__main__"`. 
- If the module is imported into another script, `__name__` is set to the module's name (e.g., `"my_calculator"`).

This is commonly used to include code that should only run when the script is executed directly (e.g., tests, setup code, command-line interfaces). We saw this in `my_calculator.py`.

>[Example`__name__Attribute.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/__name__Attribute.py)

### 7. Reloading Modules 🔄 (For development)
During development, if you modify a module file (`.py`) while your Python interpreter (or Jupyter kernel) is still running, `import` statements won't pick up the changes because Python caches imported modules. To see the changes without restarting, you can use `importlib.reload()`.

>[Example`ReloadingModules.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/ReloadingModules.py)

### 8. Standard Library Modules 📖
Python comes with a vast collection of pre-installed modules, known as the "Standard Library." These modules provide functionalities for almost anything you can imagine, from file operations and regular expressions to network communication and mathematical functions.

Some commonly used standard library modules include:

- `math`: Mathematical functions (e.g., `sqrt`, `sin`, `cos`, `pi`).
- `random`: Generating random numbers.
- `datetime`: Working with dates and times.
- `os`: Interacting with the operating system (e.g., file paths, directories).
- `sys`: System-specific parameters and functions.
- `json`: Working with JSON data.
- `re`: Regular expressions.

>[Example`StandardLibraryModules.py`.](https://github.com/SonaniAkshit/Python-for-Data-Science/blob/main/Python%20Tutorial/21-Modules/StandardLibraryModules.py)

### Conclusion 🎉
You've now got a solid grasp of Python Modules! They are the backbone of writing organized, reusable, and maintainable Python code. By leveraging modules effectively, you can build complex applications more easily and collaborate with others. Keep practicing by breaking your own projects into logical modules!

---

<p align="center">Happy modular coding! 🚀🐍</p>