#  A Creating and Using a Simple Package Step
#1:Directory Structure
#my_package/
    #init .py
     #math_operations.py
     # #string_operations.py
#main.py


# math_operations.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
#string_operations.py:
def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()
#init .py file  
from .math_operations import add, subtract
from .string_operations import to_uppercase, to_lowercase
# new main.py file
import my_package

# Math operations
print(my_package.add(5, 3))
print(my_package.subtract(5, 3))

# String operations
print(my_package.to_uppercase('hello'))
print(my_package.to_lowercase('WORLD'))




# B.  Using External Packages:
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
print("Array multiplied by 2:", arr * 2)
print("Sum of array:", np.sum(arr))
print("Mean of array:", np.mean(arr))