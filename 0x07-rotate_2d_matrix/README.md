# Rotate 2D Matrix

## Description
This project provides a Python function to rotate an n x n 2D matrix by 90 degrees clockwise in-place. It employs matrix manipulation techniques such as transposition and row reversal to achieve the rotation without requiring any additional space.

## Usage
To use the `rotate_2d_matrix` function, simply copy the code below into your Python script and pass the desired matrix as an argument. The function will modify the matrix in-place without returning anything.

```python
def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)


Output:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]



Approach
The rotation is achieved in two steps:

Transpose the matrix by swapping rows and columns.
Reverse each row of the transposed matrix.
Requirements
Python 3.8.10 or higher

