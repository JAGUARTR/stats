#try exception handling
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("The result is:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

#catch 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("The result is:", result)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

#finally block
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution complete.")
