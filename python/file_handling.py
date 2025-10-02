# A Creating a File
import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Hello World!\n")
            print("File " + filename + " created successfully.")
    except Exception:
        print("Error: could not create file " + filename)

# B Reading from a File
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

# C Appending to a File
def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
            print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

if __name__ == "__main__":
    filename = "example.txt"
    create_file(filename)
    read_file(filename)
    append_file(filename, "I am Harsh.\n")
    read_file(filename)