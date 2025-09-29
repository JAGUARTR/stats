import numpy as np

# Function to take matrix input from the user
def input_matrix(n):
    matrix = []
    print(f"Enter the entries of a {n}x{n} matrix row by row:")
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print(f"Please enter exactly {n} values.")
            return input_matrix(n)
        matrix.append(row)
    return np.array(matrix)

# Get the size of the matrix from the user
n = int(input("Enter the size of the square matrix (e.g., 2 for 2x2): "))

# Get the matrix from the user
A = input_matrix(n)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenValues:")
print(eigenvalues)

print("\nEigenVectors:")
print(eigenvectors)
