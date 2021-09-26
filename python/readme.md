# Python Tutorial!
If you're at all familiar with programming, you've probably heard the term "Python" thrown around. Python is a POWERFUL, versatile programming language! It is one of the most popular languages used for data science and machine learning projects, as well as web programming. In fact, the backend of the Crimson's website is built on a Python web framework called [Django](https://www.djangoproject.com/).

In this lab, we are going to learn some fundamental concepts in Python programming. If you're new to programming (i.e., uncomfortable with variables, conditionals, and some object-oriented concepts like classes), you may want to start by watching (and following along) one of the videos linked in the Extra Resources section at the bottom of this page. Otherwise, feel free to jump into the Python Tutorial and start tackling the to-do list.

## Python Tutorial
1. [Hello World](https://www.w3schools.com/python/python_intro.asp)
2. [variables](https://www.w3schools.com/python/python_variables.asp)
3. [if statements](https://www.w3schools.com/python/python_conditions.asp)
4. [for loops](https://www.w3schools.com/python/python_for_loops.asp)
5. [while loops](https://www.w3schools.com/python/python_while_loops.asp)
6. [functions](https://www.w3schools.com/python/python_functions.asp)
7. [lists](https://www.w3schools.com/python/python_lists.asp)
8. [dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
9. [imports](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3)
10. [classes](https://www.w3schools.com/python/python_classes.asp)

## To-do List 
1. In `square_root.py`, write a function that returns the square root of a given integer `n`. If `n` is negative or not a number (i.e. `n` is a string), return `-1`.

2. In `random_ints.py`, write a program that randomly generates a number from the range [1,10] inclusive, appends it to the list `l`, and repeats this process until a `7` is generated and appended to `l`, at which point the program should return `l`.

    Hint: what does `(int) (random.random()*10)` generate? Can you adjust the range of its output?

3. In `sum.py`, write a program that takes a list `l` and a number `N` and returns `True` if any two numbers in the list sum to `N`, and `False` otherwise.

    For example: given `l = [1, 2, 4, 5, 6]` and `N = 10`, the program should return `True` because `4 + 6 = 10`.
    
    Hint: Use `set()`!

4. In `rm_smallest.py`, write a program that, given a dictonary, removes the key corresponding to the minimum value and returns the updated dictonary. If the dictionary is empty, the program should return the original dictionary.

    For example on input:
    ```Python
    sampleDict = {
      'Physics': 82,
      'Math': 65,
      'history': 75
    }
    ```
    The returned output should be:
    ```Python
    sampleDict = {
      'Physics': 82,
      'history': 75
    }
    ```

## Optional To-Do List/Extra Practice
* In company.py, define a class to represent companies. Companies should have a name (given at creation), a catalog (a dictionary of products and their prices, represented by strings and integers, respectively), and a list of current employees.

* Define a function to add a new product to the catalog. The function should take the name of the product and the price as arguments.

* Define a function to add an employee to the list of current employees. The function should take the name of the new employee as an argument.

* Define an employee class. Employees should have a name, a company, and a role, all given at creation. An employee's role should be represented by a number (i.e. `1` is a new hire, while `10` is the CEO). Make the role value optional, with the default set to `1`.

## Submit
Finished all the required exercises (and any optional exercises that looked interesting)? Make a Pull Request (PR), just like last week!

## Extra Resources
The YouTube channel Programming With Mosh is chock-full of awesome tutorials and mini-courses related to all things programming. Check out one or both of his mini beginner Python courses:
- [Python for Beginners - Learn Python in 1 Hour](https://youtu.be/kqtD5dpn9C8)
- [Python Tutorial - Python for Beginners](https://youtu.be/_uQrJ0TkZlc) (6 hours)