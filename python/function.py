 #A Defining and Calling Functions
#Define a function
def my_function():
    print("Hello from a function")
my_function()


#B Default Parameter Values and Arbitrary Arguments
# Function with a default parameter value
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}") # Arbitrary arguments
def print_names(*names):
    for name in names:
        print(name)
# Arbitrary keyword arguments
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Using the functions
greet("Jack") # Uses default greeting
print_names("Jack", "Sam", "Jessi")
print_key_values(name="Sam", age=30)


#C Return Values
def add(a, b):
    return a + b
result = add(5,10)
print(result)