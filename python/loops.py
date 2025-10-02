# If, else, and elif
def check_number():
    number = float(input("Enter a number: "))
    
    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print("The number is zero.")

if __name__ == "__main__":
    check_number()
   

# For Loop
def print_squares():
    print("\nSquares of numbers from 1 to 10:")
    for number in range(1, 11):
        square = number ** 2
        print(f"The square of {number} is {square}")

if __name__ == "__main__":
    print_squares()


# While Loop
def count_to_ten():
    count = 1
    while count <= 10:
        print(count)
        count += 1

if __name__ == "__main__":
    count_to_ten()
